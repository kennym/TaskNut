# -*- mode: python; coding: utf-8; -*-

"""
The task object.
"""

__author__ = "Kenny Meyer"
__email__ = "knny.myer@gmail.com"

from jsonpickle import Pickler

from datetime import datetime


class Task(object):
    """The task object."""
    pickler = Pickler()

    def __init__(self, name=None):
        self.name = name
        self.times = []

    def set_name(self, name):
        """Set the name of the task object."""
        self.name = name

    def get_name(self):
        """Get the name of the task object."""
        return self.name

    def start_time(self):
        """Start a new timer for the task"""
        cur_time = datetime.now()
        time = None
        if len(self.times) == 0:
            time = [None, ""]
            time[0] = repr(cur_time)
            #print time
        elif len(self.times) > 0:
            for time in self.times:
                # If there's a task running...
                if time[0] and not time[1]:
                    print "There's a task running!"
                    break
                # Else if there's no task running...
                elif not time[0] and not time[1]:
                    time = [None, None]
                    time[0] = repr(cur_time)
        self.times.append(time)

    def end_time(self):
        """Set an end time of the task."""
        if len(self.times) == 0:
            print "You didn't start the task, yet!"
            return
        elif len(self.times) > 0:
            # Possible scenarios:
            #   - Task has no start time and no end time
            #   - Task has start time and no end time
            #   - Task has start time and end time
            #   - Task has no start time and has end time (Impossible!)
            for time in self.times:
                #: If has start time and no end time
                if time[0] and not time[1]:
                    # Set the end time...
                    time[1] = repr(datetime.now())
                #: If task has no start time and no end time
                if not time[0] and not time[1]:
                    break
                #: If has start and end time
                if time[0] and time[1]:
                    print "Task already ended."
                    # Nothing to do here, skip
                    continue
                # Task has no start time but end time - Should not happen!
                if not time[0] and time[1]:
                    # Fail whistling and shouting!
                    raise AssertionError("This should not have happened!")

    def show_stats(self):
        """Show statistics about the current task.

        | Name    | Duration     | From            | To
        +---------+--------------+-----------------+-------------------
        | <name>  | timedelta    |                 | 
        |         |              |                 |       
        |         |              |                 |     
        """
        return """
    | Name    | Duration     | From            | To
    +---------+--------------+-----------------+-------------------
    | %s      | %s           | %s              | %s
    |         |              |                 |       
    |         |              |                 |     
    """

    def to_json(self):
        """Return a JSON representation of the class."""
        return self.pickler.flatten(self.__dict__())

    def set_from_dict(self, dct):
        """Load the data from `dict`."""
        # In `dict` there should be no more than *one* key
        assert len(dct.keys()) == 1

        self.name = dct.keys()[0]
        self.times = dct.values()[0]["times"]

    def __dict__(self):
        return {str(self.name):
                    {"times":
                        self.times
                    }
               }

    def __str__(self):
        return "<%s name=%s, times=%s>" % (self.__class__, self.name,
                                           str(self.times))

    def __repr__(self):
        return self.__str__()
