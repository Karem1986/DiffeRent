import pandas as pd

data = pd.read_csv('pararius_scraped.csv')
df = pd.DataFrame(data, columns = ['Address', 'Postcode', 'Size', 'Rooms', 'Prize'])
print(df.head())

