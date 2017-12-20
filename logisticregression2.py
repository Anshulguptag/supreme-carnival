import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

t_data=pd.read_csv('LR.csv')

theta=np.array([t_data['theta']])
x=np.array([t_data['x']])

z=np.dot(theta.T,x)
exp=2.718
hypo=1/(1+exp**(-z))
hypo=hypo[~np.isnan(hypo)]        #remove nan values from array
z=z[~np.isnan(z)]                 #remove nan values from array

xmin=x.min()
xmax=x.max()
ymin=hypo.min()
ymax=hypo.max()

plt.plot(z,hypo)
plt.axis([xmin,xmax,ymin,ymax])
plt.show()