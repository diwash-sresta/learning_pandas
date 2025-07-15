# pd.merge(df1,df2, on='column_name',how = 'type of join')
import pandas as pd;

df_customers = pd.DataFrame({
  'CustomerID' : [1,2,3,4,5],
  'Name':['Ram','Shyam','Hari','Rani','Gita']
})

df_orders = pd.DataFrame({
  'CustomerID' : [1,2,5],
  'Order_Amount' : [250,300,1000]
})

#Merging
# df_merged = pd.merge(df_customers,df_orders, on='CustomerID', how="inner") #inner merge
# df_merged = pd.merge(df_customers,df_orders, on='CustomerID', how="outer") #outer merge
# df_merged = pd.merge(df_customers,df_orders, on='CustomerID', how="left") #left join merge
# df_merged = pd.merge(df_customers,df_orders, on='CustomerID', how="right") #right join merge
df_merged = pd.merge(df_customers,df_orders,  how="cross") #cross join merge
print(df_merged)