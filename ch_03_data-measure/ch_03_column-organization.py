import pandas as pd
import numpy as np
pd.set_option('display.width', 100)
pd.set_option('display.max_columns', 20)
pd.set_option('display.max_rows', 15)
pd.options.display.float_format = '{:,.0f}'.format

#[]
#reading in the data as well as changing the columns with an object dtype to category to save memory
nls97 = pd.read_csv("data/nls97.csv")
nls97.set_index('personid',inplace=True)

nls97.loc[:,nls97.dtypes=='object'] = nls97.select_dtypes(['object']).apply(lambda x:x.astype('category'))

#[]
#verifying the different effects of slicing on dataframes
# ganalysis = nls97['gender']
# type(ganalysis)

# ganalysis = nls97[['gender']]
# type(ganalysis)

# ganalysis = nls97.loc[:,['gender']]
# type(ganalysis)

# ganalysis = nls97.iloc[:,[0]]
# type(ganalysis)

#[]
# These show the same 2 slices each in a different way
ganalysis = nls97[['gender','maritalstatus',
 'highestgradecompleted']]
ganalysis.shape
ganalysis.head()

ganalysis = nls97.loc[:,['gender','maritalstatus',
 'highestgradecompleted']]
ganalysis.shape
ganalysis.head()

#[]
# using a pre-made list to slice the DF
keyvars = ['gender','maritalstatus',
 'highestgradecompleted','wageincome',
 'gpaoverall','weeksworked17','colenroct17']
analysiskeys = nls97[keyvars]
analysiskeys.info()


#[]
# using fuzzy matching to search for a set of columns
cfilter = nls97.filter(like='weeksworked')
cfilter.info()

#[]
# select columns by data type
canalysis = nls97.select_dtypes(include='category')
canalysis.info()

nanalysis = nls97.select_dtypes(include='number')
nanalysis.info()

#[]
#creating lists of columns to group the columns by relation
demo = ['gender','birthmonth','birthyear']
highschoolrecord = ['satverbal','satmath','gpaoverall',
 'gpaenglish','gpamath','gpascience']
govresp = ['govprovidejobs','govpricecontrols',
  'govhealthcare','govelderliving','govindhelp',
  'govunemp','govincomediff','govcollegefinance',
  'govdecenthousing','govprotectenvironment']
demoadult = ['highestgradecompleted','maritalstatus',
  'childathome','childnotathome','wageincome',
  'weeklyhrscomputer','weeklyhrstv','nightlyhrssleep',
  'highestdegree']
weeksworked = ['weeksworked00','weeksworked01',
  'weeksworked02','weeksworked03','weeksworked04',
  'weeksworked05','weeksworked06',  'weeksworked07',
  'weeksworked08','weeksworked09','weeksworked10',
  'weeksworked11','weeksworked12','weeksworked13',
  'weeksworked14','weeksworked15','weeksworked16',
  'weeksworked17']
colenr = ['colenrfeb97','colenroct97','colenrfeb98',
  'colenroct98','colenrfeb99',  'colenroct99',
  'colenrfeb00','colenroct00','colenrfeb01',
  'colenroct01','colenrfeb02','colenroct02',
  'colenrfeb03','colenroct03','colenrfeb04',
  'colenroct04','colenrfeb05','colenroct05',
  'colenrfeb06','colenroct06','colenrfeb07',
  'colenroct07','colenrfeb08','colenroct08',
  'colenrfeb09','colenroct09','colenrfeb10',
  'colenroct10','colenrfeb11','colenroct11',
  'colenrfeb12','colenroct12','colenrfeb13',
  'colenroct13',  'colenrfeb14','colenroct14',
  'colenrfeb15','colenroct15','colenrfeb16',
  'colenroct16','colenrfeb17','colenroct17']

nls97[demoadult + demo + highschoolrecord + govresp + weeksworked + colenr]
nls97.dtypes

#[]
#using regex to search for a set of columns and also select_dtypes to exclude them
nls97.select_dtypes(exclude=['category']).info()
nls97.filter(regex='income') #using filter w/ like would have gotten the same result but regex would have more functionality
