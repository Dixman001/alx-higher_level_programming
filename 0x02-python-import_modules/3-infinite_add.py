#!/usr/bin/python3
if __name__ == "__main__":
    """Print the addition of all arguments."""
    from sys import argv
    varlen = len(argv) - 1

    total = 0

    for i in range(1, varlen + 1):
        total += int(argv[i])
    print(total)
