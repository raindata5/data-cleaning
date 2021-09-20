import pandas as pd
from pyod.models.knn import KNN
from sklearn.preprocessing import StandardScaler

pd.set_option('display.width', 80)
pd.set_option('display.max_columns', 7)
pd.set_option('display.max_rows', 20)
pd.options.display.float_format = '{:,.2f}'.format
covidtotals = pd.read_csv("data/covidtotals.csv")
covidtotals.set_index("iso_code", inplace=True)

#[]
#
standardizer = StandardScaler()
analysisvars = ['location','total_cases_pm','total_deaths_pm',\
  'pop_density','median_age','gdp_per_capita']

covidanalysis = covidtotals.loc[:, analysisvars].dropna()

covidanalysis_stand = standardizer.fit_transform(covidanalysis.iloc[:,1:]) #getting the z-scores

#[]
#
clf_name = 'KNN'
clf = KNN(contamination=0.1)
clf.fit(covidanalysis_stand)

y_pred = clf.labels_
y_scores = clf.decision_scores_

#[]
#
pred = pd.DataFrame(zip(y_pred,y_scores),columns=['outliers','scores'],index=covidanalysis.index)

pred.sample(10,random_state=1) #outliers = 0

pred.outliers.value_counts()
pred.groupby(['outliers'])[['scores']].agg(['min','median','max'])

#[]
#

covidanalysis.join(pred).loc[pred.outliers==1,['location','total_cases_pm','total_deaths_pm','scores']].sort_values(['scores'], ascending=False)
