# Import necessary libraries
import numpy as np                    # For numerical arrays and matrix operations
import matplotlib.pyplot as plt       # (Not used here, but typically for plotting)
import math                           # For factorial calculations

# Given x-values (independent variable)
x_vals = np.array([1, 2, 3, 4, 5])

# Corresponding y-values (dependent variable / function values at x)
y_init = np.array([-13, -10, 13, 98, 250])

# Number of data points
n = len(x_vals)

# Initialize the forward difference table with zeros
d = np.zeros((n, n))

# First column of difference table is the original y-values
d[:, 0] = y_init

# Compute the forward difference table
for i in range(1, n):                      # For each column (order of difference)
    for j in range(n - i):                 # For each row within valid range
        d[j][i] = d[j + 1][i - 1] - d[j][i - 1]  # Difference formula

# Display the forward difference table
print("Forward Difference Table:")
for i in range(n):
    print(f"{x_vals[i]:.2f}", end="\t")      # Print x value
    for j in range(n - i):                   # Print forward differences
        print(f"{d[i][j]:.2f}", end="\t")
    print()

# Point at which we want to interpolate the value
x = 3.9

# Starting point for interpolation (x₀ = first x-value)
x0 = x_vals[0]

# Step size (assumed to be equal for Newton Forward method)
h = x_vals[1] - x_vals[0]

# Calculate p = (x - x0)/h
p = (x - x0) / h

# Initialize interpolated value with f(x₀)
value = d[0][0]

# Initialize product term P = 1 (used in constructing p(p-1)(p-2)... terms)
P = 1

# Apply Newton Forward Interpolation Formula
for i in range(1, n):
    P *= (p - i + 1)                      # Compute p(p-1)(p-2)... incrementally
    value += (P * d[0][i]) / math.factorial(i)  # Add i-th term to the interpolated value

# Display the interpolated result
print(f"\nInterpolated value at x = {x} is {value}")
