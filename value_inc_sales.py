import pandas as pd

# Importing the data
data = pd.read_csv('transaction.csv',sep = ';')

# Quick check on Data
data.info()

# Assigning variables to columns for math operations
Costperitem = data['CostPerItem']
SellingPrice = data['SellingPricePerItem']

Numofitemspurchesed = data['NumberOfItemsPurchased']

# Operation
CostPerTransaction= Costperitem * Numofitemspurchesed

# Creating a new column and Exporting into Data
data['CostPerTransaction'] = CostPerTransaction
data['SellingPriceOfTransaction'] = SellingPrice * Numofitemspurchesed

data['Profit'] = data['SellingPriceOfTransaction'] - data['CostPerTransaction']
data['Markup'] = data['Profit'] / data['CostPerTransaction']

# Rounding off to 2 decimal points
data['Markup'] = round(data['Markup'],2)

# Concatenation of 3 columns
data['PurchaseDate'] = data['Day'].astype(str) + '-' + data['Month'].astype(str) + '-' + data['Year'].astype(str)

# Splitting up keywords 
split_keywords= data['ClientKeywords'].str.split(',' , expand= True)


# Alotting those keywords to specific columns
data['ClientAge']= split_keywords[0]
data['ClientField']= split_keywords[1]
data['ClientTenure']= split_keywords[2]

# Removing unwanted text in string
data['ClientAge']= data['ClientAge'].str.replace('[', '')
data['ClientTenure']= data['ClientTenure'].str.replace(']', '')

# Changing upper case letters to lower case
data['ItemDescription']= data['ItemDescription'].str.lower()

# Importing new data into a new data variable
seasons = pd.read_csv('value_inc_seasons.csv', sep=';')

# Merging both the data variables 
data = pd.merge(data, seasons, on = 'Month')

# Removing unwanted columns
data = data.drop('Year', axis=1)
data = data.drop('Month', axis=1)
data = data.drop('Day', axis=1)
data = data.drop('ClientKeywords', axis=1)

# Exporting to .CSV
data.to_csv('Value_inc_Cleaned', index = False)


