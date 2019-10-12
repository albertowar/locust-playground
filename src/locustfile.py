from locust import TaskSet, task, events
from locust.contrib.fasthttp import FastHttpLocust

class UserBehavior(TaskSet):
    @task
    def index(self):
        self.client.get("/")

class WebsiteUser(FastHttpLocust):
    task_set = UserBehavior
    min_wait = 0
    max_wait = 0
