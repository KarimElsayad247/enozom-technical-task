import pandas as pd
import numpy as np
import hashlib

# I use pandas library to read the data because it makes it easier to work with tabular data
data = pd.read_csv('annual-enterprise-survey-2020-financial-year-provisional-csv.csv')

# I want to see how many rows there are, to make sure I split the table correctly
print(data.shape)

# I get the data of 3rd column which happens to be named 'Industry_code_NZSIOC'
third_col = data['Industry_code_NZSIOC']

# Should have the same amount of rows as before
print(len(third_col))

# now to get the odd rows. iloc() is a function that allows us to access rows by index
# I assume odd rows start with the first column, which has index 0
third_col_odd_rows =  third_col.iloc[::2]

# I make sure it's half the previous length
print(len(third_col_odd_rows))

# next step is Concatenating the data. To do that I put them all in a list, 
# then use python method join() to Concatenate them
# pandas method Series.tolist() makes this very convenient
content = third_col_odd_rows.tolist()

# now to create a string
full_string = ''.join(str(x) for x in content)

# And finally, hasing
result = hashlib.md5(full_string.encode())
print(result.hexdigest().upper())