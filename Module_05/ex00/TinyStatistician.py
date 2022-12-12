import math


class TinyStatistician:
    @staticmethod
    def mean(x):
        if not isinstance(x, list) or len(x) == 0:
            return None
        temp = 0
        for i in x:
            temp += i
        return float(temp/len(x))

    @staticmethod
    def median(x):
        if not isinstance(x, list) or len(x) == 0:
            return None
        x.sort()
        if len(x) % 2 == 0:
            return (((x[((len(x)//2) - 1)]) + (x[len(x)//2]))/2)
        else:
            return float(x[len(x)//2])

    @classmethod
    def quartile(cls, x):
        if not isinstance(x, list) or len(x) == 0:
            return None
        x.sort()
        middle = len(x)//2
        if len(x) % 2 == 0:
            return [cls.median(x[:middle]), cls.median(x[middle:])]
        else:
            # weird that in many videos on the internet and cacualtors calculate this as the median of the middle of the list in each side however using the numpy quantiles fucntion, returns what is on the pdf. Following the numpy fuction
            return [float(x[(len(x)//4)]), float(cls.median(x[middle:]))]

    @classmethod
    def var(cls, x):
        if not isinstance(x, list) or len(x) == 0:
            return None
        x.sort()
        mean = cls.mean(x)
        var = 0
        for i in x:
            var += (i-mean)**2
        # sample variance inclues a -1 in below formula. When population, removes the -1. Eg ex05,module_02
        # applies the same for standard deviation but using this variance fx, works
        return var/(len(x)-1)

    @classmethod
    def std(cls, x):
        if not isinstance(x, list) or len(x) == 0:
            return None
        return cls.var(x)**0.5

    @staticmethod
    def percentile(x, p):
        if not isinstance(x, list) or len(x) == 0:
            return None
        #r = (P / 100) * (N -1) + 1
        r = (p/100)*(len(x)-1) + 1
        # v(r) = v1 + rf (v2 - v1) // Interpolation https://www.free-online-calculator-use.com/percentile-calculator.html
        frac, whole = math.modf(r)
        return int(whole) + (frac * (10 - 1))
