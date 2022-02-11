from distutils.command.build_scripts import first_line_re
from xml.dom.minidom import ReadOnlySequentialNamedNodeMap
import pandas as pd
import csv
import plotly.figure_factory as ff
import random
import statistics
import plotly.graph_objects as go

df=pd.read_csv('data.csv')
data=df['Math_score'].tolist()
fig=ff.create_distplot([data],['Math_score'],show_hist=False)
fig.show()

mean=statistics.mean(data)
std_dev=statistics.stdev(data)

print('mean of population= ',mean)
print('std_dev of population= ',std_dev)

def random_set_of_mean(counter):
    dataset=[]
    for i in range(0,counter):
        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        dataset.append(value)
    mean=statistics.mean(dataset)
    return mean()

mean_list=[]
for i in range(0,1000):
    set_of_means=random_set_of_mean(100)
    mean_list.append(set_of_means)

std_dev=statistics.stdev(mean_list)
mean=statistics.mean(mean_list)
print('mean of sampling dis= ',mean)

fig=ff.create_distplot([mean_list],[])

first_std_dev_start,first_std_dev_end=mean-std_dev,mean+std_dev
second_std_dev_start,second_std_dev_end=mean-(2*std_dev),mean+(2*std_dev)
third_std_dev_start,third_std_dev_end=mean-(3*std_dev),mean+(3*std_dev)


