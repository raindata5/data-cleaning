import pandas as pd
import numpy as np

#[1]
#
pd.set_option('display.width', 200)
pd.set_option('display.max_columns', 35)
pd.set_option('display.max_rows', 200)
pd.options.display.float_format = '{:,.2f}'.format
coviddaily = pd.read_csv("data/coviddaily720.csv", parse_dates=["casedate"])
ltbrazil = pd.read_csv("data/ltbrazil.csv")

#[2]
# sorting the data by location and casedate

coviddaily = coviddaily.sort_values(['location','casedate'])

#[3]
# looping through data one row at a time to get a running tally

prev_loc = 'ZZZ'
rowlist = []

for row in coviddaily.itertuples(): #iterates through each row in the DF
    if (prev_loc!=row.location): # this is to say if we are now on a different location
        if (prev_loc!='ZZZ'): # this is to say once we are on a new country then the previous data can be appended to rowlist as a dictionary but for first iteration skip
            rowlist.append({'location':prev_loc, 'casecnt':casecnt})
        casecnt=0 #keeping a count of each case per location
        prev_loc=row.location #now that we're on a new location which can change the prev_loc variable
    casecnt += row.new_cases #here we append the new cases

rowlist.append({'location':prev_loc, 'casecnt':casecnt}) #to append the data from the last location since we don't loop through again
len(rowlist)
rowlist[0:4]

#[4]
# creating our data from our list of dictionaries
covidtotals = pd.DataFrame(rowlist)
covidtotals.head()

#[5]
# preparing data by sorting on location and month and dropping rows that have null in temperature
ltbrazil = ltbrazil.sort_values(['station','month'])
ltbrazil = ltbrazil.dropna(subset=['temperature'])

#[6]
#  looping through data one row at a time to get an average while excluding outliers

prev_station = 'ZZZ'
prev_temp = 0
rowlist1 = []

for row in ltbrazil.itertuples():
    if (prev_station!= row.station): # this is to say if we are now on a different station
        if (prev_station!='ZZZ'): # this is to say once we are on a new country then the previous data can be appended to rowlist as a dictionary but for first iteration skip
           rowlist1.append({'station':prev_station, 'avgtemp':tempcnt/stationcnt, 'stationcnt':stationcnt})
        tempcnt = 0 #resetting var.
        stationcnt = 0 #resetting var.
        prev_station = row.station

# method to exclude outliers
    if((0<= abs(row.temperature-prev_temp <= 3 )) or (stationcnt == 0)) : # this is to say that the current temp minus the previous month temp must be within 3 units otherwise it's consider as an outlier
        tempcnt += row.temperature #keeping a sum of the temperature per location
        stationcnt += 1 #keeping a count of each temperature per location
    prev_temp=row.temperature

rowlist1.append({'station':prev_station, 'avgtemp':tempcnt/stationcnt, 'stationcnt':stationcnt}) #to append the data from the last station
rowlist1[:5]

ltbrazilavgs = pd.DataFrame(rowlist1)
ltbrazilavgs.head()
