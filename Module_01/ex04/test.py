from vector import Vector

# addition
a = Vector([[1, 2, 3, 4]])
b = Vector([[10, 11, 12, 13]])
print('addition=', a+b)

# substraction
c = Vector([[1, 1, 1, 1]])
d = Vector([[10, 11, 12, 13]])
print('substraction=', c-d)

# multiplication
e = Vector([[1, 2, 3, 4]])
print('multiplication=', e*2)
# rmul
print('rmul=', e.__rmul__(2))

# truediv
f = Vector([[1, 2, 3, 4]])
print('truediv=', f/2)

# rtruediv
print('rtruediv=', f.__rtruediv__())
