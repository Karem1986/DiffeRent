import pandas as pd
import numpy as np

data = pd.read_csv('Geocodes.csv')

df = pd.DataFrame(data)
#print(df.head(10))
#print(df.info())


orig_data = pd.read_csv('pararius_scraped.csv')
orig_df = pd.DataFrame(orig_data, columns = ['Address', 'Postcode', 'Size in m²', 'Rooms', 'Prize in €', 'Price/Sqm', 'Latitude', 'Longitude', 'Status'])
orig_df.drop(columns=['Latitude', 'Longitude'], inplace = True)

orig_df['Latitude'] = df[' Latitude']
orig_df['Longitude'] = df[' Longitude']
orig_df['Status'] = df[' Status']
orig_df['City'] = df[' City']
orig_df['Country'] = df[' Country']
print(orig_df.info())
print(orig_df.head(10))

print(orig_df['City'].unique())
print(orig_df['Country'].unique())

orig_df = orig_df.replace({'City' : {'Netherlands' : 'NaN', 
     'NieuwAmsterdam' : 'NaN', 
     'Netherlands' : 'NaN', 
     '1057JB' : 'NaN', 
     '1075CV' : 'NaN', 
     '38.185.311' : 'NaN',
     '5.706.689' : 'NaN',
     'Terneuzen' : 'NaN',
     '23.798.532' : 'NaN',
     'Huizen' : 'NaN',
     'Rotterdam' : 'NaN',
     'BerkelenRodenrys' : 'NaN',
     'Breda' : 'NaN',
     'Alfen' : 'NaN',
     '1066SC' : 'NaN',
     'Posterholt' : 'NaN',
     'Leeuwarden' : 'NaN',
     '36.382.192' : 'NaN',
     'Muiden' : 'NaN',
     '1012CA' : 'NaN',
     'Tilburg' : 'NaN',
     '3.613.793' : 'NaN',
     'Almere' : 'NaN',
     '33.528.049' : 'NaN',
     '1105AW' : 'NaN',
     'Arnhem' : 'NaN',
     'Voorburg' : 'NaN',
     '1019VM' : 'NaN',
     'Roden' : 'NaN',
     'Meppel' : 'NaN'}}, regex=True)

orig_df = orig_df.replace({'Country' : {'5.237.243' : 'NaN', 
     '5.176.019' : 'NaN',
     'Amsterdam' : 'NaN',
     '72.571.946' : 'NaN',
     '25.458.464' : 'NaN',
     '120.955.426' : 'NaN',
     '53.446.688' : 'NaN',
     '128.123.986' : 'NaN',
     '52.295.031' : 'NaN',
     '138.441.899' : 'NaN',
     '64.168.459' : 'NaN'}}, regex=True)

df = df.replace({' City' : {'Netherlands' : 'NaN', 
     'NieuwAmsterdam' : 'NaN', 
     'Netherlands' : 'NaN', 
     '1057JB' : 'NaN', 
     '1075CV' : 'NaN', 
     '38.185.311' : 'NaN',
     '5.706.689' : 'NaN',
     'Terneuzen' : 'NaN',
     '23.798.532' : 'NaN',
     'Huizen' : 'NaN',
     'Rotterdam' : 'NaN',
     'BerkelenRodenrys' : 'NaN',
     'Breda' : 'NaN',
     'Alfen' : 'NaN',
     '1066SC' : 'NaN',
     'Posterholt' : 'NaN',
     'Leeuwarden' : 'NaN',
     '36.382.192' : 'NaN',
     'Muiden' : 'NaN',
     '1012CA' : 'NaN',
     'Tilburg' : 'NaN',
     '3.613.793' : 'NaN',
     'Almere' : 'NaN',
     '33.528.049' : 'NaN',
     '1105AW' : 'NaN',
     'Arnhem' : 'NaN',
     'Voorburg' : 'NaN',
     '1019VM' : 'NaN',
     'Roden' : 'NaN',
     'Meppel' : 'NaN'}}, regex=True)

df = df.replace({' Country' : {'5.237.243' : 'NaN', 
     '5.176.019' : 'NaN',
     'Amsterdam' : 'NaN',
     '72.571.946' : 'NaN',
     '25.458.464' : 'NaN',
     '120.955.426' : 'NaN',
     '53.446.688' : 'NaN',
     '128.123.986' : 'NaN',
     '52.295.031' : 'NaN',
     '138.441.899' : 'NaN',
     '64.168.459' : 'NaN'}}, regex=True)

orig_df = orig_df[orig_df['City'] != 'NaN']
orig_df = orig_df[orig_df['Country'] != 'NaN']
orig_df.drop(columns=['City', 'Country'], inplace = True)

df = df[df[' City'] != 'NaN']
df = df[df[' Country'] != 'NaN']
print(df.info())

#df.to_csv("Geocodes.csv")
#orig_df.to_csv("pararius_scraped.csv")

