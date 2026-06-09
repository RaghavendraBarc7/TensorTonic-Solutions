import numpy as np

def select_by_index(arr, indices, axis):
    """
    Returns: 2D ndarray of float64
    """

    np_arr = np.asarray(arr, dtype = np.float64)
    return np.take(np_arr, indices, axis = axis)
    

    
    pass