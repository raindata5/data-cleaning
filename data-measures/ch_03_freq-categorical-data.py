import pandas as pd
pd.set_option('display.width', 75)
pd.set_option('display.max_columns', 10)
pd.set_option('display.max_rows', 20)
pd.options.display.float_format = '{:,.2f}'.format

#[]
#reading in data and looping through the object columns to change them to category data types
nls97 = pd.read_csv("data/nls97.csv")
nls97.set_index("personid", inplace=True)

nls97.loc[:,nls97.dtypes == 'object'] = nls97.select_dtypes(['object']).apply(lambda x: x.astype('category'))


#[]
#checking for the number of missing values in the category columns and getting frequencies on the marital status column
catcols = nls97.select_dtypes(include=['category']).columns
nls97[catcols].isnull().sum()

nls97.maritalstatus.value_counts()
nls97.maritalstatus.value_counts(sort=False)
nls97.maritalstatus.value_counts(sort=False,normalize=True)

#[]
#looking to see if there is some difference when those that are married respond to the questions on government responsibility
nls97.filter(like='gov').apply(pd.value_counts,normalize=True)
nls97.loc[nls97.maritalstatus == 'Married',:].filter(like='gov').apply(pd.value_counts,sort=False,normalize=True)
#however one would have to look at the distributuion of other variables among those that are married because maybe it's age that is providing us with an association
#so this could be a confounding variable

#[]
# saving the frquencies of the data to a file
freqout = open('views/frequencies.txt','w')

for col in nls97.select_dtypes(include=['category']) :
    print(col,'----------',
        'frequencies', nls97[col].value_counts(sort=False),
    'percentages', nls97[col].value_counts(normalize=True,sort=False),
    sep=r'\n\n', end = r'\n\n\n',file=freqout)
freqout.close()
