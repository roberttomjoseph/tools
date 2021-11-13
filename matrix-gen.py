import numpy as np


def matrix_generator(n):
    matrix = np.array([])
    last_int = 1
    for i in range(n):
        matrix.append([])
        for i in range(n):
            matrix.append(last_int)
            last_int += 1
    print(matrix)


matrix_generator(10)