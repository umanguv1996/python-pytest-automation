from locust import HttpUser, task, between

class RestfulBookerUser(HttpUser):
    wait_time = between(1, 3)
    host = "https://restful-booker.herokuapp.com"

    @task(3)
    def get_all_bookings(self):
        self.client.get("/booking")

    @task(1)
    def health_check(self):
        self.client.get("/ping")
