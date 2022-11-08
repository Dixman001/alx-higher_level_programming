#!/usr/bin/python3
"""this module writes a file"""


def read_file(filename=""):
    """this function writes file in utf-8"""
    with open(filename, "w", encoding="utf-8") as f:
        print(f.read(), end="")
