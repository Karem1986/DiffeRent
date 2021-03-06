import pandas as pd
import numpy as np
data = pd.read_csv('pararius_scraped.csv')
df = pd.DataFrame(data, columns = ['Address', 'Postcode', 'Size in m²', 'Rooms', 'Prize in €'])
df.head(10)
# Data cleaning:
#Prize into Numerical value: 
df['Prize in €'] = df['Prize in €'].str.replace(',', '') #First we remove the comma's - otherwise our .split() method in the next section will not work properly.
print('-----------Price column values before preprocessing-----------\n')
print(df['Prize in €'].unique())
print('\n\n')
print('-----------Price column values after removing non number values-----------\n')
#Apply a function that splits (converts into list) each string value of the Price column, and then only selects the characters that are numbers, and then join those back together to form a string again.
df['Numerical values'] = df['Prize in €'].apply(lambda x: ''.join(char for char in x.split() if char.isdigit())) #The values of this new column only containt the numbers of the values of the Prize in € column 
print(df['Numerical values'].unique()) #Checking unique values you see that it worked (although there are missing values)
print('\n\n')
print('-----------Price column values after converting column to numeric and labeling missing values-----------\n')
df['Numerical values'] = pd.to_numeric(df['Numerical values'], errors='coerce') #We convert the columns values to numerical values and give the empty values a nan (not a number) value
print(df['Numerical values'].unique())
print('-----------checking the datatype of our new column-----------\n')
print('The datatype is:',df['Numerical values'].dtypes) #It worked :)

#1Handle missing values, convert ? to NaN in the whole data set: 

# replace "?" to NaN
df.replace("?", np.nan, inplace = True)
df.head(5)

#1.1.Check for missing values:
missing_data = df.isnull()
missing_data.head(10) #returns false because we are not missing any values.

# DATA EXPLORATION: 
# Is there a relation between size in m2 and Numerical values?
# groupby to find the average prize of a property based on size in m2
import matplotlib.pyplot as plt

#First we select the columns we are interested in:
df_group_one = df[['Size in m²', 'Numerical values']]
# Second: grouping results based on Size in m2 : Does Size in m2 has an influence on price?
df_Size_m2 = df_group_one.groupby(['Size in m²']).mean()
df_Size_m2 #As you can see above, Size in m2 needs to be also converted to float, as price. 
# Next we could try again to find the average. 
