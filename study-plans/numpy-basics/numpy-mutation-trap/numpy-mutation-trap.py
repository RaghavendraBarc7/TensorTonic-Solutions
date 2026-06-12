import numpy as np

def original_and_clipped(data, row_idx, lo, hi):
    """
    Returns: 2D ndarray of float64 with shape (2, ncols)
    """
    data = np.array(data, dtype = np.float64)
    row_data = data[row_idx, :].copy()
    row_data[row_data < lo] = lo
    row_data[row_data > hi] = hi 
    return np.stack([data[row_idx, :], row_data])
    pass