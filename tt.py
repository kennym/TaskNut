# -*- mode: python; coding: utf-8; -*-

"""
The Time Tracker main module.
"""

__author__ = "Kenny Meyer"
__email__ = "knny.myer@gmail.com"

import simplejson as json
from sys import argv

from src import Task
from src import JSONHandler


class TimeTracker(object):
    def __init__(self):
        self.task = Task()
        self.fh = JSONHandler("test.json")

    def track(self, name):
        self.task.set_name(name)
        data = self.task.to_json()
        self.fh.write(data)
        print self.fh.load()

def main():
    tracker = TimeTracker()
    if argv[1].startswith("track"):
        tracker.track(argv[2])

if __name__ == "__main__":
    main()
