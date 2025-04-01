import os # To set working directory
import numpy as np # For log transformation
# import math
import pandas as pd # To read and inspect data
import statsmodels.formula.api as sm # to estimate linear regression
# import statsmodels.formula.api as smf # Another way to estimate regression
# import statsmodels.api as sm # Another way to estimate regression
import statsmodels.nonparametric.kernel_regression as npreg
# FOr nonparametric kernel regression
import matplotlib.pyplot as plt  # To plot regression results
# import seaborn as sns # Another package for plotting data
# sns.set(style="white")
# sns.set(style="whitegrid", color_codes=True)
import sqlite3


os.getcwd()
# Change to a new directory.
git_path = 'C:/Users/x/Documents/GitHub/WangXin_QMB3111/'
os.chdir(git_path + 'Project')
# Check that the change was successful.
os.getcwd()

# Load Data.
hmda = pd.read_csv('hmda_sw.csv')

# Take a look at the individual types of columns in the data frame.
hmda.dtypes
#s23a=marital stat s13=race s45=debt-to-inc ratio 
#s27a=self-employ school=education s7=action taken s19a=reasons for denial

# Check the dimensions of the data.
hmda.index
hmda.columns

# Calculate summary statistics for your data.
hmda.describe()

# Look at a few variables at a time.
hmda[['s7','s13','s19a','s23a','s27a','s45','school']].describe()

# Inspect the target variable.
hmda['s13'].value_counts()
# 5=white, 3=black
hmda['s23a'].value_counts()
# M=married U=unwed S=separated
hmda['s27a'].value_counts()
# 0=not self-employed 1=self-employed
hmda['s45'].value_counts()
# debt-to-income ratio
hmda['school'].value_counts()
# years of education

hmda['s7'].value_counts()
# 1=loan originated 2=application approved but not accepted 3=application denied

# Display the correlation matrix.
hmda[['s13','s7']].corr()

# Plot a histogram (default width of bins).
n, bins, patches = plt.hist(x = hmda['s13'], 
                            bins = 'auto', 
                            color = '#0504aa',
                            alpha = 0.7, rwidth = 0.85)
plt.grid(axis='y', alpha=0.75)
plt.xlabel('Race')
plt.ylabel('Frequency')
plt.title('Histogram of Race')
# Create the plot in pdf.
# plt.savefig('Images//price_hist.pdf')
# But png will plot in the README file.
plt.savefig('Images//race.png')
plt.show()

n, bins, patches = plt.hist(x = hmda['s7'], 
                            bins = 'auto', 
                            color = '#0504aa',
                            alpha = 0.7, rwidth = 0.85)
plt.grid(axis='y', alpha=0.75)
plt.xlabel('Approvals')
plt.ylabel('Frequency')
plt.title('Histogram of Approvals')
# Create the plot in pdf.
# plt.savefig('Images//price_hist.pdf')
# But png will plot in the README file.
plt.savefig('Images//approvals.png')
plt.show()

#Calculate baseline probability of approval
hmda['s7'].value_counts() / len(hmda.s7)

# 
print(pd.crosstab(hmda['s13'], hmda['s7']))

print(pd.crosstab(hmda['s13'], hmda['s7']))/len(hmda.s7)

value_counts