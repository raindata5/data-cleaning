#[1]
#

import pandas as pd
import os
import sys
import pprint
nls97 = pd.read_csv("data/nls97f.csv")
nls97.set_index('personid', inplace=True)
covidtotals = pd.read_csv("data/covidtotals720.csv")

#[2]
# exploring the distribution of the data

sys.path.append(os.getcwd() + "/helper-functions")
import outliers as ol

distribution = ol.get_dist_props(covidtotals.total_cases_pm)

pprint.pprint(distribution)

#[3]
import importlib
importlib.reload(ol)

#[4]
# getting information on outliers in certain columns
sumvars = ['satmath','wageincome']
othervars = ['originalid','highestdegree','gender','maritalstatus']
outliers = ol.get_outliers(nls97, sumvars, othervars)
outliers.varname.value_counts(sort=False) # number of outliers in each column

outliers.originalid.value_counts()
outliers.loc[outliers.originalid == 535]

#[5]
# moving the outliers to an excel sheet
outliers.to_excel("views/nlsoutliers.xlsx")

#[6]
# plotting distribution
ol.makeplot(nls97.satmath, "Histogram: SAT Math", "SAT Math")
ol.makeplot(nls97.satmath, "Boxplot: SAT Math", "SAT Math", "box")
