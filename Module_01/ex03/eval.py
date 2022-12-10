class Evaluator:
    @staticmethod
    def zip_evaluate(coefs, words):
        if len(coefs) != len(words):
            return -1
        else:
            x = 0
            for i, j in zip(coefs, words):
                x += i * len(j)
            print(x)

    @staticmethod
    def enumerate_evaluate(coefs, words):
        if len(coefs) != len(words):
            return -1
        else:
            x = 0
            values = []
            for index, i in enumerate(words):
                values.append(len(i))
            for index, i in enumerate(values):
                for index2, j in enumerate(coefs):
                    if index == index2:
                        x += i * j
            print(x)
