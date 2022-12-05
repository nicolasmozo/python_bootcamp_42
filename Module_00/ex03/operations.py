import sys

x = sys.argv

if len(x) < 3:
    sys.exit()
if len(x) > 3:
    print("AssertionError: too many arguments")
    sys.exit()
if x[1].isnumeric() == False:
    print("AssertionError: only integers")
    sys.exit()

a = int(x[1])
b = int(x[2])

print("Sum:         ", a+b)
print("Difference:  ", a-b)
print("Product:     ", a*b)
if a != 0 and b != 0:
    print("Quotient:    ", a/b)
    print("Remainder:   ", a % b)
else:
    print("Quotient: ERROR (division by zero)")
    print("Remainder: ERROR (modulo by zero)")
