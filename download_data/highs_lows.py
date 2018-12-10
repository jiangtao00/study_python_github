#! usr/bin/env python
# -*- encoding=utf-8 -*-
# __author__ = "john"
# date = 11/2018

import csv
from matplotlib import pyplot as plt
from datetime import datetime

# first_data = datetime.strptime("2014-7-1", '%Y-%m-%d')
# print(first_data)

# form the file receive the highest temperature
filename = "weather_data.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)
    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], '%Y-%m-%d')
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'miss data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
    # print(highs)

# use these data draw the picture
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
# set the format for the picture
plt.title("Daily high temperatures, July 2014", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()
