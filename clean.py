import pandas as pd
import os

df = pd.read_csv('remote.csv', index_col='Id')
df['AvgBedroomSize'] = df['1stFlrSF'] / df['BedroomAbvGr']
df.to_csv('dataset.csv')
