# NumPy Cheatsheet

## NumPy Tutorial

### **NumPy HOME**
NumPy (Numerical Python) is a library for numerical computing in Python. It provides support for arrays, matrices, and mathematical operations.

### **NumPy Intro**
- Core library for numerical computing.
- Provides high-performance multidimensional arrays.
- Supports mathematical functions, linear algebra, and more.
- Uses C-based optimizations for speed.

### **NumPy Getting Started**
- Install NumPy using pip:
  ```sh
  pip install numpy
  ```
- Importing NumPy:
  ```python
  import numpy as np
  ```

## **NumPy Arrays**
### **Creating Arrays**
- Create a NumPy array:
  ```python
  arr = np.array([1, 2, 3, 4])
  ```
- Create an array with a specific shape:
  ```python
  arr = np.zeros((2, 3))  # 2x3 matrix of zeros
  ```

### **Array Indexing**
- Access elements:
  ```python
  arr[0]  # First element
  ```
- Accessing multiple elements:
  ```python
  arr[1:3]  # Slice from index 1 to 2
  ```

### **Array Slicing**
- Select a subarray:
  ```python
  arr[:, 1]  # All rows, second column
  ```

### **Data Types**
- Check data type:
  ```python
  arr.dtype
  ```
- Convert data type:
  ```python
  arr.astype(float)
  ```

### **Copy vs View**
- Copy creates a new object:
  ```python
  new_arr = arr.copy()
  ```
- View refers to the same object:
  ```python
  view_arr = arr.view()
  ```

### **Array Shape**
- Check shape:
  ```python
  arr.shape
  ```

### **Array Reshape**
- Change shape without modifying data:
  ```python
  arr.reshape(3, 2)  # Convert to 3x2
  ```

### **Array Iterating**
- Loop through elements:
  ```python
  for x in np.nditer(arr):
      print(x)
  ```

### **Array Join**
- Concatenate arrays:
  ```python
  np.concatenate((arr1, arr2), axis=0)
  ```

### **Array Split**
- Split an array:
  ```python
  np.array_split(arr, 3)
  ```

### **Array Search**
- Find an element:
  ```python
  np.where(arr == 4)
  ```

### **Array Sort**
- Sort array elements:
  ```python
  np.sort(arr)
  ```

### **Array Filter**
- Filter elements based on a condition:
  ```python
  arr[arr > 5]
  ```

## **NumPy Random**
### **Random Intro**
- Generate random numbers using NumPy's random module:
  ```python
  np.random.rand(5)  # 5 random values
  ```

### **Data Distribution**
- Generate normal distribution:
  ```python
  np.random.normal(0, 1, 10)  # Mean=0, StdDev=1, 10 values
  ```

### **Random Permutation**
- Shuffle array elements:
  ```python
  np.random.permutation(arr)
  ```

### **Seaborn Module**
- Seaborn is used for statistical visualizations:
  ```python
  import seaborn as sns
  sns.histplot(data)
  ```

## **Probability Distributions**
### **Normal Distribution**
- Generate normally distributed values:
  ```python
  np.random.normal(0, 1, 1000)
  ```

### **Binomial Distribution**
- Binomial probability simulation:
  ```python
  np.random.binomial(n=10, p=0.5, size=100)
  ```

### **Poisson Distribution**
- Generate Poisson-distributed values:
  ```python
  np.random.poisson(lam=3, size=1000)
  ```

### **Uniform Distribution**
- Generate uniform values between 0 and 1:
  ```python
  np.random.uniform(0, 1, 100)
  ```

### **Logistic Distribution**
- Used for binary classification modeling:
  ```python
  np.random.logistic(0, 1, 100)
  ```

### **Multinomial Distribution**
- Simulate multi-outcome events:
  ```python
  np.random.multinomial(10, [0.2, 0.3, 0.5])
  ```

### **Exponential Distribution**
- Used for time until an event occurs:
  ```python
  np.random.exponential(scale=2, size=100)
  ```

### **Chi-Square Distribution**
- Used in statistical tests:
  ```python
  np.random.chisquare(df=2, size=100)
  ```

### **Rayleigh Distribution**
- Used in signal processing:
  ```python
  np.random.rayleigh(scale=2, size=100)
  ```

### **Pareto Distribution**
- Used in economics and finance:
  ```python
  np.random.pareto(a=3, size=100)
  ```

### **Zipf Distribution**
- Used in linguistics and social sciences:
  ```python
  np.random.zipf(a=2, size=100)
  ```

## **NumPy ufunc (Universal Functions)**
### **Ufunc Introduction**
- NumPy universal functions (ufuncs) operate on ndarrays:
  ```python
  np.add(arr1, arr2)
  ```
### **Common Ufuncs & Parameters**
- `np.add(x1, x2)`: Element-wise addition.
- `np.subtract(x1, x2)`: Element-wise subtraction.
- `np.multiply(x1, x2)`: Element-wise multiplication.
- `np.divide(x1, x2)`: Element-wise division.
- `np.round(x, decimals=0)`: Round elements.
- `np.floor(x)`: Round down.
- `np.ceil(x)`: Round up.
- `np.log(x)`, `np.log10(x)`: Logarithms.
- `np.sum(a, axis=None)`: Sum elements.
- `np.prod(a, axis=None)`: Product of elements.
- `np.diff(a, n=1)`: Discrete differences.
- `np.lcm(x1, x2)`: Least common multiple.
- `np.gcd(x1, x2)`: Greatest common divisor.
- `np.sin(x)`, `np.cos(x)`, `np.tan(x)`: Trigonometric functions.
- `np.sinh(x)`, `np.cosh(x)`: Hyperbolic functions.
- `np.union1d(arr1, arr2)`: Union of sets.
- `np.intersect1d(arr1, arr2)`: Intersection of sets.

---
This cheatsheet summarizes key NumPy functions and probability distributions. 🚀
