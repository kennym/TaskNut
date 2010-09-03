# -*- mode: python; coding: utf-8; -*-

"""
Test the Task class.
"""

__author__ = "Kenny Meyer"
__email__ = "knny.myer@gmail.com"

from unittest import TestCase

import simplejson as json
from jsonpickle import Pickler, Unpickler
from os import path, remove

from src import Task
from src import JSONHandler

class TaskTests(TestCase):
    def setUp(self):
        self.task = Task()
        self.pickler = Pickler()
        self.unpickler = Unpickler()

    def test_get_json_representation(self):
        """Get the correct json representation for the __dict__ object of the
        instantiated class..."""
        task_dict = self.task.__dict__
        json_dict = self.unpickler.restore(self.task.to_json())
        self.assertEquals(json_dict, task_dict)


class HandlerTests(TestCase):
    def setUp(self):
        file_name = "unit_test"
        self.database = file_name + ".json"
        self.json_handler = JSONHandler(self.database)
    
    def test_json_handler_writing(self):
        """Check the data integrity of the data in the files of the
        JSONHandler."""
        # Write information to database
        test_data = {"name": "Blabla"}
        self.json_handler.write(test_data)
        json_data = self.json_handler.load()
        self.assertEquals(json_data, test_data)
        # Be sure the handler doesn't tell us shits...
        test_data = {"name": "Blabladf"} # fake the data
        self.assertNotEqual(json_data, test_data)
        remove(self.database)

    def test_json_handler_write_to_custom_file(self):
        """Check that the data integrity still persists when writing to custom
        specified file object."""
        test_file = "other.json"
        # Write information to database
        test_data = {"name": "Blabla"}
        self.json_handler.write(test_data, test_file)
        json_data = self.json_handler.load(test_file)
        self.assertEquals(json_data, test_data)
        # Be sure the handler doesn't tell us shits...
        test_data = {"name": "Blabladf"} # fake the data
        self.assertNotEqual(json_data, test_data)
        
        # Clean up...
        remove(test_file)
