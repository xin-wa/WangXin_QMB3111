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

