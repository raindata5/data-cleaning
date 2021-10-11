#[1]
#

import pandas as pd
import numpy as np
import os
pd.set_option('display.width', 200)
pd.set_option('display.max_columns', 35)
pd.set_option('display.max_rows', 50)
pd.options.display.float_format = '{:,.2f}'.format

#[2]
# reading in 2 data sets
ltcameroon = pd.read_csv("data/ltcountry/ltcameroon.csv")
ltpoland = pd.read_csv("data/ltcountry/ltpoland.csv")

#[3]
# checking the shape of the datasets to see if they have the same amount of columns and then concatenating them

ltcameroon.shape
ltpoland.shape

lt_con = pd.concat([ltcameroon,ltpoland])

#[4]
# method for concatenating multiple files in a directory that end with .csv

directory = "data/ltcountry"
lt_con = pd.DataFrame() #initializing a dataframe

for filename in os.listdir(directory): # listing all the contents in the directory
    if filename.endswith(".csv") : #making sure it's a csv file
        fileloc = os.path.join(directory, filename) # appending the directory and the filename to our cwd
        # now opening the file
        with open(fileloc) as f :
            ltnew = pd.read_csv(fileloc)
            print(filename + ' has ' + str(ltnew.shape[0]) + ' rows.') #confirming how many rows the dataset has
            lt_con = pd.concat([lt_con,ltnew]) # concatenating the new dataframe to lt_con
            # checking for differences in columns
            columndiff = lt_con.columns.symmetric_difference(ltnew.columns)
            if (not columndiff.empty) :
                print("", "Different column names for:", filename,columndiff, "", sep="\n")


#[5]
# sampling the dataset to explore it a bit
lt_con[['country','station','month','temperature','latitude']].sample(5, random_state=1)

#[6]
# since oman was missing a column this explains the null values we get and also we check the value counts for each with the rows printed prior
# when loading in the data
lt_con.country.value_counts().sort_index()
lt_con.groupby(['country']).agg({'temperature':['min','mean','max','count'],'latabs':['min','mean','max','count']})

#[7]
# Oman is above the equator thus the latitude would be positive
lt_con['latabs'] = np.where(lt_con.country=="Oman", lt_con.latitude, lt_con.latabs)
lt_con.groupby(['country']).agg({'temperature':['min','mean','max','count'],'latabs':['min','mean','max','count']})
