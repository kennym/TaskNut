# -*- mode: python; coding: utf-8; -*-

"""
Test the Task class.
"""

__author__ = "Kenny Meyer"
__email__ = "knny.myer@gmail.com"

import unittest
from unittest import TestCase

import simplejson as json
from jsonpickle import Pickler, Unpickler
from os import path, remove

from src import Task

class TaskTests(TestCase):
    def setUp(self):
        self.task = Task()
        self.pickler = Pickler()
        self.unpickler = Unpickler()

    def test_get_json_representation(self):
        """Get the json representation for the __dict__ object of the Task object..."""
        task_dict = self.task.__dict__()
        json_dict = self.unpickler.restore(self.task.to_json())
        self.assertEquals(json_dict, task_dict)


if __name__ == "__main__":
    unittest.main()
