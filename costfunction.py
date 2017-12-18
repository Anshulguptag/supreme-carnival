import matplotlib.pyplot as plt
import numpy as np

# create 1000 equally spaced points between -10 and 10
x =np.array([-5,-4,-3,-2,-1,0,1,2,3,4,5])
y=np.array([-6,-5,-4,-3,-2,-1,0,1,2,3,4])
# calculate the y value for each element of the x vector
cost=np.array(11)
cost = (((0.35*x+0.20)-y)**2)/(2*len(x))

fig, ax = plt.subplots()
ax.plot(x, cost)
plt.show()
