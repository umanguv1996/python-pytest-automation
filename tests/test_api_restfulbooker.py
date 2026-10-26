import pytest
import requests
from api.booker_client import BookerClient

@pytest.fixture(scope="module")
def client():
    return BookerClient()

@pytest.mark.api
def test_get_bookings(client):
    response = client.get_bookings()
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)

@pytest.mark.api
def test_create_and_get_booking(client):
    payload = {
        "firstname": "John",
        "lastname": "Doe",
        "totalprice": 150,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2026-01-01",
            "checkout": "2026-01-10"
        },
        "additionalneeds": "Breakfast"
    }
    create_res = client.create_booking_valid(payload)
    assert create_res.status_code == 200
    res_data = create_res.json()
    booking_id = res_data.get("bookingid")
    assert booking_id is not None

    get_res = client.get_booking(booking_id)
    assert get_res.status_code == 200
    assert get_res.json()["firstname"] == "John"

@pytest.mark.api
@pytest.mark.negative
def test_get_nonexistent_booking(client):
    response = client.get_booking(9999999)
    assert response.status_code == 404

@pytest.mark.api
def test_delete_booking(client):
    payload = {
        "firstname": "Jane",
        "lastname": "Smith",
        "totalprice": 200,
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2026-02-01",
            "checkout": "2026-02-05"
        }
    }
    create_res = client.create_booking_valid(payload)
    booking_id = create_res.json().get("bookingid")

    del_res = client.delete_booking(booking_id)
    assert del_res.status_code in [200, 201, 204]
