from locust import TaskSet, task, HttpLocust

class UserBehavior(TaskSet):
    @task
    def index(self):
        self.client.get("/")

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    host = "https://blooming-eyrie-27593.herokuapp.com/"
    min_wait = 0
    max_wait = 0