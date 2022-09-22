#!/usr/bin/python3
if __name__ == "__main__":
    """Print the number of and list of arguments."""
    import sys

    sex = len(sys.argv) - 1
    if sex == 0:
        print('0 argument.')
    elif sex == 1:
        print('1 argument:')
    else:
        print('{} arguments:'.format(sex))
    for a in range(sex):
        print('{}: {}'.format(a + 1, sys.argv[a + 1]))
