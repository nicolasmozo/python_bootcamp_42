def ft_reduce(function_to_apply, iterable):
    """Apply function of two arguments cumulatively.Args:function_to_apply: a function taking an iterable.iterable: an iterable object (list, tuple, iterator).Return:A value, of same type of elements in the iterable parameter.None if the iterable can not be used by the function."""
    if isinstance(iterable, list) or hasattr(iterable, '__iter__') or isinstance(iterable, tuple):
        it = iter(iterable)
        value = next(it)
        for element in it:
            value = function_to_apply(value,element)
        return value
    return None

# lst = ['H','e','l','l','o',' ','w','o','r','l','d']
# #lst = [1,3,4,5]
# print(ft_reduce(lambda u, v: u + v, lst))