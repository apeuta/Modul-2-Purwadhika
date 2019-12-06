import pandas as pd
import numpy as numpy

df = pd.read_csv("data.csv")
df = df.replace("-",0)
print (df)