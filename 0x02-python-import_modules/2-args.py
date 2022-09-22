#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    sex = len(sys.argv) - 1
    if sex == 0:
        print('0 arguement.')
    else:
        print('{} arguements:'.format(sex))
    for a in range(sex):
        print('{}: {}'.format(a + 1, sys.argv[a + 1]))
