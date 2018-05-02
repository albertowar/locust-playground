from locust import HttpLocust, TaskSet, task, events, web
from flask import jsonify
import sys
import logging

logger = logging.getLogger()

logger.info('HI!')

class UserBehavior(TaskSet):
    @task
    def index(self):
        self.client.get("/")

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    host = "https://blooming-eyrie-27593.herokuapp.com/"
    min_wait = 0
    max_wait = 0

def on_slave_report(client_id, data,  *args, **kwargs):
    try:
        logger.info(data)
        logger.info(args)
        logger.info(kwargs)
    except Exception as e:
        logger.info(e.message)
    

events.slave_report += on_slave_report