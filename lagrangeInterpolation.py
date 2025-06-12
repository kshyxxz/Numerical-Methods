# Import necessary libraries
import numpy as np                    # For numerical arrays and operations
import matplotlib.pyplot as plt       # For plotting

# Function to perform Lagrange Interpolation
def lagrange_interpolation(x_val, y_val, x_value):
    n = len(x_val)                    # Number of known data points
    result = 0                        # Initialize result of interpolation

    # Loop through each term in the Lagrange formula
    for i in range(n):
        term = y_val[i]               # Start with y_i (initial weight for L_i(x))

        # Construct L_i(x) = Π (x - x_j)/(x_i - x_j) for j ≠ i
        for j in range(n):
            if j != i:
                term *= (x_value - x_val[j]) / (x_val[i] - x_val[j])
        
        # Accumulate the result
        result += term

    return result                     # Return final interpolated value

# Known x and y data points
x_val = np.array([-13, -10, 10, 27])
y_val = np.array([-5, -7, 17, 30])

# Point at which we want to interpolate the y-value
x_value = 5

# Call the interpolation function
interpolated_value = lagrange_interpolation(x_val, y_val, x_value)

# Output the interpolated result
print("*** LAGRANGE INTERPOLATION IMPLEMENTATION by kshyxxz ***")
print(f"The interpolated value at x = {x_value} is: {interpolated_value}")

# Create a smooth set of x values for plotting the interpolation curve
x_interp = np.linspace(min(x_val), max(x_val), 100)

# Compute the corresponding interpolated y values
y_interp = [lagrange_interpolation(x_val, y_val, xi) for xi in x_interp]

# Plot original data points
plt.scatter(x_val, y_val, color='#DDA0DD', label='Data Points')

# Highlight the interpolated point at x = 5
plt.scatter(x_value, interpolated_value, color='darkred', label='y - value @ x = 5')

# Plot the interpolated polynomial curve
plt.plot(x_interp, y_interp, color='navy', label='Interpolated Polynomial')

# Add titles and labels
plt.title('LAGRANGE INTERPOLATION by kshyxxz')
plt.xlabel('x')
plt.ylabel('y')

# Draw axes lines
plt.axhline(0, color='black')
plt.axvline(0, color='black')

# Add legend and grid for clarity
plt.legend()
plt.grid(True)

# Show the final plot
plt.show()
