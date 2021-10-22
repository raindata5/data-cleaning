
#[1]
#
import pandas as pd
cmacitations = pd.read_csv("data/cmacitations.csv")
cmacreators = pd.read_csv("data/cmacreators.csv")

#[2]
# exploring the data with multiple citations for each id
cmacitations.head(10)
cmacitations.shape
cmacitations.id.nunique()

#[3]
# exploring the next dataset that also has duplicate ids
cmacreators.loc[:,['id','creator','birth_year']].head(10)
cmacreators.shape
cmacreators.id.nunique()

#[4]
# seeing the value counts for some of the ids in the data
cmacitations.id.value_counts()

cmacreators.id.value_counts()

#[5]
# using the checkmerge function to help identify the nature of the join

def checkmerge(dfleft, dfright, idvar):
    dfleft['inleft'] = "Y"
    dfright['inright'] = "Y"
    dfboth = pd.merge(dfleft[[idvar,'inleft']],\
    dfright[[idvar,'inright']], on=[idvar], how="outer")
    dfboth.fillna('N', inplace=True)
    print(pd.crosstab(dfboth.inleft, dfboth.inright))
    print(dfboth.loc[(dfboth.inleft=='N') | (dfboth.inright=='N')])

checkmerge(cmacitations.copy(), cmacreators.copy(), "id")

#[6]
# exploring a value with multiple values in one dataset and the other so we can expect 28 values corresponding to thsi id in the final dataset
cmacitations.loc[cmacitations.id==124733]
cmacreators.loc[cmacreators.id==124733, ['id','creator','birth_year','title']]

#[7]
# doing the many to many merge and then taking another look at the value we looked at before
cma = pd.merge(cmacitations, cmacreators, on=['id'], how="outer")
cma['citation'] = cma.citation.str[0:20]
cma['creator'] = cma.creator.str[0:20]
cma.loc[cma.id==124733, ['citation','creator','birth_year']]
