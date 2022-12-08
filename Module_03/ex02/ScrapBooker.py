import cv2
import numpy as np
import matplotlib.pyplot as plt

class ScrapBooker:

    @classmethod
    def crop(self, array, dim, position=(0,0)):
        """Crops the image as a rectangle via dim arguments (being the new heightand width of the image) from the coordinates given by position arguments.
        
        Args:
        -----
            array: numpy.ndarray
            dim: tuple of 2 integers.
            position: tuple of 2 integers.
        
        Return:
        -------
            new_arr: the cropped numpy.ndarray.
            None (if combinaison of parameters not compatible).

        Raise:
        ------
            This function should not raise any Exception."""
        from_row = dim[1]
        to_row = dim[0] + 1
        from_col = position[1]
        to_col = position[0]
        arr = array[from_row:to_row,from_col:to_col]
        if np.size(arr) == 0:
            return None
        return arr
    
    @classmethod
    def thin(self, array, n, axis):
        """Deletes every n-th line pixels along the specified axis (0: Horizontal, 1: Vertical)
        
        Args:
        -----
            array: numpy.ndarray.
            n: non null positive integer lower than the number of row/column of the array(depending of axis value).
            axis: positive non null integer.
        
        Return:
        -------
            new_arr: thined numpy.ndarray.
            None (if combinaison of parameters not compatible).
            
        Raise:
        ------
            This function should not raise any Exception."""
        if axis == 0:
            axis = 1
        elif axis == 1:
            axis = 0
        else:
            return None
        return np.delete(array,slice(n-1,array.shape[1],n),axis=axis)

    @classmethod
    def juxtapose(self,array,n,axis):
        """
        Juxtaposes n copies of the image along the specified axis.

        Args:
        -----
            array: numpy.ndarray.
            n: positive non null integer.
            axis: integer of value 0 or 1.

        Return:
        -------
            new_arr: juxtaposed numpy.ndarray.
            None (combinaison of parameters not compatible).
        
        Raises:
        -------
            This function should not raise any Exception.
        """
        pass

arr = np.array("A B C D E F G H I".split() * 6).reshape(-1,9)
print(arr.shape)
print(ScrapBooker.thin(arr,3,0))