import numpy as np

import matplotlib.pyplot as plt

pop=[1,1,2,3,4,5,6,7,8,9,10,11]
pro=[1,2,3,1,4,5,6,4,7,10,15,9]
hypo=np.empty(12)
m=np.empty(12)
c=np.empty(12)
m[0]=0
b=np.empty(12)
b[0]=0
alpha=0.01
def linear(p,i):
    y=m[i]*p+b[i]
    return y
def summation(pop, pro, j):

    total=0
    total1=0
    for i in range(0,len(pop)):
        total=total+(linear(pop[i],j)-pro[i])
        total1=total1+((linear(pop[i],j)-pro[i])*pop[i])
    return total/len(pop), total1/len(pop)

for i in range (1,12):
    s1,s2 = summation(pop,pro,i-1)
    m[i] = m[i-1]-alpha*s1
    b[i] = b[i-1]-alpha*s2

for i in range(1,12):
    for j in range(0,len(pop)):
        hypo[j] = m[i]*pop[j]+b[i]

    plt.plot(pro, pop, marker='o', linestyle=' ', color='r')
    plt.plot(hypo, pop, linestyle='-', color='g')
    plt.legend(loc='lower right')
    plt.show()

