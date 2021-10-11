import pandas as pd
from sklearn.impute import KNNImputer

pd.options.display.float_format = '{:,.1f}'.format
nls97 = pd.read_csv("data/nls97c.csv")
nls97.set_index("personid", inplace=True)

#[1]
# isolating the int variables for which we want to impute values

schoolrecordlist = ['satverbal','satmath','gpaoverall','gpaenglish',
  'gpamath','gpascience','highestgradecompleted']

school_record = nls97.loc[:,schoolrecordlist]

#[2]
# initializing the KNNImputer and then transforming the nulls using KNN

imp_KNN = KNNImputer(n_neighbors=5)
new_values = imp_KNN.fit_transform(school_record)

school_record_imp = pd.DataFrame(new_values, columns=schoolrecordlist, index= school_record.index)


#[3]
# inspecting the new values
school_record.head().T

school_record_imp.head().T

#[4]
# comparing the values based on aggregation methods

school_record.loc[:,['gpaoverall','highestgradecompleted']].agg(['mean','count'])

school_record_imp.loc[:,['gpaoverall','highestgradecompleted']].agg(['mean','count'])

# in this case the KNNImputer may not be the best option for values that are missing significant amounts of nulls
# so best to remove some of them maybe those with 4 or more missing values
