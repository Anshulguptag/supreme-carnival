import pandas as pd
import numpy as np


df=pd.read_csv('data.csv')
dex=np.random.randint(0,2,100)
df.insert(4,'dex',dex)
df.to_csv('data.csv')