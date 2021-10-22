#[1]
#

import pandas as pd
import os
import sys

#[2]
#
sys.path.append(os.getcwd() + "/helperfunctions")
import combineaggfunctions as caf
import importlib
importlib.reload(caf)

#[3]
# reading in datasets
coviddaily = pd.read_csv("data/coviddaily720.csv")
ltbrazil = pd.read_csv("data/ltbrazil.csv")
countries = pd.read_csv("data/ltcountries.csv")
locations = pd.read_csv("data/ltlocations.csv")

#[4]
# testing function with and without outlier criterion
caf.adjmeans(coviddaily, 'location','new_cases','casedate')

caf.adjmeans(coviddaily, 'location','new_cases','casedate', 150)

#[5]
# verifying the merge operation

caf.checkmerge(countries.copy(), locations.copy(),"countryid", "countryid")

#[6]
#
landtemps = ca.add_files("data/ltcountry")
landtemps.country.value_counts()
