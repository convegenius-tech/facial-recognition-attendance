import pandas as pd
import csv

df = pd.read_csv(r"data23.csv", header=None)


print(df)
df.to_csv(r"test1.csv", header = ['id', 'Roll', 'Name', 'Dept', 'Time', 'Date', 'Status'], index=False) 


finaldata = pd.read_csv(r"test1.csv")

print("Number of lines present:-", len(finaldata))

