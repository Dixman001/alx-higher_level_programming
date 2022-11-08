#!/usr/bin/python3
"""the module defines the JSON write object"""
import json


def load_from_json_file(filename):
    """ the function creates the JSON of an object"""
    with open(filename) as a:
        return json.load(a)
