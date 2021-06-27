import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

helix = pd.read_csv('pararius_scraped.csv')
# shape of the dataframe
helix.shape
# Select columns
# selecting a couple of columns:
selected_columns = helix[['Prize in €', 'Price/Sqm', 'Postcode']]
selected_columns.head()

findingAvg = selected_columns.groupby(['Price/Sqm']).mean()

findingAvg.head(10)

# major_ticks = np.arange(0, 200, 20)
# minor_ticks = np.arange(0, 180, 5)

plt.figure(figsize=(6, 5))


s = plt.scatter('Price/Sqm', 'Postcode', c='green',
                data=findingAvg, cmap='Blues_r', marker='s', s=190)

# ax.axis([findingAvg['Price/Sqm'].min()-10, findingAvg['Postcode'].max()+10, findingAvg['Price/Sqm'].min()-10])


plt.ylabel('Price', fontsize=15)
plt.xlabel('s2m')
plt.title('Does the price increase based on Postcode?', size=20)

ax = plt.subplot(1, 1, 1)
cbar = plt.colorbar(mappable=s, ax=ax)


plt.show()
