import pandas as pd
import numpy as np


#REad the csv file.
netflix_data = pd.read_csv (r"C:\Users\amcgrat\PycharmProjects\WEEK_4_PROJ\netflix_titles.csv")

#Take a look at the data
print(netflix_data.head())
print(netflix_data.shape)

missing_values_count = netflix_data.isnull().sum()
print(missing_values_count[0:5])

droprows = netflix_data.dropna()
print(netflix_data.shape,droprows.shape)

dropcolumns = netflix_data.dropna(axis=1)
print(netflix_data.shape,dropcolumns.shape)

cleaned_data = netflix_data.fillna(0)
cleaned_data = netflix_data.fillna(method='bfill', axis=0).fillna(0)


drop_duplicates= netflix_data.drop_duplicates()
print(netflix_data.shape,drop_duplicates.shape)

drop_duplicates= netflix_data.drop_duplicates(subset=['show_id'])
print(netflix_data.shape,drop_duplicates.shape)
