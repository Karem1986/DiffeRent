import pandas as pd
import numpy as np

data = pd.read_csv('pararius_scraped.csv')
df = pd.DataFrame(data, columns = ['Address', 'Postcode', 'Size in m²', 'Rooms', 'Prize in €', 'Price/Sqm', 'Latitude', 'Longitude', 'Status'])

df.dropna(inplace=True)

df['Latitude']= df['Latitude'].str.replace('.','', regex=True)
df['Longitude']= df['Longitude'].str.replace('.','', regex=True)
df['Latitude']= df['Latitude'].str.replace('522','52.2', regex=True)
df['Latitude']= df['Latitude'].str.replace('523','52.3', regex=True)
df['Latitude']= df['Latitude'].str.replace('524','52.4', regex=True)
df['Longitude']= df['Longitude'].str.replace('48','4.8', regex=True)
df['Longitude']= df['Longitude'].str.replace('49','4.9', regex=True)
df['Longitude']= df['Longitude'].str.replace('47','4.7', regex=True)


df['Latitude'] = df['Latitude'].apply(pd.to_numeric, errors='coerce')
df['Longitude'] = df['Longitude'].apply(pd.to_numeric, errors='coerce')

df.dropna(inplace=True)
df.drop(columns=['Status'], inplace = True)

print(df.head(10))
print(df.info())

df.to_csv("pararius_scraped.csv")