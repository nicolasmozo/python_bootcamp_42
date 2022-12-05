import sys

i = 1
s = ""
while i <= len(sys.argv[1:]):
    if i == len(sys.argv[1:]):
        s  += sys.argv[i].swapcase()
        break
    else:
        s  += sys.argv[i].swapcase() + " "
    i += 1
print(s[::-1])