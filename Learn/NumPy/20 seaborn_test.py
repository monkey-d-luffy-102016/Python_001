# Distplot stands for distribution plot, it takes as input an array and plots a curve corresponding to the distribution of points in the array.
import matplotlib.pyplot as plt
import seaborn as sns

sns.histplot([0,1,2,3,4,5,6])
plt.savefig("/home/tejas/Programs/Python/Learn/NumPy/output.png")  # Saves the plot as an image file
