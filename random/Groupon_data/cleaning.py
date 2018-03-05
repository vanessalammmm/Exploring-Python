
# Import required libraries

import numpy as np
import pandas as pd
import re

# Read data file

listings=pd.read_csv('listings_beauty.csv')

# Convert Price columns to numeric dtype

for col in ['Original Price','Sale Price']:
    for i in ['S','$',',']:
        listings[col]=listings[col].str.replace(i,'')
    listings[col]=pd.to_numeric(listings[col])

# Convert date columns to datetime dtype

listings['Offer start date']=listings['Offer start date'].apply(lambda x:x[:10])

for col in ['Offer start date','Date retrieved']:
    listings[col]=pd.to_datetime(listings[col])

# Calc age of offer in days

listings['Offer Age']=listings['Date retrieved']-listings['Offer start date']
listings['Offer Age']=listings['Offer Age'].dt.days

# Export df

listings.to_csv('listings_beauty_cleaned.csv')

