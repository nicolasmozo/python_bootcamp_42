import random
import numpy as N


def generator(text, sep=" ", option=None):
    '''Splits the text according to sep value and yield the substrings.option precise if a action is performed to the substrings before it is yielded.'''
    if isinstance(text, str) == False:
        return print("ERROR")
    if isinstance(text, str) and text.isprintable() and option == 'shuffle' or option == 'unique' or option == 'ordered' or option == None:
        words = text.split(sep)
        if option == 'shuffle':
            n = len(words)
            print(n)
            for i in range(n):
                j = random.randint(0, n-1)
                element = words.pop(j)
                words.append(element)
                print(words)
                return
        if option == 'unique':
            res = N.array(words)
            unique = N.unique(res)
            print(unique)
            return
        if option == 'ordered':
            words.sort()
            for i in words:
                print(i)
            return
        for i in words:
            print(i)
        return
    else:
        print("ERROR")
        return
