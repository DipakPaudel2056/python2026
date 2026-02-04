# panda is yet another data analysis library for Python.
# It is built on top of numpy library.

import pandas as pd
# creating a simple pandas Series
data = [10, 20, 30, 40, 50]
series = pd.Series(data)
print("Pandas Series:")
print(series)

# creating a pandas DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)
print("\nPandas DataFrame:")
print(df)



# loading data from a CSV file (assuming 'data.csv' exists in the same directory)
df_csv = pd.read_csv('./data.csv')
print("\nDataFrame loaded from CSV:")
print(df_csv)

# we can use the loc to access the rows and columns 
# and can also index them to get the desired column

print("\nAccessing 'Name' column using loc:")
print(df.loc[1]) #it access the row at index 1
print("\nAccessing 'Age' column using indexing:")
print(df['Age']) #it access the 'Age' column



# we can also get the json data loaded into pandas dataframe
print("\nLoading JSON data into DataFrame:")

df_json = pd.read_json('./data.json')
print(df_json)


