import pandas as pd
import numpy as np
import pymssql
import mysql.connector

# write the query for the db and alias the some columns
query = "SELECT studentid, school, sex, age, famsize,\
medu AS mothereducation, fedu AS fathereducation,traveltime, studytime, failures, \
famrel, freetime,goout, g1 AS gradeperiod1, g2 AS gradeperiod2,\
g3 AS gradeperiod3 From studentmath"


# place the access information ... in practice this would be placed in a different file where we could use configparser to access it
# rather than hard coded
server = "pdcc.c9sqqzd5fulv.us-west-2.rds.amazonaws.com"
user = "pdccuser"
password = "pdccpass"
database = "pdcctest"

conn = pymssql.connect(server=server,
  user=user, password=password, database=database)

#sending the query to the db
studentmath = pd.read_sql(query,conn)
#closing the connection to return it to the pool on the server
conn.close()

#[]
#inspecting the dataframe
studentmath.info()
studentmath.describe()

# now will use the my sql connector with a more less identical process
host = "pdccmysql.c9sqqzd5fulv.us-west-2.rds.amazonaws.com"
user = "pdccuser"
password = "pdccpass"
database = "pdccschema"
connmysql = mysql.connector.connect(host=host,
  database=database,user=user,password=password)
studentmath2 = pd.read_sql(query,connmysql)
connmysql.close()

studentmath2.info()
studentmath2.describe()

# will first rearrange the columns and set studentid as the index
newcolorder = ['studentid', 'gradeperiod1', 'gradeperiod2',
  'gradeperiod3', 'school', 'sex', 'age', 'famsize',
  'mothereducation', 'fathereducation', 'traveltime',
  'studytime', 'freetime', 'failures', 'famrel',
  'goout']
studentmath = studentmath[newcolorder]
studentmath.info()
studentmath.studentid.count()
studentmath.studentid.nunique()
studentmath.set_index('studentid',inplace=True)

#counting for missing values
studentmath.count()

# going to replace these abstract values with more informative ones

setvalues={"famrel":{1:"1:very bad",2:"2:bad",3:"3:neutral",
    4:"4:good",5:"5:excellent"},
  "freetime":{1:"1:very low",2:"2:low",3:"3:neutral",
    4:"4:high",5:"5:very high"},
  "goout":{1:"1:very low",2:"2:low",3:"3:neutral",
    4:"4:high",5:"5:very high"},
  "mothereducation":{0:np.nan,1:"1:k-4",2:"2:5-9",
    3:"3:secondary ed",4:"4:higher ed"},
  "fathereducation":{0:np.nan,1:"1:k-4",2:"2:5-9",
    3:"3:secondary ed",4:"4:higher ed"}}

studentmath.replace(setvalues,inplace=True)

setvalueskeys = [x for x in setvalues]
# setvalueskeys = setvalues.keys

#[]

# will change type to category for the modified columns

studentmath[setvalueskeys].memory_usage(index=False)

for col in setvalueskeys :
    studentmath[col] = studentmath[col].astype('category')

studentmath[setvalueskeys].memory_usage(index=False)

#[]
# percentages
studentmath.famrel.value_counts(sort=False , normalize=True)

#[]
#calculating percentages on multiple columns
studentmath[['freetime','goout']].apply(pd.Series.value_counts,sort=False,
    normalize=True)

studentmath[['mothereducation','fathereducation']].apply(pd.Series.value_counts,sort=False,
    normalize=True)
