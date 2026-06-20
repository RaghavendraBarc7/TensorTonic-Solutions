import numpy as np

def norm_gate(X, W, threshold):
    """Returns: np.ndarray of shape (n, k), gated projection where rows below threshold are zeroed"""
    X = np.asarray(X, dtype = np.float64)
    W = np.asarray(W, dtype = np.float64)
    Y = X @ W
    norms = np.linalg.norm(Y, axis = 1)
    gates = np.where(norms[:, np.newaxis] < threshold, 0, Y).astype(np.float64)
    return gates
    pass