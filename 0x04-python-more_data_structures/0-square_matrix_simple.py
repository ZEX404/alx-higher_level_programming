#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    new_matrix = []
    for col in matrix:
        temp_list = []
        for i in col:
            new_i = i**2
            temp_list.append(new_i)
        new_matrix.append(temp_list)

    return new_matrix
