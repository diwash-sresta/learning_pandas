# pd.concat([df1,df2], axis = 0 , ignore_index = True)

import pandas as pd;

df_region1 = pd.DataFrame({
  'Customers_ID': [1,2],
  'Name' : ['Raju','Kaju']
})

df_region2 =pd.DataFrame ({
  'Customers_ID': [3,4],
  'Name' : ['Rani','Kali']
})

df_concate = pd.concat([df_region1,df_region2], axis=0, ignore_index=True)
print(df_concate)

df_concate = pd.concat([df_region1,df_region2], axis=1, ignore_index=True)
print(df_concate)#horizontal concat