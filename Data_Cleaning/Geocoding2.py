import pandas as pd
import numpy as np
from geopy.geocoders import Nominatim
import time
from pprint import pprint

data = pd.read_csv('Geocodes.csv')

df = pd.DataFrame(data)
print(df.head(10))
print(df.info())


orig_data = pd.read_csv('pararius_scraped.csv')
orig_df = pd.DataFrame(orig_data, columns = ['Address', 'Postcode', 'Size in m²', 'Rooms', 'Prize in €', 'Price/Sqm', 'Latitude', 'Longitude'])
orig_df.drop(columns=['Latitude', 'Longitude'], inplace = True)

orig_df['Latitude'] = df[' Latitude']
orig_df['Longitude'] = df[' Longitude']
orig_df['Status'] = df[' Status']
print(orig_df.info())
print(orig_df.head(10))

orig_df.to_csv("pararius_scraped.csv")

