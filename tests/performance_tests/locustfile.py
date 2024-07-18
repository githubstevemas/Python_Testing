from locust import HttpUser, task


class UserBehavior(HttpUser):

    def on_start(self):
        self.client.post("/showSummary",
                                    data={"email": "john@simplylift.co"})

    @task(1)
    def index(self):
        self.client.get("/")

    @task(2)
    def show_summary(self):
        self.client.post("/showSummary", data={"email": "john@simplylift.co"})

    @task(3)
    def purchase_places(self):
        self.client.post("/purchasePlaces", data={
            "places": 1,
            "competition": "Spring Festival",
            "club": "Simply Lift"
        })
