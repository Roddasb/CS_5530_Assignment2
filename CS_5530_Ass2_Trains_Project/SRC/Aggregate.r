library(dplyr)

# Read the data from the provided CSV file
data <- read.csv("/content/Clean_Modified_trains_data.csv")

# Step 1: Rename columns for better readability
data <- data %>%
  rename(Location_City = Location)

# Step 2: Mutate - Calculate the age of the car
data <- data %>%
  mutate(Car_Age = as.numeric(format(Sys.Date(), "%Y")) - Year)

# Step 3: Arrange the data by the year of manufacture (Year) in descending order
data <- data %>%
  arrange(desc(Year))

# Step 4: Summarize - Group by Location and summarize the data
summary_data <- data %>%
  group_by(Location_City) %>%
  summarize(
    Total_Cars = n(),
    Average_Kilometers = mean(Kilometers_Driven),
    Average_Price = mean(Price),
    Oldest_Car_Year = min(Year),
    Newest_Car_Year = max(Year)
  )

# View the summarized data
print(summary_data)