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
