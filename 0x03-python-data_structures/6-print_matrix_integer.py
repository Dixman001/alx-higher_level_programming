#!/usr/bin/pyython3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for column in row:
            print('{;d}'.format(column), end=' ')
            if column == row:
                print('{:d}'.format(column), end='')
        print()