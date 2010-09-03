# -*- mode: python; coding: utf-8; -*-

"""
Class representation of the Task.
"""

__author__ = "Kenny Meyer"
__email__ = "knny.myer@gmail.com"

import simplejson as json
from jsonpickle import Pickler

p = Pickler()

class Task(object):
    def __init__(self):
        self.name = None
        self.times = {}
    
    def set_name(self, name):
        self.name = name
    
    def set_time(self, time, start_time=None, end_time=None):
        """Set the the start and end time for the task.

        A timedelta is represented as a list.
        """
        pass

    def to_json(self):
        return p.flatten(self.__dict__)
