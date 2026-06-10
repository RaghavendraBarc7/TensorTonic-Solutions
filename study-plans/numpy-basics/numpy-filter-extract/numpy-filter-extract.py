import numpy as np

def filter_and_extract(data, row_start, row_stop, threshold):
    """
    Returns: 1D ndarray of float64
    """
    np_arr = np.array(data, dtype = np.float64)
    sub = np_arr[row_start:row_stop]
    mask = np.where(sub > threshold)
    return sub[mask]
    pass