#!/usr/bin/python3
"""
This module provides a function to divide all elements of a matrix.
"""

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number.

    Args:
        matrix: A list of lists containing integers or floats.
        div: A number (int or float) to divide the matrix elements by.

    Returns:
        A new matrix with all elements divided by div, rounded to 2 decimal places.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats,
                   or if rows are not of the same size,
                   or if div is not a number.
        ZeroDivisionError: If div is zero.
    """
    # Validate matrix type and structure
    if not isinstance(matrix, list) or not all(
        isinstance(row, list) for row in matrix
    ):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Validate that all elements are int or float and all rows are the same size
    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
        for elem in row:
            if not isinstance(elem, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Validate div
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Return new matrix
    return [[round(elem / div, 2) for elem in row] for row in matrix]
