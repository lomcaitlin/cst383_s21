import numpy as npimport pandas as pdimport seaborn as snsfrom matplotlib import rcParams# allow output to span multiple output lines in the consolepd.set_option('display.max_columns', 500)# switch to seaborn default stylistic parameters# see the useful https://seaborn.pydata.org/tutorial/aesthetics.htmlsns.set()sns.set_context('paper')   # 'talk' for slightly larger# change default plot sizercParams['figure.figsize'] = 9,7# 1 read datainfile = "https://raw.githubusercontent.com/grbruns/cst383/master/campaign-ca-2016-sample.csv"df = pd.read_csv(infile)# 2 look @ data using variable explorer# 3 look at the type of each column in dfdf.info()# 4 which columns contain NA values?df.isna().sum()df.isna().sum().sum()# 5 find values 