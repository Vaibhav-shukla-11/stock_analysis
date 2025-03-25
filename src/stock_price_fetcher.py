# src/stock_price_fetcher.py

import requests
import yfinance as yf
from duckduckgo_search import DDGS

def fetch_stock_price_duckduckgo(ticker: str):
    """Fetch stock price using DuckDuckGo search."""
    query = f"{ticker} stock price"
    
    results = DDGS().text(query, max_results=5)
    
    for result in results:
        if "$" in result or "INR" in result:
            return {"ticker": ticker, "price": result}
    
    return {"ticker": ticker, "price": "Not Found"}

def fetch_stock_price_yfinance(ticker: str):
    """Fetch stock price using Yahoo Finance API."""
    try:
        stock = yf.Ticker(ticker)
        price = stock.history(period="1d")["Close"].iloc[-1]
        return {"ticker": ticker, "price": f"${price:.2f}"}
    except Exception as e:
        return {"ticker": ticker, "error": str(e)}
