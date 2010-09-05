# -*- mode: python; coding: utf-8; -*-

"""
Class representation of the Task.
"""

__author__ = "Kenny Meyer"
__email__ = "knny.myer@gmail.com"

import simplejson as json
from jsonpickle import Pickler

from datetime import datetime

p = Pickler()

class Task(object):
    def __init__(self, name=None):
        self.name = name
        self.times = []
    
    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name
    
    def start_time(self):
        """Start a new timer for the task"""
        cur_time = datetime.now()
        time = [None, None]
        time[0] = repr(cur_time)
        time[1] = None
        print time
        self.times.append(time)

    def end_time(self):
        pass

    def to_json(self):
        """Return a JSON representation of the class."""
        return p.flatten(self.__dict__())

    def __dict__(self):
        return {str(self.name): 
                    {"times": 
                        self.times
                    }
               }
