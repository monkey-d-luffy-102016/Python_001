import matplotlib.pyplot as plt
fig, axs = plt.subplots(2, 2)
axs[0, 0].plot([1, 2, 3, 4], [10, 20, 25, 30])
axs[1, 1].plot([1, 2, 3, 4], [30, 25, 20, 10])
plt.show()