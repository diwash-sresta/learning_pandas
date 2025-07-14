'''
info() method:

1-number of rows and columns
2-column names
3-data types of columns(dtype:obkect,int64,float)
4-non null values
5-memory usage
'''
import pandas as pd;

df = pd.read_json("sample_Data.json")
print(f"Display DataFrame info:\n{df.info()}")