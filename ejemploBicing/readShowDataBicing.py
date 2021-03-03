import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

bicingdata = pd.read_csv('bicing.output',sep=",")
#print(bicingdata['ebikes'])

bicingBruc = bicingdata[bicingdata['name']=="C/ BRUC, 66"]
#print(bicingBruc)

f, (p1,p2) = plt.subplots(2)

sns.stripplot(ax=p1,x=bicingdata['normal_bikes'], y=bicingdata['name'][0:30],data=bicingdata)
p2.plot(bicingBruc['time'],bicingBruc['empty_slots'])
plt.show()

