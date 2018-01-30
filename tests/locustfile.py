from locust import TaskSet, task
from locust.contrib.fasthttp import FastHttpLocust

class UserBehavior(TaskSet):
    @task
    def index(self):
        self.client.get("/")

class WebsiteUser(FastHttpLocust):
    task_set = UserBehavior
    host = "http://www.google.com"
    min_wait = 0
    max_wait = 0