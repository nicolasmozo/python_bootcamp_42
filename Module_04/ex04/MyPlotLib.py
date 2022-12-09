import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class MyPlotLib:
    @staticmethod
    def histogram(data,features):
        # for i in features:
        #     plt.hist(data[i])
        #     plt.xlabel(i)
        for i in range(1,len(features)+1):
            plt.subplot(1,2,i)
            plt.hist(data[i])
        return plt.show()

df = pd.read_csv("athlete_events.csv")
f = ['Height','Weight']
# for i in range(1,len(f)+1):
#     print(i)

#print(df)
MyPlotLib.histogram(df,['Height','Weight'])
