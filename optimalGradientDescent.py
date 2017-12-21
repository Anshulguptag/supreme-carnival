import numpy as np
import matplotlib.pyplot as plt

#iterations=50, features=4
x_points=np.arange(-5,5,0.067).reshape(50,3)
#row, col=np.indices((50,4))
mean=np.mean(x_points)
y_points=x_points < mean
a=y_points.astype(int)
theta=np.array([5,0.31,0.25,0.56])

def hypo_func(x,theta):
    exp = 2.712
    z=theta[1]*x[0]+theta[2]*x[1]+theta[3]*x[2]+theta[0]
    predict=1/(1+exp**(-z))
    predict1=predict.reshape(predict.size,1)
    return predict1

def cost_func(y,x,theta):
    step1=-(y*np.log(hypo_func(x,theta)))
    step2=-(1-y)*np.log(1-hypo_func(x,theta))
    cost=step1+step2
    return cost


def grad_calc(x,y):
    total=0
    total1=0
    total2=0
    total3=0
    for i in range(0,len(x)):
        total=total+(hypo_func(x[i],theta)-y[i])
        total1=total1+(hypo_func(x[i],theta)-y[i])*x[i][0]
        total2=total2+(hypo_func(x[i],theta)-y[i])*x[i][1]
        total3=total3+(hypo_func(x[i],theta)-y[i])*x[i][2]

    total=total.mean()
    total1 = total1.mean()
    total2 = total2.mean()
    total3 = total3.mean()

    return total/len(x), total1/len(x), total2/len(x), total3/len(x)

alpha=0.01


s=grad_calc(x_points,y_points)
theta1=np.zeros(4)
for i in range(0,4):
    theta1[i]=theta[i]-alpha*s[i]


b=theta1[0]
theta1=np.delete(theta1,0)
exp = 2.712
z1=np.dot(theta1,x_points.T)
hypo=1/(1+exp**(-z1))
hypo1=hypo.reshape(hypo.size,1)

plt.plot(z1,hypo1,marker='x',linestyle=' ')
plt.show()