import numpy as np
import matplotlib.pyplot as plt

length=np.array([100,150,120,300,230,170])
breadth=np.array([200,190,100,160,210,160])

area=np.empty(6)

area=length*breadth

max =area.max()
min =area.min()

size=np.empty(6)
avg=area.mean()
size=(area-avg)/(max-min)

hypo=np.empty(6)

hypo=0.51+0.26*size+0.25*(size)**2
print hypo
plt.plot(hypo,size)
plt.show()