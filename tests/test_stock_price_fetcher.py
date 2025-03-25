import unittest
from src.stock_price_fetcher import fetch_stock_price_duckduckgo, fetch_stock_price_yfinance

class TestStockPriceFetcher(unittest.TestCase):

    def test_fetch_stock_price_duckduckgo(self):
        """Test DuckDuckGo stock price fetcher."""
        result = fetch_stock_price_duckduckgo("AAPL")
        print("DuckDuckGo:", result)  # Debugging
        self.assertIn("price", result)
        self.assertIsInstance(result["price"], str)

    def test_fetch_stock_price_yfinance(self):
        """Test Yahoo Finance stock price fetcher."""
        result = fetch_stock_price_yfinance("AAPL")
        print("Yahoo Finance:", result)  # Debugging
        self.assertIn("price", result)
        self.assertTrue("$" in result["price"] or "error" in result)

if __name__ == "__main__":
    unittest.main()
