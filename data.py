import pandas as pd


data = pd.read_csv('data.csv').to_dict(orient='records')
print(data)