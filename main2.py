import pandas as pd
import plotly.express as px
import numpy as np
import csv
import os
data = pd.read_csv("csv/data3.csv")
print('data read')
a1 = []
a2 = []
with open('csv/data3.csv') as cf:
    readed = csv.DictReader(cf)
    for i in readed:
        a1.append(float(i['Marks In Percentage']))

        item = float(i['Days Present'])
        a2.append(item)
# print(a1)
# print(a2)
r = np.corrcoef(a1, a2)
print(f'The correlation of Marks In Percentage vs Days Present is : {r}')
# figure = px.scatter(data, x="Marks In Percentage", y="Days Present",
#                     title="Marks In Percentage vs Days Present")
# print('...')
# figure.show()
# print('done')
