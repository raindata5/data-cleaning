#[]
#
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as scistat
import math

#[]
# this formula gets stats related to the distribution of the series in the data
# it also includes a hypothesis test for whether the distribution is normal or not
def get_dist_props(seriestotest):
  out = {}
  normstat, normpvalue = scistat.shapiro(seriestotest)
  if (not math.isnan(normstat)):
    out['normstat'] = normstat
    if (normpvalue>=0.05):
      out['normpvalue'] = str(round(normpvalue, 2)) + ":H0 - Accept Normal"
    elif (normpvalue<0.05):
      out['normpvalue'] = str(round(normpvalue, 2)) + ":HA - Reject Normal"
  out['mean'] = seriestotest.mean()
  out['median'] = seriestotest.median()
  out['std'] = seriestotest.std()
  out['kurtosis'] = seriestotest.kurtosis()
  out['skew'] = seriestotest.skew()
  out['count'] = seriestotest.count()
  return out

#[]
# this function find outliers
def get_outliers(dfin,sumvars,othervars):
    dfin = dfin[sumvars + othervars] # getting a dataframe of all the data with the desired columns
    dfout = pd.DataFrame(columns=dfin.columns, data=None) # initlializng a dataframe with all the columns which will be kept in the end
    dfsums = dfin[sumvars] #separating the variables for which we want to explore the outliers
    for col in dfsums.columns:
        thirdq, firstq = dfsums[col].quantile(0.75),dfsums[col].quantile(0.25) #calculating quantiles to get iqr
        interquartilerange = 1.5*(thirdq-firstq) # multiplying by 1.5 to test for outliers
        outlierhigh, outlierlow = interquartilerange+thirdq,firstq-interquartilerange #finding the high outlier threshold and the same for the lower
        df = dfin.loc[(dfin[col]>outlierhigh) | (dfin[col]<outlierlow)] #finding rows that are either high or low extreme values
        df = df.assign(varname = col, threshlow = outlierlow, threshhigh = outlierhigh) # creating 3 columns that display the reason why this row was considered an outlier
        dfout = pd.concat([dfout, df])
    return dfout

#[]
# creating a plot for the distribution
def makeplot(seriestoplot, title, xlabel, plottype="hist"):
    if (plottype=="hist"):
        plt.hist(seriestoplot)
        plt.axvline(seriestoplot.mean(), color='red',linestyle='dashed', linewidth=1)
        plt.xlabel(xlabel)
        plt.ylabel("Frequency")
    elif (plottype=="box"):
        plt.boxplot(seriestoplot.dropna(), labels=[xlabel])
    plt.title(title)
    plt.show()
