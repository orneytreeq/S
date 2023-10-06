import pandas as pd
df = pd.read_csv('bdf92d44747096a5.csv')
df.fillna(0, inplace=True)
df.loc[:, df.nunique() > 1] 
df.to_csv('new2.csv', index=False)