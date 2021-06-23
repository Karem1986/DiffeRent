import pandas as pd
import numpy as np
data = pd.read_csv('pararius_scraped.csv')
df = pd.DataFrame(data, columns = ['Address', 'Postcode', 'Size in m²', 'Rooms', 'Prize in €'])

df['Address'] = df['Address'].str.split(n=1).str[1]
df = df.replace('\n','', regex=True)
df = df.replace('\r','', regex=True)
df = df.replace('new','', regex=True)
df = df.replace(',','', regex=True)
df = df.replace('€','', regex=True)
df = df.replace('rdij ','NaN', regex=True)
df = df.replace(' floo','NaN', regex=True)

print(df.head(10))

df['Prize in €'] = df['Prize in €'].astype(float)
df['Size in m²'] = df['Size in m²'].astype(float)
df['Price/Sqm'] = df['Prize in €'] / df['Size in m²']
print(df.head(10))

df.to_csv("pararius_scraped.csv", index=False)
