#!/usr/bin/python3
"""base of class"""
import json
import csv
import turtle


class Base:
    """represents base of class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """ """
        if id is not None:
            self.id = id
        else:
            base.__nb_objects += 1
            self.id = Base.__nb_objects
