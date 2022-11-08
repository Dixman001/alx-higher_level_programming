#!/usr/bin/python3
"""this module appends a file"""


def append_write(filename="", text=""):
    """this function appends file in utf-8"""
    with open(filename, "a", encoding="utf-8") as f:
        print(f.read(), end="")
