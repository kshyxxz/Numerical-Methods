import numpy as np
import sys

# Input number of unknowns
n = int(input('Enter the number of unknowns: '))

# Initialize augmented matrix and solution array
a = np.zeros((n, n + 1))
x = np.zeros(n)

# Input augmented matrix coefficients
print("\nEnter the augmented matrix coefficients row by row:")
for i in range(n):
    for j in range(n + 1):
        a[i][j] = float(input(f"  a[{i+1}][{j+1}] = "))

print("\nInitial Augmented Matrix:")
print(a)

# Perform Gauss-Jordan elimination
for i in range(n):
    if a[i][i] == 0:
        sys.exit("Mathematical Error: Division by zero detected!")

    for j in range(n):
        if j != i:
            ratio = a[j][i] / a[i][i]
            for k in range(n + 1):
                a[j][k] -= ratio * a[i][k]

# Display matrix after Gauss-Jordan elimination
print("\nMatrix after Gauss-Jordan Elimination:")
print(np.round(a, 2))

# Calculate solutions
for i in range(n):
    x[i] = a[i][n] / a[i][i]

# Display the solutions
print("\nRequired Solution:")
for i in range(n):
    print(f"  x{i + 1} = {x[i]:.4f}")

