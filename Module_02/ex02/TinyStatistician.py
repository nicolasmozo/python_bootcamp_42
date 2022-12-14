class TinyStatistician:

    @staticmethod
    def mean(x):
        if len(x) == 0:
            return None
        temp = 0
        for i in x:
            temp += i
        return temp/len(x)

    @staticmethod
    def median(x):
        if len(x) == 0:
            return None
        x.sort()
        if len(x) % 2 == 0:
            return (((x[((len(x)//2) - 1)]) + (x[len(x)//2]))/2)
        else:
            return x[len(x)//2]

    @classmethod
    def quartiles(cls, x):
        if len(x) == 0:
            return None
        x.sort()
        middle = len(x)//2
        if len(x) % 2 == 0:
            return [cls.median(x[:middle]), cls.median(x[middle:])]
        else:
            # weird that in many videos on the internet and cacualtors calculate this as the median of the middle of the list in each side however using the numpy quantiles fucntion, returns what is on the pdf. Following the numpy fuction
            return [x[(len(x)//4)], cls.median(x[middle:])]

    @classmethod
    def var(cls, x):
        if len(x) == 0:
            return None
        x.sort()
        mean = cls.mean(x)
        var = 0
        for i in x:
            var += (i-mean)**2
        return var/(len(x))

    @classmethod
    def std(cls, x):
        if len(x) == 0:
            return None
        return cls.var(x)**0.5