import pandas as pd
import numpy as np
from geopy.geocoders import Nominatim
import time
from pprint import pprint

data = pd.read_csv('pararius_scraped.csv')
df = pd.DataFrame(data, columns = ['Address', 'Postcode', 'Size in m²', 'Rooms', 'Prize in €', 'Price/Sqm', 'Latitude', 'Longitude'])
df['address_for_geo'] = df['Address']+ ', ' + df['Postcode'] + ', Amsterdam, Netherlands'

app = Nominatim(user_agent="tutorial")

def get_location_by_address(address):
    time.sleep(1)
    try:
        return app.geocode(address).raw
    except:
        return 'NaN'

Latitude = list()
Longitude = list()

addresses = df['address_for_geo']
for address in addresses:
    location = get_location_by_address(address)
    if location == 'NaN':
        Latitude.append('NaN')
        Longitude.append('NaN')
    else:
        lati = location["lat"]
        Latitude.append(lati)
        longi = location["lon"]
        Longitude.append(longi)

df['Latitude'] = Latitude 
df['Longitude'] = Longitude
df.drop(columns=['address_for_geo'], inplace = True)
print(df.head(10))

#df.to_csv("pararius_scraped.csv", index=False)
