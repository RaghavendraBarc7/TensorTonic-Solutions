import numpy as np

def reshape_array(data, operation):
    """
    Returns: ndarray of float64 with shape determined by the operation
    """
    df = np.array(data, dtype = np.float64)
    shape = df.shape
    if operation == 'flatten':
        return df.flatten()
    elif operation == 'transpose':
        return df.transpose()
    else:
        return np.expand_dims(df, axis = 0)
    pass
