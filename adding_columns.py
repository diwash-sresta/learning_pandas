import pandas as pd;

data = {
  "Name": ['Ram','Shyam','Hari','Rani','Gita','Sita','Kiran','Anita'],
  "Age" : [23,24,26,22,25,27,28,29],
  "City" :['Hetauda','Janakpur','Birgunj','Pokhara','Kathmandu','Lalitpur','Bhaktapur','Nepalgunj'],
  "Salary":[50000,60000,55000,52000,58000,62000,53000,54000],
  "Performance Score": [4.5, 3.8, 4.2, 4.0, 3.9, 4.1, 4.3, 4.6]
}

df = pd.DataFrame(data)
print(df)
# using square brackets to add new colummn
df['Bonus'] = df['Salary'] * 0.1
print(df)

# using insert() to add new column
df.insert(0,'Employee ID',[100,101,102,103,104,105,106,107])
print(df)

