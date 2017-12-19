import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 2*(np.pi))
plt.plot(x, np.sin(x),c='b')
plt.plot(x, np.cos(x),c='r')
#plt.legend(loc='lower right')
plt.xlabel('Angle [rad]')
plt.ylabel('sin(x), cos(x)')
plt.axis('tight')
plt.show()
