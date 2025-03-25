import unittest
from src.agent import analyze_stock

class TestStockAgent(unittest.TestCase):

    def test_analyze_stock(self):
        """Test AI agent with a sample stock price."""
        result = analyze_stock("AAPL", "$175.42")
        print("Agent Response:", result)
        self.assertIn("analysis", result)

if __name__ == "__main__":
    unittest.main()
