import numpy as np

def row_summary(data, threshold):
    """Returns: np.ndarray of shape (3, m, n), stacked element mask, any-filtered, all-filtered"""
    data = np.array(data, dtype = np.float64)
    elem_mask = (data > threshold).astype(np.float64)
    any_row_mask = np.any(data > threshold, axis = 1)
    all_row_mask = np.all(data > threshold, axis = 1)
    final_data = np.stack([elem_mask, np.where(any_row_mask[:, np.newaxis], data, 0.0), \
                          np.where(all_row_mask[:, np.newaxis], data, 0.0)])
    print(final_data)
    return final_data
