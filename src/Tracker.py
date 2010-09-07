# -*- mode: python; coding: utf-8; -*-

"""
The tracker main module.
"""

__author__ = "Kenny Meyer"
__email__ = "knny.myer@gmail.com"

import simplejson as json

from os import path

from src import Task
from src import JSONHandler

class Tracker(object):
    # Class constants
    CURRENT = path.expanduser("~/.tt_running")

    def __init__(self):
        self.task = Task()
        self.fh = JSONHandler("test.json")

    def track(self, name):
        self.task.set_name(name)
        try:
            with open(self.CURRENT) as f:
                d = f.readline()
                if d:
                    print "Task", d, "already running."
                else:
                    f.close()
                    # Write task-name to ~/.tt_running
                    f = open(self.CURRENT, "w")
                    f.write(name)
                    f.close()
        except IOError:
            # Write task-name to ~/.tt_running
            f = open(self.CURRENT, "w")
            f.write(name)
            f.close()
        self.task.start_time()
        data = self.task.to_json()
        self.fh.write(data)

    # TODO:
    # Terminate task with given `task_name`
    #def end(self, task_name):
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

    def reset(self):
        """Reset the current running task."""
        # Empty the self.CURRENT file
        f = open(self.CURRENT, "w")
        f.write("").close()
