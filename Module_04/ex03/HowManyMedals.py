import pandas as pd
#from FileLoader import FileLoader

def how_many_medals(df,name):
    new = df[df['Name'] == name]
    medals = {}
    for i in new.iloc[:,9]:
        medals[i] = {
                    'G': len(new[(new['Medal'] == 'Gold') & (new['Year'] == i)]),
                    'S': len(new[(new['Medal'] == 'Silver') & (new['Year'] == i)]),
                    'B': len(new[(new['Medal'] == 'Bronze') & (new['Year'] == i)])}
    return medals