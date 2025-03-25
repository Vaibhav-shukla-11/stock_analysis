# stock_analysis
# AI-Powered Stock Analysis Backend

## 📌 Overview
This is a FastAPI-based backend that fetches **real-time stock prices** and provides **AI-powered analysis**.  
It integrates **LangChain**, **OpenAI**, and **DuckDuckGo API** for intelligent financial insights.

## 🚀 Features
- 📈 Fetches live stock prices
- 🤖 AI-generated insights on stock trends
- 🌐 Web search for additional stock-related news
- 🛠️ Manual fallback in case AI fails

## 🛠️ Installation Steps

1. **Clone the repository**  
   ```bash
  git clone <[GitHub Repo Link](https://github.com/Vaibhav-shukla-11/stock_analysis.git)>
cd <stock_ai_agent>
pip install -r requirements.txt
uvicorn src.api:app --reload


:- Create a virtual environment (optional but recommended):
python -m venv venv
source venv/bin/activate  # On Mac/Linux
venv\Scripts\activate     # On Windows

:- Install dependencies:
pip install -r requirements.txt
      --- requirenments.txt : fastapi==0.110.1
uvicorn==0.29.0
langchain==0.2.0
langchain-openai==0.1.1
langchain-community==0.2.0
openai==1.12.0
python-dotenv==1.0.1
requests==2.31.0
duckduckgo-search==3.9.5


:- Set up environment variables:

Create a .env file in the root directory:
OPENAI_API_KEY=your-api-key-here
DUCKDUCKGO_API_KEY=your-duckduckgo-key-here


:- Run the FastAPI server:
uvicorn src.api:app --reload


:- Test the API:

Open http://127.0.0.1:8000/docs for the Swagger UI.

Or, test directly in Postman with:

http://127.0.0.1:8000/analyze_stock/?ticker=AAPL&price=175.42



