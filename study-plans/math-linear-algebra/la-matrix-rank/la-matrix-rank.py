import numpy as np

def matrix_rank(A):
    return int(np.linalg.matrix_rank(np.array(A, dtype = float)))