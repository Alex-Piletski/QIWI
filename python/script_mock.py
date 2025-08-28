import unittest
import time

def fake_get(url):
    if "payments" in url and "accounts" not in url:
        return {"data": [{"id": "123", "status": "SUCCESS"}]}
    if "accounts" in url:
        return {"accounts": [{"balance": {"amount": 100, "currency": "RUB"}}]}
    if "payments/test_123" in url:
        return {"status": "SUCCESS"}
    return {}

def fake_post(url, json):
    return {"status": "SUCCESS"}

class TestQiwiAPIMock(unittest.TestCase):
    payment_id = "test_123"

    def test_service_access(self):
        data = fake_get("payments")
        self.assertIn("data", data)
        self.assertIsInstance(data["data"], list)

    def test_balance_positive(self):
        data = fake_get("accounts")
        self.assertGreater(data["accounts"][0]["balance"]["amount"], 0)

    def test_create_payment(self):
        data = fake_post("transfer", {"id": self.payment_id})
        self.assertIn(data["status"], ["SUCCESS", "WAITING"])

    def test_payment_execution(self):
        data = fake_get(f"payments/{self.payment_id}")
        self.assertIn(data["status"], ["SUCCESS", "WAITING"])


if __name__ == "__main__":
    unittest.main()
