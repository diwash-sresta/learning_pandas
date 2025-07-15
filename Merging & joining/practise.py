import pandas as pd;

df_customers = pd.DataFrame({
  'CustomerID' : [1,2,3,4,5],
  'Name':['Ram','Shyam','Hari','Rani','Gita']
})

df_orders = pd.DataFrame({
  'CustomerID' : [1,2,5],
  'Order_Amount' : [250,300,1000]
})

df_merged_inner = pd.merge(df_customers,df_orders, on='CustomerID', how="inner")

df_merged_outer = pd.merge(df_customers,df_orders, on='CustomerID', how="outer")
print(df_merged_outer)


df_concat = pd.concat([df_merged_inner,df_merged_outer], axis=0, ignore_index=True)
print(df_concat)
