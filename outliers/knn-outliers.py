import pandas as pd
from pyod.models.knn import KNN
from sklearn.preprocessing import StandardScaler

pd.set_option('display.width', 80)
pd.set_option('display.max_columns', 7)
pd.set_option('display.max_rows', 20)
pd.options.display.float_format = '{:,.2f}'.format
covidtotals = pd.read_csv("data/covidtotals.csv")
covidtotals.set_index("iso_code", inplace=True)

#[1]
# initializing the scaler to use in the KNN model
standardizer = StandardScaler()
analysisvars = ['location','total_cases_pm','total_deaths_pm',\
  'pop_density','median_age','gdp_per_capita']

covidanalysis = covidtotals.loc[:, analysisvars].dropna()

covidanalysis_stand = standardizer.fit_transform(covidanalysis.iloc[:,1:]) #getting the z-scores

#[2]
# running the KNN model and getting the labels which show whether it is an outlier and also the scores that it used to make the decision
clf_name = 'KNN'
clf = KNN(contamination=0.1)
clf.fit(covidanalysis_stand)

y_pred = clf.labels_
y_scores = clf.decision_scores_

#[3]
# placing the attributes in the dataframe with the same index as the orig. dataset so as to facilitate indexing
pred = pd.DataFrame(zip(y_pred,y_scores),columns=['outliers','scores'],index=covidanalysis.index)

pred.sample(10,random_state=1) #outliers = 0

#[4]
# checking frequencies and also running agg. stats
pred.outliers.value_counts()
pred.groupby(['outliers'])[['scores']].agg(['min','median','max'])

#[5]
#joining data to the orig. df to check the stats for the outliers

covidanalysis.join(pred).loc[pred.outliers==1,['location','total_cases_pm','total_deaths_pm','scores']].sort_values(['scores'], ascending=False)
