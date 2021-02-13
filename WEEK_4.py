import pandas as pd
import numpy as np

#raad the .csv file
netflix_data = pd.read_csv(r"C:\Users\amcgrat\\Desktop\netflix_titles.csv")

#Take a first look to understand the data
#print(netflix_data.head())
#print(netflix_data.shape)

#Count missing values in each column
missing_values_count = netflix_data.isnull().sum()
#print(missing_values_count[0:])

#Drop rows where data is missing
droprows= netflix_data.dropna()
print(netflix_data.shape,droprows.shape)
print (droprows.head())

#Drop Columns where data is missing
dropcolumns = netflix_data.dropna(axis=1)
print(netflix_data.shape,dropcolumns.shape)

#Fill all missing values with 0
cleaned_data = netflix_data.fillna(0)

#Fill all missing values to the value that comes next in the same column
cleaned_data = netflix_data.fillna(method='bfill', axis=0).fillna(0)

#Drop all rows that are duplicate
drop_duplicates= netflix_data.drop_duplicates()
print(netflix_data.shape,drop_duplicates.shape)

#Drop Duplicate Rows based on specific columns
drop_duplicates= netflix_data.drop_duplicates(subset=['show_id'])
print(netflix_data.shape,drop_duplicates.shape)

