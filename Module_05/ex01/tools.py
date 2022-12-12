import numpy as np


def add_intercept(x):
    """Adds a column of 1's to the non-empty numpy.array x.

    Args:
        x: has to be a numpy.array of dimension m * n.

    Returns:
        X, a numpy.array of dimension m * (n + 1).
        None if x is not a numpy.array.
        None if x is an empty numpy.array.

    Raises:
        This function should not raise any Exception.
    """
    if not type(x) == type(np.arange(1, 1)) or not np.any(x):
        return
    a = np.ones((x.shape[0], 1))
    if x.ndim == 1:
        x = x.reshape((len(x), 1))
    return np.hstack((a, x))
