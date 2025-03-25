from fastapi import FastAPI, HTTPException
import traceback
from src.agent import analyze_stock

app = FastAPI()

@app.get("/analyze_stock/")
def get_stock_analysis(ticker: str, price: str, user_decision: str = None):
    """API to analyze stock price or accept manual input."""
    try:
        result = analyze_stock(ticker, price, user_decision)
        return result
    except Exception as e:
        error_message = f"❌ INTERNAL SERVER ERROR:\n{str(e)}\n\nTRACEBACK:\n{traceback.format_exc()}"
        print(error_message)  # Show detailed logs in terminal
        raise HTTPException(status_code=500, detail=error_message)  # Send error to Postman
