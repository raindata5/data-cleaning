import pandas as pd
import numpy as np
import json
import pprint
import requests
from bs4 import BeautifulSoup

#editing display of our output
pd.set_option('display.width', 80)
pd.set_option('display.max_columns',6)
# making a get request to the site
webpage = requests.get("http://www.alrb.org/datacleaning/covidcaseoutliers.html")

#initializing the parser
bs = BeautifulSoup(webpage.text,'html.parser')

#taking the column names to create a sort of list
theadrows = bs.find('table',{'id':'tblDeaths'}).thead.find_all('th')
type(theadrows)
#creating a true list for the column names
labelcols = [j.get_text() for j in theadrows]
labelcols[0] = "rowheadings"
labelcols

#[]
# getting all the rows in the table
rows = bs.find('table', {'id':'tblDeaths'}).tbody.find_all('tr')
datarows = []
labelrows = []

for row in rows :
    rowlabels = row.find('th').get_text()
    cells = row.find_all('td',{'class':'data'})
    if (len(rowlabels) > 3):
        labelrows.append(rowlabels)
        print(rowlabels)
        print(len(rowlabels))
    if (len(cells) > 0):
        cellvalues = [j.get_text() for j in cells]
        datarows.append(cellvalues)


pprint.pprint(datarows[0:2])
pprint.pprint(labelrows[0:2])

#[]
# this gives me the first list in datarows then the insert method inserts the country name at the index of 0
for i in range(len(datarows)) :
    datarows[i].insert(0,labelrows[i])

#[] placing data in dataframe
totaldeaths = pd.DataFrame(datarows,columns = labelcols)

totaldeaths.head()
totaldeaths.dtypes

#[]
# modifying the column names, and changing the column types
totaldeaths.columns = totaldeaths.columns.str.lower().str.replace(' ','_')
for col in totaldeaths.columns[1:-1]: # changing all but the first and last column
    totaldeaths[col] = totaldeaths[col].str.replace(r'[^0-9]','').astype('int64')

totaldeaths['hospital_beds_per_100k'] = totaldeaths['hospital_beds_per_100k'].astype('float')
totaldeaths.head()
totaldeaths.dtypes
