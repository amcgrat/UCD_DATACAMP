df = pandas.read_csv("C:/Users/amcgrat/Desktop/PYTHON/L2_DATA_FILES/ORS_DESC_EXPORT_TXT_CLEANED_COMMA_TOP_100.csv", usecols = ['ORS DESCRIPTION'])
from collections import Counter
res = df['ORS DESCRIPTION'].str.split().apply(Counter)
res1 = sorted(res.items())