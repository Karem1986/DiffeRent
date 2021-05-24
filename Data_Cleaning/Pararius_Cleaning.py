import pandas as pd
data = pd.read_csv('pararius_scraped.csv')
df = pd.DataFrame(
    data, columns=['Address', 'Postcode', 'Size', 'Rooms', 'Prize'])
print(df.head())
# Data cleaning:
#Prize into Numerical values: 
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

#Identifiying missing values in the whole data set:
missing_data = df.isnull()
missing_data.head(10) #returns false because we are not missing any values.
