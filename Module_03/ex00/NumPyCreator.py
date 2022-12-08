import numpy

class NumpyCreator:
    
    @classmethod
    def from_list(self, lst, datatype=None):
        for i in lst: 
            if len(i) != len(lst[0]):
                return None
        if type(lst) != type([1,2]):
            return None
        arr = numpy.array(lst, dtype=datatype)
        return numpy.append(arr,arr.dtype)
    
    @classmethod
    def from_tuple(self,tpl):
        if type(tpl) != type(('a','b')):
            return None
        return self.from_list(list(tpl))

    @classmethod
    def from_iterable(self, itr, datatype=None):
        if numpy.iterable(itr) == False:
            return None
        arr = numpy.fromiter(itr,dtype=datatype)
        return numpy.append(arr,arr.dtype)
    
    @classmethod
    def from_shape(self, shape,value=0):
        return numpy.full(shape,value)
    
    @classmethod
    def random(self,shape):
        return numpy.random.random(shape)
    
    @classmethod
    def identity(self, n):
        return numpy.identity(n)