def ft_map(function_to_apply, iterable):
    """Map the function to all elements of the iterable.Args:function_to_apply: a function taking an iterable.iterable: an iterable object (list, tuple, iterator).Return:An iterable.None if the iterable can not be used by the function."""
    if isinstance(iterable, list) or hasattr(iterable, '__iter__') or isinstance(iterable, tuple):
        for x in iterable:
            yield function_to_apply(x)
    return None


# li = [1,2,3,4,5]
# #li = ['a','b','ac']
# def fx(x):
#     return x+x
# print(hasattr(2,'__iter__'))
# print(list(ft_map(fx,li)))


# ft_map(fx,li)

# -----------------------------------
# ft_map using yield
# def generator(li):
#     for x in li:
#         yield x + x


# print(fx(x) for x in li if x%2 ==0) - returns address
# print([fx(x) for x in li if x%2 ==0]) - returns list if comprehension is within []
