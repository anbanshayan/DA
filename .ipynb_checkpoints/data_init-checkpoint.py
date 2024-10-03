import pandas as pd

url = "/home/anbashayan/Downloads/heart+disease/switzerland.data"

df = pd.read_csv(url, header = None)

print(df.head(5))