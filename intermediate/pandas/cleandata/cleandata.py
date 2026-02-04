# after we do the initial observation of the data it is time to clean the data

# load data and do initial observation
import pandas as pd
data = pd.read_csv('./messydata.csv')
print(data.info())


# first and foremost we need to handle missing data
# check for missing data
print("Missing data in each column:")
print(data.isnull().sum())

# let's remove all the missing data and get new df
cleaned_data = data.dropna()
print("Data after removing missing values:")
print(cleaned_data.info())

# here we have a new data frame called cleaned_data which has no missing values
# however if we want to do this for the originaql data we can do the following
data.dropna(inplace=True)
print("Original data after removing missing values:")
print(data.info())
# now we have the understanding of missing data we can fill them with some values

# to do that we use a function called fillna()
data_filled = data.fillna({
    'Duration': 0,  # fill missing Duration with 0
    'Date': '2024-01-01',  # fill missing Date with a default date
})
print("Data after filling missing values:")
print(data_filled.info())

# next we need to handle duplicates
# check for duplicates
print("Number of duplicate rows:", data.duplicated().sum())
# remove duplicates
data_no_duplicates = data.drop_duplicates()
print("Data after removing duplicates:")
print(data_no_duplicates.info())

