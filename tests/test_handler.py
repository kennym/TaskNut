# -*- mode: python; coding: utf-8; -*-

"""
A brief module description.
"""

__author__ = "Kenny Meyer"
__email__ = "knny.myer@gmail.com"

import unittest
from unittest import TestCase

import simplejson as json
from jsonpickle import Pickler, Unpickler
from os import path, remove

from src import JSONHandler
from src import Task


class HandlerTests(TestCase):
    def setUp(self):
        file_name = "unit_test"
        self.database = file_name + ".json"
        self.json_handler = JSONHandler(self.database)
    
    def tearDown(self):
        if path.exists("unit_test.json"): remove("unit_test.json")

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

    def test_json_handler_writing_multiple_tasks(self):
        """Save multiple tasks, and assert that they are existing in file."""
        task_1 = Task("Hello")
        task_2 = Task("Hello2")
        task_3 = Task("Hello3")
        # Create the test dictionary
        test_data = {}
        # Write the tasks to the file
        self.json_handler.write(task_1.to_json())
        self.json_handler.write(task_2.to_json())
        self.json_handler.write(task_3.to_json())
        # Load the data from the file.
        json_data = self.json_handler.load()
        # Check that the key exist in the file.
        for key in json_data.keys():
            self.assertTrue(key in [task_1.get_name(),
                                    task_2.get_name(),
                                    task_3.get_name()])
    
    def test_task_exists_only_once(self):
        """Verify that task is only written once to the database.

        The serializer should check that the identifier (name) of the task is in
        the database, if yes, then don't create the new task; otherwise, yes.
        """
        # Create identical tasks
        task_1 = Task("Hello")
        task_2 = Task("Hello")
        task_3 = Task("Hello")
        self.json_handler.write(task_1.to_json())
        self.json_handler.write(task_2.to_json())
        self.json_handler.write(task_3.to_json())
        json_data = self.json_handler.load()
        key_counter = 0
        for key in json_data.keys():
            key_counter += 1
        self.assertTrue(key_counter == 1)

    def test_load_object(self):
        task_1 = Task("Test1")
        self.json_handler.write(task_1.to_json())
        json_data = self.json_handler.load_obj("Test1")
        # Assert that the data is the same.
        self.assertEquals(json_data, task_1.__dict__())

    def test_load_objects(self):
        """Load an object from the JSON database."""
        task_1 = Task("Test1")
        task_2 = Task("Test2")
        task_3 = Task("Test3")
        self.json_handler.write(task_1.to_json())
        self.json_handler.write(task_2.to_json())
        self.json_handler.write(task_3.to_json())
        # Check the first instance
        json_data = self.json_handler.load_obj("Test1")
        self.assertEquals(json_data, task_1.__dict__())
        # Check the second instance
        json_data = self.json_handler.load_obj("Test2")
        self.assertEquals(json_data, task_2.__dict__())
        # Check the third instance
        json_data = self.json_handler.load_obj("Test3")
        self.assertEquals(json_data, task_3.__dict__())


if __name__ == "__main__":
    unittest.main()
