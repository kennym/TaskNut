# -*- mode: python; coding: utf-8; -*-

"""
A collection of useful functions.
"""

__author__ = "Kenny Meyer"
__email__ = "knny.myer@gmail.com"

import datetime

def print_datetime(time):
    """Make a datetime object human-readable."""
    return time.strftime("%d-%m-%Y")
