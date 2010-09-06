#!/usr/bin/python2.6
# -*- mode: python; coding: utf-8; -*-

"""
The Time Tracker main module.
"""

__author__ = "Kenny Meyer"
__email__ = "knny.myer@gmail.com"

import simplejson as json

from os import path
from sys import argv

from src import Task
from src import JSONHandler

class TimeTracker(object):
    CURRENT = path.expanduser("~/.tt_running")

    def __init__(self):
        self.task = Task()
        self.fh = JSONHandler("test.json")

    def track(self, name):
        self.task.set_name(name)
        # Write task-name to ~/.tt_running
        f = open(self.CURRENT, "w")
        f.write(name)
        f.close()
        self.task.start_time()
        data = self.task.to_json()
        self.fh.write(data)

    def end(self):
        # Read ~/.tt_running
        data = None
        try:
            f = open(self.CURRENT)
            data = f.readline()
            f.close()
        except IOError:
            pass

        if data:
            self.task.set_from_dict(self.fh.load_obj(data))
            # Debug:
            #print self.task.__dict__()
            self.task.end_time()
            self.fh.write(self.task.to_json())
        else:
            print "No task running."

    # TODO:
    #def reset(self):
    #    pass

def main():
    tracker = TimeTracker()
    if argv[1].startswith("track"):
        tracker.track(argv[2])
    elif argv[1].startswith("list"):
        tracker.fh.task_list
    elif argv[1].startswith("end"):
        tracker.end()
    else:
        print "Check your credits!"

if __name__ == "__main__":
    main()
