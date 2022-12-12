import numpy as np


def predict_(x, theta):
    """Computes the vector of prediction y_hat from two non-empty numpy.array.

    Args:
        x: has to be an numpy.array, a vector of dimension m * 1.
        theta: has to be an numpy.array, a vector of dimension 2 * 1.

    Returns:
        y_hat as a numpy.array, a vector of dimension m * 1.
        None if x and/or theta are not numpy.array.
        None if x or theta are empty numpy.array.
        None if x or theta dimensions are not appropriate.

    Raises:This function should not raise any Exceptions.
    """
    t = type(np.arange(1, 1))
    if not type(x) == t or not type(theta) == t or not np.any(x) or not np.any(theta) or not x.ndim == 1 or not theta.shape == (2, 1):
        return
    a = np.ones((x.shape[0], 1))
    x = x.reshape((len(x), 1))
    ax = np.hstack((a, x))
    return ax.dot(theta)
