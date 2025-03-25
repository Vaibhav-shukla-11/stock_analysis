import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.agents import AgentType, initialize_agent

# Load environment variables
load_dotenv()

# Fetch OpenAI API Key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("ERROR: OPENAI_API_KEY is missing. Set it in your .env file or environment variables.")

# Initialize OpenAI LLM
llm = ChatOpenAI(openai_api_key=OPENAI_API_KEY)

# Initialize LangChain agent with the recommended way
search_tool = DuckDuckGoSearchRun()
agent = initialize_agent(
    tools=[search_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,  # Fix deprecation warning
    verbose=True
)

def analyze_stock(ticker: str, price: str, user_decision: str = None):
    """Analyzes stock price with AI or accepts manual input."""
    
    if user_decision:
        return {"ticker": ticker, "price": price, "analysis": f"User decided: {user_decision}"}

    prompt = f"""
    The stock price of {ticker} is currently {price}.
    Based on market trends, financial analysis, and investor sentiment,
    should I BUY, SELL, or HOLD this stock?
    Provide a well-reasoned explanation in simple terms.
    """

    try:
        response = agent.invoke(prompt)  # Corrected function call
        return {"ticker": ticker, "price": price, "analysis": response}
    except Exception as e:
        return {"ticker": ticker, "price": price, "error": f"AI analysis failed: {str(e)}"}
