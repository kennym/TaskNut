# -*- mode: python; coding: utf-8; -*-

"""
The Task class.
"""

__author__ = "Kenny Meyer"
__email__ = "knny.myer@gmail.com"


import datetime
from datetime import timedelta, time

from jsonpickle import Pickler, Unpickler

from src.utils import print_datetime


class AbstractTask(object):
    """The abstract Task interface.

    Only subclass this!
    """
    def __init__(self, name=None):
        pass

    def set_name(self, name):
        """Set the name of the task object."""
        raise NotImplementedError("Abstract class")

    def get_name(self):
        """Get the name of the task object."""
        raise NotImplementedError("Abstract class")

    def start_task(self):
        """Start a new task."""
        raise NotImplementedError("Abstract class")

    def end_task(self):
        """Set an end time of the task."""
        raise NotImplementedError("Abstract class")

    def show_stats(self):
        """Show the statistics of the current task."""
        raise NotImplementedError("Abstract class")

    def to_json(self):
        """Return a JSON representation of the class."""
        raise NotImplementedError("Abstract class")

    def set_from_dict(self, dct):
        """Apply the data from `dict` to the task."""
        raise NotImplementedError("Abstract class")


class Task(AbstractTask):
    """The task object."""
    #: A jsonpickle.Pickler() object, for serializing Python objects to JSON.
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

    def start_task(self):
        """Set a new time for the task"""
        cur_time = datetime.datetime.now()
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

    def end_task(self):
        """Set an end time of the task."""
        if len(self.times) == 0:
            print "You haven't started tracking the task, yet!"
            return
        elif len(self.times) > 0:
            # Possible scenarios:
            #  - Task has no start time and no end time
            #  - Task has start time and no end time
            #  - Task has start time and end time
            #  - Task has no start time and has end time (Impossible!)
            for time in self.times:
                #: If has start time and no end time
                if time[0] and not time[1]:
                    # Set the end time...
                    time[1] = repr(datetime.datetime.now())
                #: If task has no start time and no end time
                if not time[0] and not time[1]:
                    break
                #: If has start and end time
                if time[0] and time[1]:
                    print "Task already ended."
                    # Nothing to do here, skip
                    continue
                #: Task has no start time but end time - Should not happen!
                if not time[0] and time[1]:
                    #: Fail whistling and shouting!
                    raise AssertionError("This should not have happened!")

    def show_stats(self):
        """Show the statistics of the current task."""
        duration = self._calculate_duration()
        return """
    | Name       | %s
    +------------+------------
    | Duration   | %s
    | ->From     | %s
    | ->To       | %s
    """ % (self.name,
           duration,
           print_datetime(eval(self.times[0][0])),
           print_datetime(eval(self.times[0][1])))

    def to_json(self):
        """Return a JSON representation of the class."""
        return self.pickler.flatten(self.__dict__())

    def set_from_dict(self, dct):
        """Apply the data from `dict` to the task."""
        #: In `dict` there should be no more than *one* key
        assert len(dct.keys()) == 1

        self.name = dct.keys()[0]
        self.times = dct.values()[0]["times"]

    def _calculate_duration(self):
        """Calculate the timedelta or duration of the task's time/s.

        @return datetime.time: a datetime.time object.
        """
        unpickler = Unpickler()
        restore = unpickler.restore
        duration = None
        for timer in self.times:
            duration = eval(timer[1]) - eval(timer[0])
        return time(second=duration.seconds,
                    microsecond=duration.microseconds).isoformat()

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
