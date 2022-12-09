import cv2
import matplotlib.pyplot as plt
import numpy
from os import path

class ImageProcessor:
    @staticmethod
    def load(pathh):
        if not path.exists(pathh):
            return print('Exception: FileNotFoundError -- strerror: No such fileordirectory')
        if path.getsize(pathh) == 0:
            return print('Exception: OSError -- strerror: None')
        image = cv2.imread(pathh)
        height = image.shape[0]
        width = image.shape[1]
        print(f'Loading image of dimensions {height} x {width}')
        return numpy.array(image)
    
    @staticmethod
    def display(array):
        plt.imshow(array)
        return plt.show()

