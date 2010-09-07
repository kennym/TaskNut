#!/usr/bin/python2.6
# -*- mode: python; coding: utf-8; -*-

"""
The Time Tracker main module.
"""

__author__ = "Kenny Meyer"
__email__ = "knny.myer@gmail.com"

from sys import argv

from src import Tracker

def main():
    tracker = Tracker()
    if argv[1].startswith("track"):
        tracker.track(argv[2])
    elif argv[1].startswith("list"):
        tracker.fh.task_list
    elif argv[1].startswith("end"):
        tracker.end()
    else:
        print "Check your credits!"

if __name__ == "__main__":
    main()
