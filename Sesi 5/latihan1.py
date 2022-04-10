import pandas as pd
import numpy as np

df = pd.read_csv("https://raw.githubusercontent.com/ardhiraka/PFDS_sources/master/nbaallelo.csv")
print(len(df))
print(df.shape)
print(df.head())