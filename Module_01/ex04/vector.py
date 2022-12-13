class Vector():

    def __init__(self, values):
        if isinstance(values, int):
            ls = []
            for i in range(values):
                ls.append([float(i)])
            self.values = ls
            self.shape = len(ls)
        elif isinstance(values, tuple):
            if values[0] > values[1]:
                self.values = str('a > b is not possible. Must be a < b')
            else:
                ls = []
                for i in range(values[0], values[1]):
                    ls.append([float(i)])
                self.values = ls
                self.shape = len(ls)
        else:
            self.values = values
            size = len(values)
            if size > 1:
                self.shape = (size, 1)
            elif size == 1:
                self.shape = (1, len(self.values[0]))
            else:
                self.shape = None

    def dot(self, vector):
        dot_product = 0
        size = len(vector.values)
        if not size == len(vector.values):
            return
        if size > 1:
            for i in range(size):
                value = self.values[i][0] * vector.values[i][0]
                dot_product += value
        elif size == 1:
            for i in range(len(self.values[0])):
                # not sure example in PDF is correct. Dot product of [1,3] and [2,4] is 14, not 13. Double checked it with numpy
                value = self.values[0][i] * vector.values[0][i]
                dot_product += value
        else:
            return
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
        else:
            return

    def __str__(self):
        return str(self.values)

    __repr__ = __str__

    def __add__(self, vector):
        size = len(self.values)
        if not size == len(vector.values):
            return
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
        else:
            return

    def __radd__(self, vector):
        size = len(self.values)
        if not size == len(self.values):
            return
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
        else:
            return

    def __sub__(self, vector):
        size = len(self.values)
        if not size == len(vector.values):
            return
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
        else:
            return

    def __rsub__(self, vector):
        size = len(vector.values)
        if not size == len(self.values):
            return
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
        else:
            return

    def __truediv__(self, div):
        if div == 0:
            return 'Undefined'
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
        else:
            return

    def __rtruediv__(
        self): return 'NotImplementedError: \'Division of a scalar by Vector is not defined here'

    def __mul__(self, mul):
        if not isinstance(mul, int):
            return 'only scalars (to perform multiplication of Vector by a scalar)'
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
        else:
            return

    __rmul__ = __mul__
