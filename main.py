import pandas as pd
import plotly.express as px
import numpy as np
import csv
import os
data = pd.read_csv("csv/data4.csv")
print('data read')
a1 = []
a2 = []
with open('csv/data4.csv') as cf:
    readed = csv.DictReader(cf)
    for i in readed:
        a1.append(float(i['sleep in hours']))

        item = float(i['Coffee in ml'])
        a2.append(item)
# print(a1)
# print(a2)
r = np.corrcoef(a1, a2)
print(f'Correlation of Coffee intake vs sleep in Hrs is : {r}')
# figure = px.scatter(data,x="sleep in hours",y="week",color="Coffee in ml",  title="Coffee intake vs sleep in Hrs")
# print('...')
# figure.show()
# print('done')
