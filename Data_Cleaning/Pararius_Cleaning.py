import pandas as pd
data = pd.read_csv('pararius_scraped.csv')
df = pd.DataFrame(
    data, columns=['Address', 'Postcode', 'Size', 'Rooms', 'Prize'])
print(df.head())
# Data cleaning-karem:
# 1: #First remove euro sign, comma and the text in PRIZE
#example: data['columnName'] = data['columnName'].map(lambda x: x.lstrip('+-').rstrip('aAbBcC'))
# df['Prize'] = df ['Prize'].map(lambda x: x.lstrip('€').rstrip('per month'))--DONT WORK.

df['Prize'].str.replace(r'\€', '')  # removes any symbols including commas
df['Prize'].str.replace(r'\D', '')  # removes any letters

# 2.#Convert price to a float
# df ['Prize'] = pd.to_numeric(df['Prize'], errors='coerce')
# df = df.replace(np.nan, 0, regex=True)
df['Prize'].astype(str).astype(float)
print(df)
df.dtypes
