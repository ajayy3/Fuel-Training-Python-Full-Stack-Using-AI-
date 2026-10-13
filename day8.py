#the preprocessing workflow

# Step     | Task                      | Typical Tools
# 1        | inspect the data          |head,info,describe,isnull 
# 2        | Clean text and types      |str methods , astype,to_numeric
# 3        | Remove duplicates         |duplicated, drop_duplicates
# 4        | Handle missing values     |dopna,fillna
# 5        | Handle outliers           |IQR rule,clip
# 6        | Encode categories         |map,get_dummies     
# 7        | scale numbers             |min-max,standardisation
# 8        | split train/test          |train_test_split

#-----------------------------------------------------------------------------------------------------------

#What to do with missing values ?

#option              | code                      | use when
# drop the rows        |df.dropna()                | very few rows are missing
# fill with mean       |fillna(col.mean())         | numbers,no outliers
# fill with median     |fillna(col.median())       | numbers with outliers
# fill with Mode       |fillna(col.mode()[0])      | categories
# fill whith a label   |fillna("unknown")          | text where blank has meaning

#----------------------------------------------------------------------------------------------------------
#Which encoding to use?

# Type of column      | Exampla                        | Method
# Ordered              A,B,C,or Low,Mid,High             map()
# Unordered            Pune,Mumbai,Kolhapur              get_dummise()
# Target/label         Pass/fail                         LabelEncoder() or map()