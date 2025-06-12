# Import necessary libraries
import numpy as np                    # For numerical operations
import matplotlib.pyplot as plt       # For plotting the function and root

# Define the function whose root we want to find: f(x) = x³ - 5x + 7
def f(x):
    return x**3 - 5*x + 7

# Secant Method implementation
def secant(x0, x1, e):
    print('\n*** SECANT METHOD IMPLEMENTATION ***')
    condition = True                  # A condition flag to control loop execution

    # Iterate until the condition (tolerance not met) is satisfied
    while condition:
        # Check for zero denominator (to avoid division by zero)
        if f(x0) == f(x1):
            print('Divide by zero error!')
            break

        # Apply Secant Method formula:
        # x2 = x0 - [(x1 - x0) * f(x0)] / [f(x1) - f(x0)]
        x2 = x0 - (x1 - x0) * f(x0) / (f(x1) - f(x0))

        # Print the current approximation and its function value
        print('x2 = %0.6f and f(x2) = %0.6f' % (x2, f(x2)))

        # Update x0 and x1 for the next iteration
        x0 = x1
        x1 = x2

        # Check whether the result is within the acceptable error (tolerance)
        condition = abs(f(x2)) > e

    # Print the final root after convergence
    print('\nRequired root is: %0.8f' % x2)
    return x2                         # Return the computed root

# Initial guesses for the root
x0_val = -2.0
x1_val = -3.0

# Acceptable error (tolerance)
e_val = 0.0001

# Call the secant function to find the root
root = secant(x0_val, x1_val, e_val)

# Create x values for plotting the function around the root
x_vals = np.linspace(root - 3, root + 3, 600)
y_vals = f(x_vals)

# Plotting the function and the root
plt.figure(figsize=(10, 6))                              # Set figure size
plt.plot(x_vals, y_vals, label='f(x) = x^3 - 5x + 7', color="#BBF90F")  # Plot the function
plt.title("SECANT METHOD by kshyxxz")                   # Title of the plot
plt.xlabel("X")                                          # Label x-axis
plt.ylabel("F(X)")                                       # Label y-axis

# Mark the root found by the secant method
plt.scatter(root, 0, color="red", marker="*", label=f'Root = {root:.6f}')

# Add grid and axes lines for better visualization
plt.grid(True)
plt.axhline(0, color='black')    # X-axis
plt.axvline(0, color='black')    # Y-axis

# Show legend and plot
plt.legend()
plt.show()
