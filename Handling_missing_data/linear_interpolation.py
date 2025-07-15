'''
When to use interpolation:
- time series data
-numeric data with a trend
-avoid dropping rows/cols
-cannot use for categorical data
'''

import pandas as pd;

data = {
  "ID" : [1,2,3,4,5,],
  "Value" : [10,None,20,None,50],
}

df = pd.DataFrame(data)
print(f"Before interpolation:\n{df}")
print(df)

df['Value'] = df['Value'].interpolate(method = 'linear')
print(f"After interpolation:\n{df}")