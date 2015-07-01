# -*- coding: utf-8 -*-

from heck import *

import random

from locust import TaskSet, task, HttpLocust, events
from locust.stats import global_stats
import tests.qa.apis.performance.url_utils as url_utils


def on_quitting():
    total = global_stats.aggregated_stats(full_request_history=True)
    for k, v in total.__dict__.iteritems():
        if k.startswith("_"):
            break
        else:
            print '{}: {}'.format(k, total.__dict__[k])
    # ToDo save item into csv file


class UserBehavior(TaskSet):

    def __init__(self, parent=None):
        super(UserBehavior, self).__init__(parent=parent)
        self.source = random.choice(url_utils.sources)

    @task(1)
    def test_items(self):
        url = self.source.urls.next()
        self.client.get(url, headers=self.source.header)


class APIUser(HttpLocust):

    if not events.quitting._handlers:
        events.quitting += on_quitting

    task_set = UserBehavior
    min_wait = 1
    max_wait = 1
