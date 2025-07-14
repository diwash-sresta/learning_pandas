import pandas as pd;

df = pd.read_json("sample_Data.json")
print(f"Display first 10 rows :\n {df.head(10)}")
print(f"Display last 10 rows :\n {df.tail(10)}")