import pandas as pd;

data = {
  "Name": ['Ram','Shyam','Hari'],
  "Age" : ['23','24','26'],
  "City" :['Hetauda','Janakpur','Birgunj']

}

df = pd.DataFrame(data)
print(df)

df.to_csv("output.csv",index=False)# saves dataframe to csv file, index = False removes index column 
df.to_excel("output.xlsx",index=False)# saves dataframe to excel file, index = False removes index column 
df.to_json("output.json",index=False)# saves dataframe to json file, index = False removes index column 