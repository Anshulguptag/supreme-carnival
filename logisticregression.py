# logistic regression model
# want 0<=hypo<=1
# h(Q)=g(Q'x)=1/(1+e^(Q'x))
# g(Q'x)=Sigmoid function or logistic function

import numpy as np
import matplotlib.pyplot as plt
import math
theta=np.array([[1.25,0.35,0.36]])
# we declare theta just like this because it is consider as 2d array and we find transpose only 2D array

x=np.array([[200,300,300,210,360,100]])
pow=np.empty([3,6])

thetatrans=theta.T

pow=np.dot(thetatrans,x)

exp=2.718
i=0
hypo=np.empty([3,6])
hypo=1/(1+(exp**(-pow)))

minx=x.min()
maxx=x.max()
row=len(x)
col=len(x[0])
c=(maxx-minx)/(row*col)
x1=np.arange(minx,maxx,c+1)

plt.scatter(x1,hypo[i,:])
plt.show()

