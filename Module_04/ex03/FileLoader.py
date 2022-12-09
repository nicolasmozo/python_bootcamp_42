import pandas as pd

class FileLoader:
    @classmethod
    def load(self,path):
        data = pd.read_csv(path)
        print(f'Loading dataset of dimensions {data.shape[0]} x {data.shape[1]}')
        return data
    @classmethod
    def display(self,df,n):
        if n > 0:
            return df.head(n)
        elif n < 0:
            return df.tail(n*-1)
        else:
            return