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
