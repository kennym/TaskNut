# -*- mode: python; coding: utf-8; -*-

"""
The database module.
"""

__author__ = "Kenny Meyer"
__email__ = "knny.myer@gmail.com"

import simplejson as json

class Handler(object):
    """The abstract class interface."""
    def __init__(self, file_name):
        self._file_name = file_name

    def write(self, obj, fp):
        """Serialize an object, and write to a specific file, if specified."""
        pass

    def load(self, fp=None):
        """Load a string object from file."""
        pass

class JSONHandler(Handler):
    def write(self, obj, fp=None):
        if fp: 
            fp = open(fp, "w")
        else:
            fp = open(self._file_name, "w")
        json.dump(obj, fp, indent=4, separators=(',', ':'), sort_keys=True)

    def load(self, fp=None):
        if not fp: 
            fp = open(self._file_name)
        else:
            fp = open(fp)
        return json.load(fp)

__all__ = ["Handler", "JSONHandler"]
