import numpy as np

def linear_combination(vectors, coefficients):
    vectors = np.asarray(vectors, dtype = np.float64)
    coefficients = np.asarray(coefficients, dtype = np.float64)

    print(vectors.shape, coefficients.shape, end = "\n")
    outer =  coefficients @ vectors
    return outer