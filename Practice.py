import matplotlib.pyplot as plt
from IPython import get_ipython
get_ipython().magic('reset -sf')
import pandas as pd
import os
df_wine = pd.read_csv("C:\Brennan\datascience\data\winequality-red.csv")