import numpy as np

def sort_with_indices(data, axis):
    """Returns: np.ndarray of shape (2, m, n), stacked sorted values and sort indices"""
    data = np.asarray(data, dtype = np.float64)
    sorted_data = np.sort(data, axis = axis)
    sort_with_indices = np.argsort(data, axis = axis)
    print(sorted_data, sort_with_indices)
    return np.stack([sorted_data, sort_with_indices])