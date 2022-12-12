import pandas as pd
#from FileLoader import FileLoader

def proportion_by_sport(df,year,sport,gender):
    new = df[(df.iloc[:,9] == year) & (df['Sex'] == gender) & (df['Sport'] == sport)].drop_duplicates(subset=['ID'])
    return new.shape[0] / df[(df.iloc[:,9] == year) & (df['Sex'] == gender)].drop_duplicates(subset=['ID']).shape[0]