from sklearn.neighbors.kde import KernelDensity
import numpy as np
import matplotlib.pyplot as plt

plt.plot(np.random.uniform(0, 10, 100), np.random.uniform(0, 10, 100), 'o')
plt.show()

plt.plot(np.random.standard_normal(100), np.random.standard_normal(100), 'o')
plt.show()
