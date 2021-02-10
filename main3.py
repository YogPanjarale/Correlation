import pandas as pd
import plotly.express as px
import numpy as np
import csv
import os
data = pd.read_csv("csv/data2.csv")
print('data read')
a1 = []
a2 = []
with open('csv/data2.csv') as cf:
    readed = csv.DictReader(cf)
    for i in readed:
        print(i)
        a1.append(float(i['Size of TV']))

        item = float(i['Average time spent watching TV in a week (hours)'])
        a2.append(item)
# print(a1)
# print(a2)
r = np.corrcoef(a1, a2)
print(f'Correlation of Size of TV vs Average time spent watching TV in a week (hours) is : {r}')
# figure = px.scatter(data, x="Size of TV", y="Average time spent watching TV in a week (hours)",
#                     title="Size of TV vs Average time spent watching TV in a week (hours)")
# print('...')
# figure.show()
# print('done')
