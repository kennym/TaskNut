# -*- mode: python; coding: utf-8; -*-

"""
The database handler.
"""

__author__ = "Kenny Meyer"
__email__ = "knny.myer@gmail.com"

import simplejson as json
from jsonpickle import Pickler, Unpickler
from pprint import pprint


class Handler(object):
    """The abstract Handler class."""
    def __init__(self, file_name):
        self._file_name = file_name

    def write(self, obj):
        """Serialize an object"""
        raise ImplementionError("Abstract class.")

    def load(self):
        """Load a string object from file."""
        raise ImplementionError("Abstract class.")

    def load_obj(self, obj):
        """Load an object from file."""
        raise ImplementionError("Abstract class.")
    

class JSONHandler(Handler):
    pickler = Pickler()
    unpickler = Unpickler()

    def write(self, obj):
        """Serialize an object, and write to a specific file, if specified.

        The serializer should check that the identifier (name) of the task is in
        the database, if yes, then don't create the new task; otherwise, yes.
        """
        data = self.load()
        # Check if the task is already in the task list...
        for key in obj.keys():
            # If not, then add it to the dictionary to be serialized:
            if key not in data.keys():
                data[key] = obj[key]
            if key in data.keys():
                try:
                    data[key].update(obj[key])
                except AttributeError:
                    data.update(obj)

        data = self.pickler.flatten(data)
        fp = open(self._file_name, "w")
        json.dump(data, fp, indent=2, separators=(',', ':'), sort_keys=True)

    def load(self):
        """Load a whole database."""
        try:
            fp = open(self._file_name)
        except IOError, e:
            return {}
        return self.unpickler.restore(json.load(fp))

    def load_obj(self, obj_name):
        """Load an object from the database."""
        data = None
        try:
            with open(self._file_name) as f:
                data = self.unpickler.restore(json.load(f))
        except IOError, e:
            return {}
        return {obj_name : data[obj_name]}

    @property
    def task_list(self):
        """Return a list of tasks."""
        pprint(self.load(), indent=4)


__all__ = ["Handler", "JSONHandler"]
