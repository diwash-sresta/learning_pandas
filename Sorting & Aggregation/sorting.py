#df.sort_values(by='Column_name',ascending=True/False,inplace = true) True-ascending , False-descending

import pandas as pd;

data = {
  "Name":['Ram','Shyam','Hari','Rani','Gita','Sita','Kiran','Anita'],
  "Age": [23,24,26,22,25,27,28,29],
  "Salary":[80000,20000,30000,40000,50000,60000,70000,10000]
}

df= pd.DataFrame(data)
# df.sort_values(by="Age",ascending=True,inplace=True) #Sorting by single column
df.sort_values(by=["Age","Salary"],ascending=[False, True],inplace=True)
print(df)