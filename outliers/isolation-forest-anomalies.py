import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import IsolationForest
from mpl_toolkits.mplot3d import Axes3D

pd.set_option('display.width', 80)
pd.set_option('display.max_rows', 20)
pd.set_option('display.max_columns', 7)

covidtotals = pd.read_csv("data/covidtotals.csv")
covidtotals.set_index("iso_code", inplace=True)

#[1]
# initializing the scaler to use in the isolation forest model
analysisvars = ['location','total_cases_pm','total_deaths_pm',
  'pop_density','median_age','gdp_per_capita']

standardizer = StandardScaler()
covidtotals.isnull().sum()
covidanalysis = covidtotals.loc[:, analysisvars].dropna()
covidanalysisstand = standardizer.fit_transform(covidanalysis.iloc[:, 1:])

#[2]
#initializing the isolation forest model
clf = IsolationForest(n_estimators=100, max_samples='auto',contamination=.1,max_features=1.0)
clf.fit(covidanalysisstand)

covidanalysis['anomaly'] = clf.predict(covidanalysisstand)
covidanalysis['scores'] = clf.decision_function(covidanalysisstand)

covidanalysis['anomaly'].value_counts() #countries with -1 are identified as outliers

#[3]
#separating the extreme values from the other values

inlier, outlier = covidanalysis.loc[covidanalysis.anomaly==1],covidanalysis.loc[covidanalysis.anomaly==-1]

outlier[['location','total_cases_pm','total_deaths_pm','median_age','gdp_per_capita','scores']].sort_values(['scores']).head(10)

#[4]
# plotting 3 of the variables to check for any patterns in the outliers
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.set_title('Isolation Forest Anomaly Detection')
ax.set_zlabel("Cases Per Million")
ax.set_xlabel("GDP Per Capita")
ax.set_ylabel("Median Age")
ax.scatter3D(inlier.gdp_per_capita, inlier.median_age, inlier.total_cases_pm,label="inliers",c="blue")
ax.scatter3D(outlier.gdp_per_capita, outlier.median_age, outlier.total_cases_pm, label="outliers", c="red")
ax.legend()
plt.tight_layout()
plt.show()
