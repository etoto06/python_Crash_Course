import matplotlib.pyplot as plt
from matplotlib import pyplot as plt

# pd.read_csv('vally.csv')
import csv

# import os
# os.path 

# reader = csv.reader('vally.csv')
# for line in reader:
#     print(line)

x1,y1=[],[]

x2=[]
y2=[]

with open('sitka_weather_2021_full.csv') as f:
    reader = csv.reader(f)
    header = next(reader)
    for line in reader:
        # print(line)
        COL_DATE = 2
        x1.append(line[COL_DATE])
        COL_TMAX = 4
        y1.append(line[COL_TMAX])
        x2.append(line[2])
        y2.append(line[5])

for idx,h in enumerate(header):
    print(h)

plt.plot(x1,y1,label='TMAX')
plt.plot(x2,y2,label='TMIN')

plt.fill_between(x1,y1,y2, alpha0.5)

plt.legend()
plt.show()






try:
    with open('c.csv') as f
        for line in f:
            print(line)
except Exception as e:
    pass
        #print(e)