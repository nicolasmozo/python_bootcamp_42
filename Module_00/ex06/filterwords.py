import sys
import re

if len(sys.argv) != 3:
    print("ERROR")
    exit()

words = sys.argv[1].split(" ")
temp = []
for word in words:
    new_str = re.sub(r'[\W_]', '', word)
    if (len(new_str)) > int(sys.argv[2]):
        temp.append(new_str)
print(temp)