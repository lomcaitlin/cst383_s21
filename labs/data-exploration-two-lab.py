import numpy as npimport pandas as pdimport matplotlib.pyplot as pltimport seaborn as snsdf = pd.read_csv('https://raw.githubusercontent.com/grbruns/cst383/master/College.csv', index_col=0)# --- pt 1 3/11/21 -------------------# 3 asns.scatterplot(x=df['F.Undergrad'], y=df['Expend'])# 3 bsns.scatterplot(x=df['F.Undergrad'], y=df['Outstate'])# 3 cdf['perc.accept'] = (100*df.Accept/df.Apps)df['perc.enroll'] = (100*df.Enroll/df.Accept)# --- pt 2 3/16/21 ---------------------# 3df['Size'] = pd.cut(df['F.Undergrad'],                    include_lowest=True,                    bins=df['F.Undergrad'].quantile([0, 0.33, 0.66, 1.0]),                    labels=['small', 'medium', 'large'])df.Size.value_counts().plot.bar()