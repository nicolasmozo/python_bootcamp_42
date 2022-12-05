import sys

if len(sys.argv) == 1:
    sys.exit()
if sys.argv[1].isnumeric() == False:
    print("AssertionError: argument is not an integer")
    sys.exit()
if int(sys.argv[1]) == 0:
    print("I'm Zero.")
    sys.exit()
if len(sys.argv) > 2:
    print("AssertionError: more than one argument are provided")
    sys.exit()
if int(sys.argv[1]) % 2 == 0:
    print("I'm Even.")
else:
    print("I'm Odd.")