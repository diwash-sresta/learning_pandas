import pandas as pd;

df = pd.read_csv('Handling_missing_data\weather_data.csv', parse_dates=['day'])
df.set_index('day',inplace=True)


print('After interpolation')

#time interpolation
df.interpolate(method='time',inplace=True)


df['event'] = df['event'].fillna('No Event')
print(df)