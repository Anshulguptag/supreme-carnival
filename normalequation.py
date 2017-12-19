import numpy as np
import matplotlib.pyplot as plt
x=([1,2104,5,1,45],[1,1416,3,2,30],[1,1534,3,2,30],[1,852,2,1,36])
np_x=np.array(x)


y=[[460],[232],[315],[178]]
np_y=np.array(y)

#print np_x.shape        tell dimensions of numpy x array
#print np_y.shape        tell dimensions of numpy y array

#print np_y.T            Transpose of numpy y matrix
#print np_x.T            Transpose of numpy x matrix

xtrans= np_x.T
xmul=np.dot(xtrans,x)       #multiplication of n X m and m X p array
xinver=np.linalg.inv(xmul)  #inverse of xtrans (note: inverse is only find for those which have square matrix i.e. (n X n) matrix
xfinal=np.dot(xinver,xtrans)

theta=np.dot(xfinal,np_y)
print theta

