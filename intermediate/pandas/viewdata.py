# one of the most important features of pandas is its ability to handle and manipulate data efficiently.
import pandas as pd
# get the data from a csv
data = pd.read_csv('./data.csv')

# view the first 5 rows of the dataframe
print("First 5 rows of the DataFrame:")
print(data.head())

# we can also pass the number of rows we want to see
print("\nFirst 3 rows of the DataFrame:")
print(data.head(3))


# in the same way we can view the last n rows of the dataframe using tail() method
print("\nLast 5 rows of the DataFrame:")
print(data.tail())

# the info() method gives a concise summary of the dataframe
print("\nDataFrame Info:")
print(data.info())

# the describe() method generates descriptive statistics of the dataframe
print("\nDescriptive Statistics:")
print(data.describe())