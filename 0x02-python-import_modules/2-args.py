#!/usr/bin/python3
if __name__ == "__main__":
    """Print the number of and list of arguments."""
    import sys

    count = len(sys.argv) - 1
    if count == 0:
        print('0 arguement.')
    elif count == 1:
        print('1 arguement:')
    else:
        print('{} arguements:'.format(count))
    for a in range(count):
        print('{}: {}'.format(a + 1, sys.argv[a + 1]))
