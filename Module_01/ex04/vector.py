import numpy as np


class Vector():

    # def __new__(cls,values):
    #     if isinstance(values,int):
    #         ls = []
    #         for i in range(values):
    #             ls.append([i])
    #         return Vector(ls)
    #     elif isinstance(values, tuple):
    #         ls = []
    #         for i in range(values[0],values[1]):
    #             ls.append([i])
    #         return Vector(ls)
    #     else:
    #         cls.__init__(cls,values)
    #deleteing above part new will make it wokr but without tuples or integers when passing. check tht, new its supposed to check frist an dthen call init with the rigt format, couldnt figure it out yet. to be continued

    def __init__(self, values):
        self.values = values
        size = len(values)
        if size > 1:
            self.shape = (size,1)
        elif size == 1:
            self.shape = (1,len(self.values[0]))
        else:
            self.shape = None

    def dot(self, vector):
        dot_product = 0
        size = len(vector.values)
        if not size == len(vector.values): return
        if size > 1:
            for i in range(size):
                value = self.values[i][0] * vector.values[i][0]
                dot_product += value
        elif size == 1:
            for i in range(len(self.values[0])):
                # not sure example in PDF is correct. Dot product of [1,3] and [2,4] is 14, not 13. Double checked it with numpy
                value = self.values[0][i] * vector.values[0][i]
                dot_product += value
        else: return
        return dot_product

    def T(self):
        ls = []
        size = len(self.values)
        if size > 1:
            for i in range(size):
                ls.append(self.values[i][0])
            return Vector([ls])
        elif size == 1:
            for i in range(len(self.values[0])):
                ls.append([self.values[0][i]])
            return Vector(ls)
        else: return
    
    def __str__(self):
        return str(self.values)

    __repr__ = __str__
    
    def __add__(self, vector):
        size = len(self.values)
        if not size == len(vector.values): return
        ls = []
        if size > 1:
            for i in range(size):
                value = self.values[i][0] + vector.values[i][0]
                ls.append([value])
            return Vector([ls])
        elif size == 1:
            for i in range(len(self.values[0])):
                value = self.values[0][i] + vector.values[0][i]
                ls.append(value)
            return Vector(ls)
        else: return

    def __radd__(self, vector):
        size = len(self.values)
        if not size == len(self.values): return
        ls = []
        if size > 1:
            for i in range(size):
                value = vector.values[i][0] + self.values[i][0]
                ls.append([value])
            return Vector([ls])
        elif size == 1:
            for i in range(len(self.values[0])):
                value = vector.values[0][i] + self.values[0][i]
                ls.append(value)
            return Vector(ls)
        else: return

    def __sub__(self, vector):
        size = len(self.values)
        if not size == len(vector.values): return
        ls = []
        if size > 1:
            for i in range(size):
                value = self.values[i][0] - vector.values[i][0]
                ls.append([value])
            return Vector([ls])
        elif size == 1:
            for i in range(len(self.values[0])):
                value = self.values[0][i] - vector.values[0][i]
                ls.append(value)
            return Vector(ls)
        else: return
    
    def __rsub__(self, vector):
        size = len(vector.values)
        if not size == len(self.values): return
        ls = []
        if size > 1:
            for i in range(size):
                value = vector.values[i][0] - self.values[i][0]
                ls.append([value])
            return Vector([ls])
        elif size == 1:
            for i in range(len(self.values[0])):
                value = vector.values[0][i] - self.values[0][i]
                ls.append(value)
            return Vector(ls)
        else: return

    def __truediv__(self, div):
        if div == 0: return 'Undefined' 
        size = len(self.values)
        ls = []
        if size > 1:
            for i in range(size):
                value = self.values[i][0] / div
                ls.append([value])
            return Vector([ls])
        elif size == 1:
            for i in range(len(self.values[0])):
                value = self.values[0][i] / div
                ls.append(value)
            return Vector(ls)
        else: return
    
    def __rtruediv__(self): return 'NotImplementedError: \'Division of a scalar by Vector is not defined here'

    def __mul__(self, mul):
        if not isinstance(mul,int): return 'only scalars (to perform multiplication of Vector by a scalar)'
        size = len(self.values)
        ls = []
        if size > 1:
            for i in range(size):
                value = self.values[i][0] * mul
                ls.append([value])
            return Vector([ls])
        elif size == 1:
            for i in range(len(self.values[0])):
                value = self.values[0][i] * mul
                ls.append(value)
            return Vector(ls)
        else: return

    __rmul__ = __mul__

v1 = Vector([[0.0, 1.0, 2.0, 3.0]])
#v2 = Vector([[0.0, 2.0, 3.0, 4.0]])
print(v1 * 3)
#v2 = Vector([[0.0], [1.0], [2.0], [3.0]])
#print(v1*100)
#a  = Vector(v1)

# class Vector2():
#     def __init__(self, values):
#         self.values = values
#         size = len(self.values)
#         if size > 1:
#             self.shape = (size,1)
#         elif size == 1:
#             self.shape = (1,len(self.values[0]))
#         else:
#             self.shape = None

#     def dot(self, vector):
#         dot_product = 0
#         size = len(vector.values)
#         if not size == len(vector.values): return
#         if size > 1:
#             for i in range(size):
#                 value = self.values[i][0] * vector.values[i][0]
#                 dot_product += value
#         elif size == 1:
#             for i in range(len(self.values[0])):
#                 not sure example in PDF is correct. Dot product of [1,3] and [2,4] is 14, not 13. Double checked it with numpy
#                 value = self.values[0][i] * vector.values[0][i]
#                 dot_product += value
#         else: return
#         return dot_product

#     def T(self):
#         ls = []
#         size = len(self.values)
#         if size > 1:
#             for i in range(size):
#                 ls.append(self.values[i][0])
#             return Vector2([ls])
#         elif size == 1:
#             for i in range(len(self.values[0])):
#                 ls.append([self.values[0][i]])
#             return Vector2(ls)
#         else: return
    
#     def __str__(self):
#         return str(self.values)

#     def __repr__(self):
#         return str(self.values)
    
#     def __add__(self, vector):
#         size = len(self.values)
#         if not size == len(vector.values): return
#         ls = []
#         if size > 1:
#             for i in range(size):
#                 value = self.values[i][0] + vector.values[i][0]
#                 ls.append([value])
#             return Vector2([ls])
#         elif size == 1:
#             for i in range(len(self.values[0])):
#                 value = self.values[0][i] + vector.values[0][i]
#                 ls.append(value)
#             return Vector2(ls)
#         else: return

#     __radd__ = __add__

#test shape
#print(Vector([[0.0], [1.0], [2.0], [3.0]]).shape)
#print(Vector([[0.0, 1.0, 2.0, 3.0]]).shape)

#test values
#print(Vector([[0.0], [1.0], [2.0], [3.0]]).values)
#print(Vector([[0.0, 1.0, 2.0, 3.0]]).values)

# test T
# v2 = Vector([[0.0, 1.0, 2.0, 3.0]])
# v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
# print(v1.T())


# test dot
# v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
# v2 = Vector([[2.0], [1.5], [2.25], [4.0]])
# v3 = Vector([[1.0, 3.0]])
# v4 = Vector([[2.0, 4.0]])
# print(v1.dot(v2))


# test shapes, T and again
# v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
# print(v1.shape)
# print(v1.T())
# print(v1.T().shape)
# v2 = Vector([[0.0, 1.0, 2.0, 3.0]])
# print(v2.shape)
# print(v2.T())
# print(v2.T().shape)

