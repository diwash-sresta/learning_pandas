#dropna() - to remove the missing values
#fillna() - to fill the missing values with a specific value or method
#Axis = 0 - for rows(default), Axis = 1 - for columns


import pandas as pd;

data = {
  "Name": ['Ram','Shyam','Hari','Rani','Gita','Sita','Kiran','Anita'],
  "Age" : [23,24,26,22,25,27,28,29],
  "City" :['Hetauda','Janakpur',None,'Pokhara','Kathmandu','Lalitpur','Bhaktapur','Nepalgunj'],
  "Salary":[50000,None,55000,52000,58000,62000,53000,54000],
  "Performance Score": [4.5, 3.8, 4.2, 4.0, 3.9, 4.1, 4.3, 4.6]
}

df = pd.DataFrame(data)
print(df)

''' Deleting rows & columns with missing values
df.dropna(inplace=True) # removing rows with missing values
print(df)

df.dropna(axis = 1,inplace=True) # removing columns with missing values
print(df)

'''
# Filling missing values

# df.fillna(0,inplace=True) # filling the missing values with 0
# print(df)
df['City'].fillna('Birgunj',inplace=True) #filling missing values in City col
df['Salary'].fillna(df['Salary'].mean(),inplace=True) # filling missing values in Salary col with mean
print(df)