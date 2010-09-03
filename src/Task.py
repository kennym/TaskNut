# -*- mode: python; coding: utf-8; -*-

"""
Class representation of the Task.
"""

__author__ = "Kenny Meyer"
__email__ = "knny.myer@gmail.com"

import simplejson as json

class Task(object):
    def __init__(self):
        self.name = None
    
    def set_name(self, name):
        self.name = name

    def to_json(self):
        return json.dumps(self.__dict__)
