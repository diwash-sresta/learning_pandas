import pandas as pd;

data = {
  "Name": ['Ram','Shyam','Hari','Rani','Gita','Sita','Kiran','Anita'],
  "Age" : [23,24,26,22,25,27,28,29],
  "City" :['Hetauda','Janakpur','Birgunj','Pokhara','Kathmandu','Lalitpur','Bhaktapur','Nepalgunj'],
  "Salary":[50000,60000,55000,52000,58000,62000,53000,54000],
  "Performance Score": [4.5, 3.8, 4.2, 4.0, 3.9, 4.1, 4.3, 4.6]
}

df = pd.DataFrame(data)
#filtering single condition
high_salary = df[df['Salary'] > 52000]
print(f"Employees with Salary > 52000:\n{high_salary}")

#filtering multiple conditions
high_salary_young = df[(df['Salary']> 55000) & (df['Age'] < 26)]
print(f"\nYoung high salary employees:\n{high_salary_young}")

#filtering using OR condition
veteran_employees = df[( (df['Performance Score']>4.0)) | (df['Age']>25)]
print(f"\nVeteran employees with high performance :\n{veteran_employees}")