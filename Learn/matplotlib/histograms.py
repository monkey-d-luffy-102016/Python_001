import matplotlib.pyplot as plt
import numpy as np
data = np.random.randn(1000)
plt.hist(data, bins=30)
plt.show()