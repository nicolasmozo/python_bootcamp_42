def what_are_the_vars(*args, **kwargs):
    """..."""
    if not args:
        return lambda: None
    i = 0
    for x in args:
        setattr(ObjectC, f'var_{i}', x)
        i += 1
    for j, k in kwargs.items():
        for i in ObjectC.__dict__.keys():
            if i == j:
                return None
    for j, k in kwargs.items():
        setattr(ObjectC, j, k)
    return ObjectC(None)  # ,ObjectC(kwargs)


class ObjectC(object):
    def __init__(self, object):
        return None


def doom_printer(obj):
    if obj is None:
        print("ERROR")
        print("end")
        return
    for attr in dir(obj):
        if attr[0] != '_':
            value = getattr(obj, attr)
            print("{}: {}".format(attr, value))
    print("end")


if __name__ == "__main__":
    obj = what_are_the_vars(7)
    doom_printer(obj)
obj = what_are_the_vars(None, [])
doom_printer(obj)
obj = what_are_the_vars("ft_lol", "Hi")
doom_printer(obj)
obj = what_are_the_vars()
doom_printer(obj)
obj = what_are_the_vars(12, "Yes", [0, 0, 0], a=10, hello="world")
doom_printer(obj)
obj = what_are_the_vars(42, a=10, var_0="world")
doom_printer(obj)
# not working
obj = what_are_the_vars(42, "Yes", a=10, var_2="world")
doom_printer(obj)
