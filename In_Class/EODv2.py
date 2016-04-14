import csv
import math
import random
import statistics as st
import numpy as np
import matplotlib.pyplot as plt

typ_price_list = []
period_vol_list = []
volume_list = []
lister = []
close_list = []


def typical_price(row):
    temp_list = []
    typ_price = 0
    for i in row[2:5]:
        temp_list.append(float(i))
    typ_price = sum(temp_list)/3

    return(typ_price)

def period_volume(a_typ_val, a_volume):
    temp = float(a_volume)
    volume_list.append(temp)
    return float(a_volume) * a_typ_val


with open('goog.csv') as f: # automatically closes the file when done
    reader = csv.reader(f)
    headers = next(reader)
    print(headers)
    print('------')
    for row in (reader):
        typ_val = 0
        per_val = 0
        # for i, col in enumerate(row):
        #     print(row[i])
        typ_val = typical_price(row)
        per_val = period_volume(typ_val, row[5])

        #storing in a list
        typ_price_list.append(typ_val)
        period_vol_list.append(per_val)
        #temp_val = [float(row[4]) for i in ]
        #close_list.append(sum(temp_val))

def calculate_vwap():
    culm_list = [float(a*b) for a,b in zip(typ_price_list,period_vol_list)]
    lister = [float(i) / sum(volume_list) for i in culm_list]
    return lister


lister = calculate_vwap()

plt.plot(lister, color = 'red')
plt.plot(close_list)
plt.show()



