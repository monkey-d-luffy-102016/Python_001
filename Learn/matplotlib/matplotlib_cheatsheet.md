# Matplotlib Cheatsheet

## Matplotlib Intro
Matplotlib is a Python library for creating static, animated, and interactive visualizations.

## Matplotlib Get Started
Install Matplotlib using:
```sh
pip install matplotlib
```
Importing Matplotlib:
```python
import matplotlib.pyplot as plt
```

## Matplotlib Pyplot
Pyplot is a module in Matplotlib providing a MATLAB-like interface.
```python
import matplotlib.pyplot as plt
plt.plot([1, 2, 3, 4])
plt.ylabel('some numbers')
plt.show()
```

## Matplotlib Plotting
Basic plotting:
```python
import matplotlib.pyplot as plt
x = [1, 2, 3, 4]
y = [10, 20, 25, 30]
plt.plot(x, y)
plt.show()
```

## Matplotlib Markers
Markers highlight data points in a plot.
```python
import matplotlib.pyplot as plt
plt.plot([1, 2, 3, 4], [10, 20, 25, 30], marker='o')
plt.show()
```

## Matplotlib Line
Customize line styles and colors.
```python
plt.plot([1, 2, 3, 4], [10, 20, 25, 30], linestyle='dashed', color='red')
plt.show()
```

## Matplotlib Labels
Adding labels to axes.
```python
plt.xlabel('X Axis Label')
plt.ylabel('Y Axis Label')
plt.title('Title of the Graph')
plt.show()
```

## Matplotlib Grid
Enable grid in the plot.
```python
plt.grid(True)
plt.show()
```

## Matplotlib Subplot
Create multiple subplots in a single figure.
```python
fig, axs = plt.subplots(2, 2)
axs[0, 0].plot([1, 2, 3, 4], [10, 20, 25, 30])
axs[1, 1].plot([1, 2, 3, 4], [30, 25, 20, 10])
plt.show()
```

## Matplotlib Scatter
Scatter plot for visualizing point data.
```python
plt.scatter([1, 2, 3, 4], [10, 20, 25, 30])
plt.show()
```

## Matplotlib Bars
Bar chart representation.
```python
plt.bar([1, 2, 3, 4], [10, 20, 25, 30])
plt.show()
```

## Matplotlib Histograms
Histogram to visualize frequency distribution.
```python
import numpy as np
data = np.random.randn(1000)
plt.hist(data, bins=30)
plt.show()
```

## Matplotlib Pie Charts
Pie chart for categorical data.
```python
labels = ['A', 'B', 'C', 'D']
sizes = [10, 20, 30, 40]
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.show()
```
