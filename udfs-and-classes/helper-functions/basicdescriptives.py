import pandas as pd

#[1]
# this function is designed to get basic information on a data set
#the df parameter takes a dataframe, the nrows takes a number of rows for the head function
# uniqueids takes a column from the data that is believed to a candidate key for the data to return the number of unique values
def get_first_look(df,nrows=5, uniqueids=None):
    out = {}
    out['head'] = df.head(nrows)
    out['dtypes'] = df.dtypes
    out['nrows'] = df.shape[0]
    out['ncols'] = df.shape[1]
    out['index'] = df.index
    if (uniqueids is not None):
        out['uniqueids'] = df[uniqueids].nunique()
    return out

#[]
# this function goes in hand with get_first_look to separate each key-value with 2 spaces

def display_dict(dicttodisplay):
  print(*(': '.join(map(str, x)) for x in dicttodisplay.items()), sep='\n\n')

#[]
# this function gets statistics on continuous variables in the dataframe

def get_tots(df):
    out = {}
    out['min'] = df.min()
    out['per15'] = df.quantile(0.15)
    out['qr1'] = df.quantile(0.25)
    out['med'] = df.median()
    out['qr3'] = df.quantile(0.75)
    out['per85'] = df.quantile(0.85)
    out['max'] = df.max()
    out['count'] = df.count()
    out['mean'] = df.mean()
    out['iqr'] = out['qr3']-out['qr1']
    return pd.DataFrame(out)

#[]
# this function shows the missing values for each column and also the frequency
# of missing values by row with the option to choose between absolute and relative frequencies

def get_missings(df, vc_normalize=False):
  return df.isnull().sum(), df.isnull().sum(axis=1).value_counts(normalize=vc_normalize).sort_index()

#[]
# this function creates a file from the output of a print function that includes
# absolute and relative frequencies for categorical values
def make_freqs(df, outfile):
  freqout = open(outfile, 'w')
  for col in df.select_dtypes(include=["category"]):
    print(col, "----------------------", "frequencies",
    df[col].value_counts().sort_index(),"percentages",
    df[col].value_counts(normalize=True).sort_index(),
    sep="\n\n", end="\n\n\n", file=freqout)

  freqout.close()

#[]
# this functions takes a group of columns and then a subset of that group and returns
# a merged dataframe of the absolute frequencies for each with the option to specify a particular value
# in one of the column through boolean indexing

def get_cnts(df, cats, rowsel=None):
  tots = cats[:-1]
  catcnt = df.groupby(cats).size().reset_index(name='catcnt')
  totcnt = df.groupby(tots).size().reset_index(name='totcnt')
  percs = pd.merge(catcnt, totcnt, left_on=tots,
    right_on=tots, how="left")
  percs['percent'] = percs.catcnt / percs.totcnt
  if (rowsel is not None):
    percs = percs.loc[eval("percs." + rowsel)]
  return percs
