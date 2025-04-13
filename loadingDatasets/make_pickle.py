import pickle
import pandas as pd
import numpy as np

filename = "load.csv"
data = pd.DataFrame({
    "a": [1, 2, 3],
    "b": [4, 5, 6],
    "c": [7, 8, 9],
    "d": [10, 11, 12],
    "e": [13, 14, 15]
})

with open('load_pickle.pkl', 'wb') as f:
    pickle.dump(data, f)
    
with open('load_pickle.pkl', 'rb') as f:
    data_loaded = pickle.load(f)
print(data_loaded)
print(data_loaded.columns)
print(data_loaded.index)
print(data_loaded.values)
print(data_loaded.dtypes)
print(data_loaded.shape)
print(data_loaded.head())
print(data_loaded.tail())
print(data_loaded.describe())
print(data_loaded.info())            