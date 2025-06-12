# Import necessary libraries
import numpy as np                    # For numerical operations and array support
import matplotlib.pyplot as plt       # For plotting

# Define the function whose root we're trying to find: f(x) = x*sin(x) + cos(x)
def f(x):
    return x * np.sin(x) + np.cos(x)

# Define the derivative of f(x): g(x) = f'(x) = x*cos(x)
def g(x):
    return x * np.cos(x)

# Implementation of the Newton-Raphson Method
def newton_raphson(x0):
    tolerable_error = 1e-6       # Define acceptable error tolerance for convergence
    max_iteration = 100          # Set a cap on maximum iterations to prevent infinite loop
    xyz = [x0]                   # List to store successive approximations for plotting or analysis

    # Begin iteration
    for i in range(max_iteration):
        fx = f(x0)               # Evaluate function at current guess
        gx = g(x0)               # Evaluate derivative at current guess

        # Avoid division by zero if derivative is zero
        if gx == 0:
            print("Mathematical error: derivative is zero.")
            break

        # Newton-Raphson update formula
        x1 = x0 - (fx / gx)

        # Store the new approximation
        xyz.append(x1)

        # Check for convergence (if change is below tolerance)
        if abs(x1 - x0) < tolerable_error:
            break

        # Update x0 for next iteration
        x0 = x1

    # Return the final root and list of iterations
    return x1, xyz

# Initial guess
root, iteration = newton_raphson(2.5)

# Print the result
print(f"The root of x*sin(x)+cos(x) is: {root}")

# Plotting the function and the approximated root
x = np.linspace(-20, 20, 400)       # Generate x values for plotting
y = f(x)                            # Evaluate f(x) over the range

plt.figure(figsize=(10, 6))         # Set the figure size
plt.plot(x, y, label='f(x) = x*sin(x)+cos(x)', color='red')  # Plot the function
plt.axhline(0, color='black')       # Plot x-axis
plt.scatter(root, 0, label=f'approx_root = {root:.6f}', color='black')  # Mark the root
plt.title('Newton-Raphson Method for f(x) = x*sin(x)+cos(x)')  # Title
plt.xlabel('x')                     # Label x-axis
plt.ylabel('f(x)')                  # Label y-axis
plt.legend()                        # Show legend
plt.grid(True)                      # Add grid
plt.show()                          # Display the plot
