import pandas as pd
import numpy as np
import pylab
data = pd.read_csv('../csv/train.csv', header=0)
# print(data.describe())

# print(data[data.Age > 60].Sex)

print(type(data.values))
