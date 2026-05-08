import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/Tojizeni/students-data/main/student.csv")

print(df)

print(df.columns)

print(df.info())