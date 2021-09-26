import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns

#[1]
# reading in data and setting respective indexes
pd.set_option('display.width', 80)
pd.set_option('display.max_columns', 12)
pd.set_option('display.max_rows', 200)
pd.options.display.float_format = '{:,.2f}'.format
landtemps = pd.read_csv("data/landtemps2019avgs.csv")

#[2]
# plotting temperature and abs. valuse of the latitude to see correlation

plt.scatter(x="latabs", y="avgtemp", data=landtemps)
plt.xlabel("Latitude (N or S)")
plt.ylabel("Average Temperature (Celsius)")
plt.yticks(np.arange(-60, 40, step=20))
plt.title("Latitude and Average Temperature in 2019")
plt.show()

#[3]
# plotting temperature and abs. valuse of the latitude again to see correlation but this time with high elevations colored red

low, high = landtemps.loc[landtemps.elevation<=1000], landtemps.loc[landtemps.elevation>1000]
plt.scatter(x="latabs", y="avgtemp", c="blue", data=low)
plt.scatter(x="latabs", y="avgtemp", c="red", data=high)
plt.legend(('low elevation', 'high elevation'))
plt.xlabel("Latitude (N or S)")
plt.ylabel("Average Temperature (Celsius)")
plt.title("Latitude and Average Temperature in 2019")
plt.show()

#[4]
# 3d plot to include the values of the elevation

fig = plt.figure()
plt.suptitle("Latitude, Temperature, and Elevation in 2019")

ax = plt.axes(projection='3d')
ax.set_title('Three D')
ax.set_xlabel("Elevation")
ax.set_ylabel("Latitude")
ax.set_zlabel("Avg Temp")
ax.scatter3D(low.elevation, low.latabs, low.avgtemp, label="low elevation", c="blue")
ax.scatter3D(high.elevation, high.latabs, high.avgtemp, label="high elevation", c="red")
ax.legend()
plt.show()

#[5]
# linear regression plot showing the temperatures dropping more as the abs. latitude becomes higher

sns.regplot(x="latabs", y="avgtemp", color="blue", data=landtemps)
plt.title("Latitude and Average Temperature in 2019")
plt.xlabel("Latitude (N or S)")
plt.ylabel("Average Temperature")
plt.show()

#[6]
#

landtemps['elevation_group'] = np.where(landtemps.elevation<=1000, 'low','high')
sns.lmplot(x='latabs',y = 'avgtemp' , hue="elevation_group", palette=dict(low="blue", high="red"), legend_out=False, data=landtemps)
plt.xlabel("Latitude (N or S)")
plt.ylabel("Average Temperature")
plt.legend(('low elevation', 'high elevation'), loc='lower left')
plt.yticks(np.arange(-60, 40, step=20))
plt.title("Latitude and Average Temperature in 2019")
plt.tight_layout()
plt.show()


#[]
# extreme values above the reg line
high.loc[(high.latabs>38) & (high.avgtemp>=18),['station','country','latabs','elevation','avgtemp']]
low.loc[(low.latabs>47) & (low.avgtemp>=14),['station','country','latabs','elevation','avgtemp']]

#[]
# extreme values below the reg line

high.loc[(high.latabs<5) & (high.avgtemp<18),['station','country','latabs','elevation','avgtemp']]
low.loc[(low.latabs<50) & (low.avgtemp<-9),['station','country','latabs','elevation','avgtemp']]
