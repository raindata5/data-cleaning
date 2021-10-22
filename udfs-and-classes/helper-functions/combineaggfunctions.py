import pandas as pd
import numpy as np
import os



#[]
# taking agg. calc. on variables in dataset with the potential to exclude outliers
def adjmeans(df, byvar, var, period, changeexclude=None, excludetype=None):
  df = df.sort_values([byvar, period]) #sorting by the entity and the frequency in the data of the values
  df = df.dropna(subset=[var]) #removing any null values for the aggregation variable

  # iterate using numpy arrays
  prevbyvar = 'ZZZ'
  prevvarvalue = 0
  rowlist = []
  varvalues = df[[byvar, var]].values

  # convert exclusion ratio to absolute number
  if (excludetype=="ratio" and changeexclude is not None):
    changeexclude = df[var].mean()*changeexclude

  # loop through variable values
  for j in range(len(varvalues)):
    byvar = varvalues[j][0] # entity
    varvalue = varvalues[j][1] # the var to be agg.
    if (prevbyvar!=byvar): # when entities change
      if (prevbyvar!='ZZZ'): # accounting for the firest iteration where prevbyvar is still 'ZZZ'
        rowlist.append({'byvar':prevbyvar, 'avgvar':varsum/byvarcnt,\
          'sumvar':varsum, 'byvarcnt':byvarcnt})
        #initalzing and setting variables
      varsum = 0
      byvarcnt = 0
      prevbyvar = byvar

    # 3 options can be flagged is true : we dont specifiy a definition for outliers, the change between two values is above our
    # definition for outliers, or we are on the first iteration of the entity
    if ((changeexclude is None) or (0 <= abs(varvalue-prevvarvalue) <= changeexclude) or (byvarcnt==0)):
      varsum += varvalue # total of the agg. var
      byvarcnt += 1 # number of observations for the entity

    prevvarvalue = varvalue # resetting variable
  # appending the data for the last entity
  rowlist.append({'byvar':prevbyvar, 'avgvar':varsum/byvarcnt, \
    'sumvar':varsum, 'byvarcnt':byvarcnt})
  return pd.DataFrame(rowlist)


#[]
# confirming if the merge can possibly eclude some vlaues due to missing key values
def checkmerge(dfleft, dfright, mergebyleft, mergebyright):
  dfleft['inleft'] = "Y"
  dfright['inright'] = "Y"
  dfboth = pd.merge(dfleft[[mergebyleft,'inleft']],\
    dfright[[mergebyright,'inright']], left_on=[mergebyleft],\
    right_on=[mergebyright], how="outer")
  dfboth.fillna('N', inplace=True)
  print(pd.crosstab(dfboth.inleft, dfboth.inright))
  print(dfboth.loc[(dfboth.inleft=='N') | (dfboth.inright=='N')].head(20))


#[]
#

def add_files(directory):
  dfout = pd.DataFrame()
  columnsmatched = True

  # loop through the files
  for filename in os.listdir(directory):
    if filename.endswith(".csv"):
      fileloc = os.path.join(directory, filename)

    # open the next file
    with open(fileloc) as f:
      dfnew = pd.read_csv(fileloc)
      print(filename + " has " + str(dfnew.shape[0]) + " rows.")
      dfout = pd.concat([dfout, dfnew])

    # check if current file has any different columns
      columndiff = dfout.columns.symmetric_difference(dfnew.columns)
    if (not columndiff.empty):
      print("", "Different column names for:", filename,\
      columndiff, "", sep="\n")
      columnsmatched = False
  print("Columns Matched:", columnsmatched)
  return dfout
