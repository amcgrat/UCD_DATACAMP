import pandas as pd
import numpy as np

#raad the .csv file
netflix_data = pd.read_csv(r"C:\Users\amcgrat\\Desktop\netflix_titles.csv")

#Take a first look to understand the data
#print(netflix_data.head())
#print(netflix_data.shape)

#Count missing values in each column
missing_values_count = netflix_data.isnull().sum()
print(missing_values_count[0:])