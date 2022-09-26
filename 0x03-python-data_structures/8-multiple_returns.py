#!/usr/bin/python3
def multiple_returns(i):
    if i != '':
        f_c = i[0]
    else:
        f_c = None
    return (len(i), i[0])
