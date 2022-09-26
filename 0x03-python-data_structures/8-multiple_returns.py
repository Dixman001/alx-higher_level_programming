#!/usr/bin/python3
def multiple_returns(i):
    if len(i) == 0:
        return None
    else:
        return (len(i), i[0])
