import numpy as np


def normalize(array1, array2):
    """
    Pixel by pizel division
    """
    normed = np.ma.masked_where(array2 <= 0.0, array1/array2)
    return normed