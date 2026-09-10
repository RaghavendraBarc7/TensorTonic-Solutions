import numpy as np

def vector_norms(v):
    """
    Returns: float64 array of shape (3,) containing [L1, L2, L-inf] norms.
    """

    v = np.asarray(v, dtype = np.float64)
    
    l2_Norm = np.linalg.norm(v)
    l1_Norm = np.linalg.norm(v, ord = 1)
    lMax_Norm = np.linalg.norm(v, ord = np.inf)
    return np.asarray([l1_Norm, l2_Norm, lMax_Norm])