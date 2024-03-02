import pandas as pd

# Read the data from the provided CSV file
data = pd.read_csv("/content/Clean_Modified_trains_data.csv")

# Step 1: Rename columns for better readability
data.rename(columns={'Location': 'Location_City'}, inplace=True)



# Step 3: Arrange the data by the year of manufacture (Year) in descending order
data.sort_values(by='Year', ascending=False, inplace=True)

# Step 4: Summarize - Group by Location and summarize the data
summary_data = data.groupby('Location_City').agg(
    Total_Cars=('ID', 'count'),
    Average_Kilometers=('Kilometers_Driven', 'mean'),
    Average_Price=('Price', 'mean'),
    Oldest_Car_Year=('Year', 'min'),
    Newest_Car_Year=('Year', 'max')
).reset_index()

# Round the numeric columns to 2 decimal places
summary_data = summary_data.round({'Average_Kilometers': 2, 'Average_Price': 2})



df.to_csv("Sumarize_trains_data.csv", index=False)

# Display the head of the modified DataFrame

print(df.head())
