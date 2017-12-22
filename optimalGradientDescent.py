import numpy as np
import matplotlib.pyplot as plt
x=np.arange(-5,5,0.067).reshape(50,3)
x1=np.ones((50,1))
x_points=np.append(x1,x,axis=1)
theta=np.array([1,0.31,0.25,0.56])
theta1=np.array([1,0.31,0.25,0.56])
y_points=np.arange(-11,12,0.46).reshape(50,1)
def calc_hypo(x,theta):
    z=np.dot(x,theta)
    exp=2.712
    hypo= 1/(1+exp**(-z))

    return hypo

def calc_graddescent(x,y,theta,j):
     total=0
     for i in range(0,len(x)):
            total=total+(calc_hypo(x[i],theta)-y[i])*x[i][j]

     return total / len(x)

c=np.empty(4)
alpha=0.01
#c=calc_hypo(x_points[0],theta)
for i in range(0,len(theta)):
    c[i]=calc_graddescent(x_points,y_points,theta,i)
    theta[i]=theta[i]-alpha*c[i]

predict1=calc_hypo(x_points,theta1)
predict2=calc_hypo(x_points,theta)

plt.plot(x,predict1,c='r',label='old')
plt.plot(x,predict2,c='b',label='new')
plt.legend(loc='lower right')
plt.show()

