import unittest
import requests
import requests_mock

BASE_URL = "https://mock.qiwi/api"

class TestQiwiAPIMock(unittest.TestCase):
    payment_id = "test_123"

    def setUp(self):
        self.mocker = requests_mock.Mocker()
        self.mocker.start()

        self.mocker.get(f"{BASE_URL}/payments", 
                        json={"data": [{"id": "123", "status": "SUCCESS"}, {"id": "124", "status": "WAITING"}]})
        self.mocker.get(f"{BASE_URL}/accounts", 
                        json={"accounts": [{"balance": {"amount": 100, "currency": "RUB"}}]})
        self.mocker.post(f"{BASE_URL}/transfer", 
                         json={"status": "SUCCESS", "transactionId": "tx_001"})
        self.mocker.get(f"{BASE_URL}/payments/{self.payment_id}", 
                        json={"status": "SUCCESS", "id": self.payment_id})

    def tearDown(self):
        self.mocker.stop()

    def test_service_access(self):
        resp = requests.get(f"{BASE_URL}/payments")
        data = resp.json()
        print("Check service access response:", data)
        self.assertIn("data", data)

    def test_balance_positive(self):
        resp = requests.get(f"{BASE_URL}/accounts")
        data = resp.json()
        print("Check balance response:", data)
        self.assertGreater(data["accounts"][0]["balance"]["amount"], 0)

    def test_create_payment(self):
        resp = requests.post(f"{BASE_URL}/transfer", json={"id": self.payment_id})
        data = resp.json()
        print("Create payment response:", data)
        self.assertIn(data["status"], ["SUCCESS", "WAITING"])

    def test_payment_execution(self):
        resp = requests.get(f"{BASE_URL}/payments/{self.payment_id}")
        data = resp.json()
        print("Payment execution response:", data)
        self.assertIn(data["status"], ["SUCCESS", "WAITING"])


if __name__ == "__main__":
    unittest.main()
