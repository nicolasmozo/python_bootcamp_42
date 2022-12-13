import numpy as np

def simple_gradient(x, y, theta):
    """Computes a gradient vector from three non-empty numpy.array, without any for loop.
        The three arrays must have compatible shapes.
    
    Args:
        x: has to be a numpy.array, a matrix of shape m * 1.
        y: has to be a numpy.array, a vector of shape m * 1.
        theta: has to be a numpy.array, a 2 * 1 vector.
    
    Return:
        The gradient as a numpy.ndarray, a vector of dimension 2 * 1.
        None if x, y, or theta is an empty numpy.ndarray.
        None if x, y and theta do not have compatible dimensions.
    
    Raises:
        This function should not raise any Exception.
    """
    column_ones = np.ones((x.shape[0], 1))
    X = x.reshape((len(x), 1))
    XI = np.hstack((column_ones, X))
    XI_times_0 = XI.dot(theta)
    X0_minus_y = XI_times_0 - y # 2 dim
    XI_times_XO_minus_y = XI * X0_minus_y
    XT = XI_times_XO_minus_y.reshape((2,len(XI_times_XO_minus_y)))

    test = [1,2,3,4,5]
    return XT / 5

x = np.array([12.4956442, 21.5007972, 31.5527382, 48.9145838, 57.5088733]).reshape((-1, 1))
y = np.array([37.4013816, 36.1473236, 45.7655287, 46.6793434, 59.5585554]).reshape((-1, 1))
theta1 = np.array([2, 0.7]).reshape((-1, 1))
print(simple_gradient(x, y, theta1))
#print(x)
#print()
