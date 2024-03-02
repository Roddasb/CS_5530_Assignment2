import pandas as pd
import re
from datetime import datetime

# Assuming you have your dataset stored in a CSV file named "cars_data.csv"
# You can read the CSV file into a pandas DataFrame
df = pd.read_csv("/content/train.csv")

## Here I assigned ID name to Unnamed column
df = df.rename(columns={'Unnamed: 0': 'ID'})


## Before looking for the missing values I went ahead and removed strings from all Numeric values
## Question 2 b) Remove the units from some of the attributes and only keep the numerical values (for example remove kmpl from “Mileage”, CC from “Engine”, bhp from “Power”, and lakh from “New_price”). (4 points)

# Remove non-numeric characters from specified columns and convert to numeric values
numeric_cols = ['Engine', 'Mileage', 'Power', 'New_Price']

for col in numeric_cols:
    df[col] = df[col].apply(lambda x: re.sub(r'[^0-9.]', '', str(x)))


# Convert columns to numeric
df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors='coerce')

# Rename specified columns
df = df.rename(columns={"Mileage": "Mileage_kms",
                        "Engine": "Engine_cc",
                        "Power": "Power_bhp",
                        "New_Price": "New_Price_Lakh"})


## Question  C) Change the categorical variables (“Fuel_Type” and “Transmission”) into numerical one hot encoded value.  (4 points).
# Replace categorical variables with fuzzy codes

df['Transmission'] = df['Transmission'].replace({'Manual': 0, 'Automatic': 1})
df['Fuel_Type'] = df['Fuel_Type'].replace({'Petrol': 0, 'Diesel': 1, 'CNG': 2, 'LPG': 3, 'Electric': 4})


## Queston 1 a)  Look for the missing values in all the columns and either impute them (replace with mean, median, or mode) or drop them. Justify your action for this task.     (5 points)
## First lets count mising value for each column

missing_values = df.isnull().sum()

print("Number of missing values in each column:")
print(missing_values)

## since the number of missing values for New_price is more than 20% of the data set , we will impute the missing values and replace with mean for New price and drop the missing values for
# Impute missing values for New_Price (In Lakh) column
##df['New_Price (In Lakh)'] = df['New_Price (In Lakh)'].fillna(method='ffill', limit=1)


mean_new_price = df['New_Price_Lakh'].mean()

# Limit decimal points to two
mean_new_price = round(mean_new_price, 2)

# Impute missing values in the "New_Price" column with the mean value
df['New_Price_Lakh'] = df['New_Price_Lakh'].fillna(mean_new_price)



# We can drop rows with missing values for Mileage, Engine,power & seats because the number of missing values is less than 10% of the total dataset
df = df.dropna(subset=['Seats', 'Power_bhp', 'Engine_cc', 'Mileage_kms'])

##d) Create one more feature and add this column to the dataset (you can use mutate function in R for this). For example, you can calculate the current age of the car by subtracting “Year” value from the current year.   (4 points)



df['Price_Difference_Lakh'] = df['New_Price_Lakh'] - df['Price']




df.to_csv("Clean_Modified_trains_data.csv", index=False)

# Display the head of the modified DataFrame

print(df.head())