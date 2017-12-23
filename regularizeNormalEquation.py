import numpy as np
import matplotlib.pyplot as plt

var0=np.random.randint(1,2,100).reshape(100,1)
var1=np.random.randint(800,1400,100).reshape(100,1)
var2=np.random.randint(2,5,100).reshape(100,1)
var3=np.random.randint(2,8,100).reshape(100,1)
var4=np.random.randint(20,50,100).reshape(100,1)

y=np.random.randint(100,450,100).reshape(100,1)
x=np.concatenate((var0,var1,var2,var3,var4),axis=1)

n=x.shape[1]
eye=np.identity(n)
eye[0,0]=0

lambda1=1000

xtrans= x.T
xmul=np.dot(xtrans,x)
internal=xmul+lambda1*eye
xinver=np.linalg.inv(internal)
xfinal=np.dot(xinver,xtrans)

theta=np.dot(xfinal,y)
print theta

