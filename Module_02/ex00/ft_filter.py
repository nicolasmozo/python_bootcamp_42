def ft_filter(function_to_apply, iterable):
    """Filter the result of function apply to all elements of the iterable.Args:function_to_apply: a function taking an iterable.iterable: an iterable object (list, tuple, iterator).Return:An iterable.None if the iterable can not be used by the function."""
    if isinstance(iterable, list) or hasattr(iterable, '__iter__') or isinstance(iterable, tuple):
        ls = []
        [ls.append(x) for x in iterable if function_to_apply(x)]
        for i in ls:
            yield i
    return None

# def fx(x):
#     if x > 5:
#         return x

# ls = [1,2,3,4,5]

# print(ft_filter(lambda dum:not(dum % 2),ls))


# --------------------------------------
# how lamda works
# normal function
# def add(n1,n2):
#    return n1+n2

# lambda
# add = lambda n1,n2 : n1+n2 // first arguments, then what to do.
