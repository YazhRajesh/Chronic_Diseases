#Importing libraries 
import pandas as pd
import numpy as np

from scipy.stats import zscore
from sklearn.model_selection import cross_val_score,GridSearchCV,train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, Lasso, Ridge
from sklearn.decomposition import NMF,PCA
from sklearn.metrics import accuracy_score, r2_score
import statsmodels.api as sm
from scipy import stats
from sklearn.ensemble import RandomForestRegressor
from data_preparation import *

import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline
pd.set_option('display.float_format', lambda x: '%.9f' % x)

# Local path to store the raw data
from get_data import get_data
path = '500cities.zip'
raw_data = get_data(path)

from eda import *
unhealthypiv,outcomespiv,data = get_unhealthy_behaviors_and_outcomes()