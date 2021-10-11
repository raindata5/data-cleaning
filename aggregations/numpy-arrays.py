#[1]
#
import pandas as pd
import numpy as np
pd.set_option('display.width', 200)
pd.set_option('display.max_columns', 35)
pd.set_option('display.max_rows', 200)
pd.options.display.float_format = '{:,.2f}'.format
coviddaily = pd.read_csv("data/coviddaily720.csv", parse_dates=["casedate"])
ltbrazil = pd.read_csv("data/ltbrazil.csv")

#[2]
# method to getting all the unique location values and then making that into a list
loclist = coviddaily.location.unique().tolist()

#[3]
# getting sums of cases for each location
rowlist= []
casevalues = coviddaily[['location','new_cases']].to_numpy() #creating a numpy array

for loc in loclist: #iterating through each location in our list

# list comprehension to create an index number for each row then
# if statement to make sure the location in that row equals the current location in the loop
    cases = [casevalues[j][1] for j in range(len(casevalues)) if casevalues[j][0]==loc]
    rowlist.append(sum(cases)) #appending the sum of cases to a list without their accompanying countries

len(rowlist)
len(loclist)
# each location is added into a dataframe with it's accompanying aggregation since order is kept in both lists
casetotals = pd.DataFrame(zip(loclist,rowlist), columns = (['location','new_cases'])) # check what happens without parenthesis ***
casetotals.head()

#[4]
# preparing data by sorting on location and month and dropping rows that have null in temperature
ltbrazil = ltbrazil.sort_values(['station','month'])
ltbrazil = ltbrazil.dropna(subset=['temperature'])

#[5]
# looping through data one row at a time to get an average while excluding outliers

prev_station = 'ZZZ'
prev_temp = 0
rowlist = []

tempvalues = ltbrazil[['station','temperature']].to_numpy() #creating a numpy array

for i in range(len(tempvalues)):
    station = tempvalues[i][0] # taking the station of the first value
    temp = tempvalues[i][1] # taking the temp of the first value
    if (prev_station!=station): # this is to say if we are now on a different station
        if (prev_station!= 'ZZZ'): # this is to say once we are on a new station then the previous data can be appended to rowlist as a dictionary but for first iteration skip
            rowlist.append({'station':prev_station, 'avgtemp':tempcnt/stationcnt, 'stationcnt':stationcnt})
        tempcnt = 0 #intializing variable first then in subsequent iterations resetting var.
        stationcnt = 0 # intializing variable first then in subsequent iterations resetting var.
        prev_station = station #now setting previous station to the cu

    if ((0 <= abs(temp-prev_temp) <=3) or (stationcnt==0)): # this is to say that the current temp minus the previous month temp must be within 3 units otherwise it's consider as an outlier
        tempcnt += temp
        stationcnt += 1

    prev_temp = temp

rowlist.append({'station':prev_station, 'avgtemp':tempcnt/stationcnt, 'stationcnt':stationcnt})
rowlist[0:5]

#[6]
# placing the data into a dataframe
ltbrazilavgs = pd.DataFrame(rowlist)
ltbrazilavgs.head()
