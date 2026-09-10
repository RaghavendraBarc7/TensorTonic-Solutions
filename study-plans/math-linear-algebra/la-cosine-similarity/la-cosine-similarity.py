import numpy as np

def cosine_similarity(a, b):
    """
    Returns: float in [-1, 1], cosine similarity between a and b.
    """
    x = np.asarray(a, dtype = np.float64)
    y = np.asarray(b, dtype = np.float64)

    dotProd = np.dot(x, y)
    modA = np.linalg.norm(x)
    modB = np.linalg.norm(y)
    if modA < 1e-10 or modB < 1e-10:
        return 0.0
    return float(dotProd/(modA*modB))