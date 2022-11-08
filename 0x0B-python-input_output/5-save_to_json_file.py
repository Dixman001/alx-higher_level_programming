#!/usr/bin/python3
"""the module defines the JSON write object"""
import json


def save_to_json_file(my_obj, filename):
    """ the function writes the JSON of an object"""
    with open(filename, "w") as a:
        json.dump(my_obj, a)
