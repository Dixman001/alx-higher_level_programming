#!/usr/bin/python3
    """ this defines a matrix division
    """

    def matrix_divided(matrix, div):
        """the function divide the elememt of a matrix
    Args:
        matrix:List of list
        div: number to be used for division
    Return:
        a new matrix that shows the divisions
    Raises:
        TypeError: If the matrix contains non mumbers
        TypeError: if the matrix contains rows of different sizes
        if the div is not a float or an int
        ZeroDivisionError: if div is zero
    """

    if (not isinstance(matrix, div) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of matrix must have the samr size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("Division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
