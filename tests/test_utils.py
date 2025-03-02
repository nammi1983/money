import unittest
from app.utils import fetch_stock_data, enforce_policies, update_policies

class TestUtils(unittest.TestCase):
    def test_fetch_stock_data(self):
        dates, prices = fetch_stock_data("AAPL")
        self.assertIsInstance(dates, list)
        self.assertIsInstance(prices, list)
        self.assertEqual(len(dates), len(prices))

    def test_enforce_policies(self):
        # Create a temporary policies file
        with open("app/policies.txt", "w") as file:
            file.write("min_value=100\nmax_value=1000")

        # Test enforcement
        self.assertEqual(enforce_policies(50), 100)  # Below min
        self.assertEqual(enforce_policies(1500), 1000)  # Above max
        self.assertEqual(enforce_policies(500), 500)  # Within range

    def test_update_policies(self):
        update_policies(200, 800)
        with open("app/policies.txt", "r") as file:
            policies = file.readlines()
        self.assertEqual(policies[0].strip(), "min_value=200.0")
        self.assertEqual(policies[1].strip(), "max_value=800.0")

if __name__ == "__main__":
    unittest.main()