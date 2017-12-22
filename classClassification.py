import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data_fetch=pd.read_csv('data.csv')
x1=np.array(data_fetch['x1']).reshape(100,1)
x2=np.array(data_fetch['x2']).reshape(100,1)
f=0.5*x1-0.30*x2
c=(f>0).astype(int)
c[c==0]=-1
#print c
x_points1=np.zeros(100)
x_points2=np.zeros(100)
x_points3=np.zeros(100)
x_points4=np.zeros(100)

for i in range(0,len(c)):
    if c[i]==1:
        x_points1[i]=x1[i]
        x_points2[i]=x2[i]
    else:
        x_points3[i]=x1[i]
        x_points4[i]=x2[i]

x_points1=x_points1[~(x_points1==0)]
x_points2=x_points2[~(x_points2==0)]
x_points3=x_points3[~(x_points3==0)]
x_points4=x_points4[~(x_points4==0)]


plt.plot(x_points1,x_points2,marker='o',linestyle=' ',c='r',label='Positive')
plt.plot(x_points3,x_points4,marker='o',linestyle=' ',c='b',label='Negative')
plt.xlabel('<---------x1------->')
plt.ylabel('<---------x2------->')
plt.legend(loc='lower right')
plt.show()