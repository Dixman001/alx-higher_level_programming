#!/usr/bin/python3
"""this module reads a file"""


def read_file(filename=""):
    """this function reads file in utf-8"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
