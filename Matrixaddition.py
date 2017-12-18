import numpy as np
import matplotlib.pyplot as plt
a=[[1,2,6],[3,4,8],[5,6,9]]
np_a=np.array(a)
b=[[9,8,4],[7,6,5],[7,6,2]]
np_b=np.array(b)
c=np.empty(10)
c=np_a+np_b
print c
#plt.scatter(c,s=50,c='r')
d=3*np_a + np_a + np_b/4
print d
x=np.array([2104,1416,1534,852])
h=np.empty(5)
h=-40+0.25*x
print h
s=[[0,0,0],[0,0,0],[0,0,0]]
matrix1=[[1,2104],[1,1416],[1,1534],[1,852]]
matrix2=[[-40,200,-150],[0.25,0.1,0.4]]
rmatrix=[[0,0,0],[0,0,0],[0,0,0]]
for i in range (0,3):
    for j in range (0,3):
        for k in range (0,2):
            rmatrix[i][j]=rmatrix[i][j]+matrix1[i][k]*matrix2[k][j]

print rmatrix
identity=np.empty([3,3])
for i in range (0,3):
    for j in range(0,3):
         if(i==j):
             identity[i][j]=1
         else:
             identity[i][j]=0

print identity

plt.scatter(x,h)
plt.show()
