import requests

class BookerClient:
    BASE_URL = "https://restful-booker.herokuapp.com"

    def __init__(self):
        self.token = self.get_auth_token()

    def get_auth_token(self):
        response = requests.post(f"{self.BASE_URL}/auth", json={
            "username": "admin",
            "password": "password123"
        })
        return response.json().get("token")

    def get_bookings(self):
        return requests.get(f"{self.BASE_URL}/booking")

    def get_booking(self, booking_id):
        return requests.get(f"{self.BASE_URL}/booking/{booking_id}")

    def create_booking_valid(self, payload):
        return requests.post(f"{self.BASE_URL}/booking", json=payload)

    def delete_booking(self, booking_id):
        headers = {"Cookie": f"token={self.token}"}
        return requests.delete(f"{self.BASE_URL}/booking/{booking_id}", headers=headers)
