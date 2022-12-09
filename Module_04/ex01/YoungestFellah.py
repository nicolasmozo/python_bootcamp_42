import pandas as pd
#from FileLoader import FileLoader 

def youngest_fellah(df,year):
    m = df[(df.iloc[:,9] == year) & (df['Sex'] == 'M')]
    f = df[(df.iloc[:,9] == year) & (df['Sex'] == 'F')]
    return {'f': f['Age'].min(), 'm': m['Age'].min()}