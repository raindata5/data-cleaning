
#[]
#
import pandas as pd
cmacitations = pd.read_csv("data/cmacitations.csv")
cmacreators = pd.read_csv("data/cmacreators.csv")

#[]
#
cmacitations.head(10)
cmacitations.shape
cmacitations.id.nunique()

#[]
#
cmacreators.loc[:,['id','creator','birth_year']].head(10)
cmacreators.shape
cmacreators.id.nunique()

#[]
#
cmacitations.id.value_counts()

#[]
#
cmacreators.id.value_counts()

#[]
#

def checkmerge(dfleft, dfright, idvar):
    dfleft['inleft'] = "Y"
    dfright['inright'] = "Y"
    dfboth = pd.merge(dfleft[[idvar,'inleft']],\
    dfright[[idvar,'inright']], on=[idvar], how="outer")
    dfboth.fillna('N', inplace=True)
    print(pd.crosstab(dfboth.inleft, dfboth.inright))
    print(dfboth.loc[(dfboth.inleft=='N') | (dfboth.inright=='N')])

checkmerge(cmacitations.copy(), cmacreators.copy(), "id")

#[]
#
cmacitations.loc[cmacitations.id==124733]
cmacreators.loc[cmacreators.id==124733, ['id','creator','birth_year','title']]

#[]
#
cma = pd.merge(cmacitations, cmacreators, on=['id'], how="outer")
cma['citation'] = cma.citation.str[0:20]
cma['creator'] = cma.creator.str[0:20]
cma.loc[cma.id==124733, ['citation','creator','birth_year']]
