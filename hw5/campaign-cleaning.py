# -*- coding: utf-8 -*-
"""
Missing Data in 2016 Campaign Contribution Data

Instructions: 
  - Problems start with #@ and then give a number.  Enter your
    Python code after each problem.  

  - Your code for a problem cannot refer to variables or functions
    you defined in your code for previous problems.  However, your
    code for a problem can define temporary variables and functions
    that will be used only within the code for that problem.
    
  - Your code for any problem can refer to the variable 'df', which
    is the main data frame.

  - If the problem asks you to compute something, the last line
    of your answer must be an *expression* (an expression is
    something that could go on the right hand side of the ' = '
    in an assignment statement)

  - In all problems, "NA" means NA values as decided by function
    numpy.isna(), and not any other values that may also seem
    to indicate missing data, such as the string "N/A".
    
  - The data used here is a sample of a larger data set.  I will test your
    code on a different sample of the full data set.
"""

import numpy as np
import pandas as pd

pd.set_option('display.max_columns', 500)

# Read the data.  This data is a subset of the 2016 presidential
# campaign contribution data for the state of California.  Spend
# a little time looking at the data -- it is interesting.

df = pd.read_csv("https://raw.githubusercontent.com/grbruns/cst383/master/campaign-ca-2016-sample.csv")

# get a summary of the data, and get a rough
# idea of where NA values lie

df.info()

#@ 1
# What is the total number of NAs in df?
# (compute a number)
df.isna().sum().sum()

#@ 2
# What fraction of all values in df are NA values?
# (compute a number between 0 and 1)
(df.isna().sum().sum())/(df.size)

#@ 3
# What fraction of the values in each column are NA?
# Show only non-zero values, and sort the result by
# decreasing value.
# (compute a Pandas Series)
df.isna().mean().loc[df.isna().mean() > 0].sort_values(ascending=False)

#@ 4
# Which columns contain more than 40% NA values?
# (compute a NumPy array of the column names, sorted alphabetically)
np.array(df.isna().mean().loc[df.isna().mean() > 0.4].index.sort_values(ascending=True))

#@ 5
# Compute a series that show the cumulative fraction of
# NA data contained in columns, ordered by most-NA column first.
#
# "Cumulative" means that the first element in the series will
# be the fraction of NA data in the most-NA column, the
# second element in the series will be the sum of the fraction
# of the data in the most-NA column and the fraction of the
# data in the next-most-NA column, etc.  The last values in
# the series must be 1.0.
# (compute a NumPy series)
(df.isna().sum()/df.isna().sum().sum()).sort_values(ascending=False).cumsum()

#@ 6
# What fraction of the rows in df contain at least 2 NA values?
# (compute a single number between 0 and 1)
(df.isna().sum(axis=1).loc[df.isna().sum(axis=1) >= 2]).count()/len(df.index)

#@ 7
# There are other values in the dataset, besides NA, that
# represent missing data.  How to find them?
# For example, how many empty strings are in the data?  Do not 
# search in the numeric columns: 'contb_receipt_amt' and 'file_num'.
# Hint: to get only the 'object' type columns, consider
# pandas.DataFrame.select_dtypes.
# (compute a single number)
(df.select_dtypes(exclude='number') == '').sum().sum()

#@ 8
# Would you expect contbr_employer to contain data that
# represent missing values?  Create a series with counts
# of the values that occur in the contbr_employer column the
# most.  The series should contain the 15 most-occurring
# values, listed in decreasing order.  Do you think any
# of the values represent missing values?
# (compute a Series)
df['contbr_employer'].value_counts().sort_values(ascending=False).iloc[:15]

#@ 9
# Repeat the previous problem, but this time create a data
# frame showing the 15 most-occurring values for columns
# contbr_employer, contbr_occupation, and contbr_city.
# You will not show the counts.  Hint: create a function
# that takes a series s and returns a series containing
# as data the 15 most-occurring values in s, in descending
# order.  The index of the returned series should range from
# 0 to 14.  Then use pandas.DataFrame.apply() with this function.
# (compute a DataFrame)
def top_vals(s):
    return pd.Series(s.value_counts().sort_values(ascending=False).iloc[:15].index)
df[['contbr_employer', 'contbr_occupation', 'contbr_city']].apply(top_vals)

#@ 10
# Look carefully at the output of the last problem.  (Do this
# before continuing.)
# Did you notice that the contbr_employer and contbr_occupation
# columns contain values 'INFORMATION REQUESTED' and
# 'INFORMATION REQUESTED PER BEST EFFORTS'?  These values -- but
# not values like 'NOT EMPLOYED' -- seem to indicate missing data.
# Modify df so that *all* values 'INFORMATION REQUESTED' and
# 'INFORMATION REQUESTED PER BEST EFFORTS' are placed with nan.
# Use DataFrame.replace(), with option 'inplace=True'.
# (write a pd.DataFrame.replace() statement)
df.replace(['INFORMATION REQUESTED', 'INFORMATION REQUESTED PER BEST EFFORTS'], np.nan, True)

#@ 11
# Did you notice that 'NOT EMPLOYED' and 'NONE'
# appear frequently in the contbr_employer column?   Do you
# think that these values represent missing data?  Replace
# all occurrences of 'NONE' in column 'contbr_employer'
# with 'NOT EMPLOYED'.
# Use Series.replace(), with option 'inplace=True'.
# (write a pd.Series.replace() statement)
df['contbr_employer'].replace(to_replace='NONE', value='NOT EMPLOYED', inplace=True)

#@ 12
# Lots of people are self-employed.  Compute a NumPy array of
# all the values in 'contbr_occupation' that contain the string 'SELF'.
# You may want to use pd.Series.str.contains().  Check out the 'na' option.
# (compute a NumPy array)
df['contbr_occupation'].loc[df['contbr_occupation'].str.contains('SELF', na=False)].unique()

#@ 13
# Update df to remove all columns containing at least 50% NA values.
# Use DataFrame.dropna with the 'thresh' option
# (write a pd.DataFrame.dropna() statement)
df.dropna(axis=1,thresh=((len(df.index))/2),inplace=True)

#@ 14
# Column election_tp has a very small number of NA values.
# Drop all *rows* of df for which election_tp is NA.
# (write a pd.DataFrame.dropna() statement)
df.dropna(subset=['election_tp'], inplace=True)

#@ 15
# What about bad zip values?  
# How many contbr_zip values contain characters that are not digits?
# Hint: the regular expression that matches something that is not
# a digit is '[^0-9]'  Consider using Series.str.contains() for this.
# (compute a number)
df['contbr_zip'].str.contains('[^0-9]').sum()


#@ 16
# What fraction of contb_receipt_amt values are less than 0?
# (compute a number between 0 and 1)
df['contb_receipt_amt'].loc[df['contb_receipt_amt'] < 0].count()/df['contb_receipt_amt'].count()


#@ Here are some tests that look at your final data frame
# (you do not need to provide any code here, but do not modify
# or remove the code below)

df.info()

(df['contbr_occupation'] == 'NONE').sum()







