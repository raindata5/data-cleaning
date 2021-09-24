import pandas as pd
import numpy as np
import pyreadstat

#[]
# importing data and taking quick view at it
nls97spss, metaspss = pyreadstat.read_sav('data/nls97.sav')

nls97spss.info()

nls97spss.head()

nls97spss['R0536300'].value_counts(normalize=True)

metaspss.variable_value_labels['R0536300']


nls97spss['R0536300'].map(metaspss.variable_value_labels['R0536300']).value_counts(normalize=True)

nls97spss = pyreadstat.set_value_labels(nls97spss,metaspss,formats_as_category=True)

#[]
# now will change columns and place them in a good format ad set index

nls97spss.columns = metaspss.column_labels
nls97spss.columns

nls97spss.columns = nls97spss.columns.str.lower().str.strip().str.replace(' ','_').str.replace('[^a-z0-9_]','')

nls97spss.set_index('pubid__yth_id_code_1997',inplace=True)

#[]
# will instead call set_value_labels from the inital read func
nls97spss, metaspss = pyreadstat.read_sav('data/nls97.sav', apply_value_formats = True,formats_as_category=True)
nls97spss.columns = metaspss.column_labels
nls97spss.columns = nls97spss.columns.str.lower().str.strip().str.replace(' ','_').str.replace('[^a-z0-9_]','')

#[]
nls97spss.dtypes
nls97spss.head()

#[]
#summary stats and setting index
nls97spss.describe()
nls97spss.set_index('pubid__yth_id_code_1997',inplace=True)



#[]
#now will apply a similar method to the stata data
nls97stata , metastata = pyreadstat.read_dta('data/nls97.dta',apply_value_formats=True,formats_as_category=True)

nls97stata.columns = metastata.column_labels

nls97stata.columns = nls97stata.columns.str.lower().str.replace(' ','_').str.replace('[^a-z0-9_]','')
nls97stata.dtypes

#[]
nls97stata.head()
nls97stata['hrsnight_r_sleeps_2017'].value_counts(sort=False)

#[]

nls97stata.min() #quick check for issues -1 to -9 signifies missing values
nls97stata.replace(list(range(-9,0)),np.nan,inplace=True)
nls97stata.min()
nls97stata.set_index('pubid__yth_id_code_1997',inplace=True)




#[]
# finally the SAS data will be loaded in

nls97sas, metasas = pyreadstat.read_sas7bdat('data/nls97.sas7bdat',
    catalog_file = 'data/nlsformats3.sas7bcat',formats_as_category=True)

nls97sas.columns = metasas.column_labels
nls97sas.columns = nls97sas.columns.str.lower().str.replace(' ','_').str.replace('[^a-z0-9_]','')
nls97sas.head()
nls97sas.hrsnight_r_sleeps_2017.value_counts()
nls97sas.info()
nls97sas.set_index('pubid__yth_id_code_1997',inplace=True)
