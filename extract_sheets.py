import pandas as pd
df_n = pd.read_excel('file.xlsx', sheet_name=0) #extract sheet 1
df_n1 = pd.read_excel('file.xlsx', sheet_name=0, usecols="B") #extract column B from sheet 1
df_email= pd.read_excel('file', sheet_name=1) #extract sheet 2
print(df_n)
print(df_n1)
print(df_email)
