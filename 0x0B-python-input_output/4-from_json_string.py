#!/usr/bin/python3
"""the module returns the JSON of an object"""
import json


def from_json_string(my_str):
    """ the function returns the JSON of an object"""
    return json.loads(my_str)
