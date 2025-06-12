# Importing necessary libraries
import numpy as np                  # For numerical operations like creating arrays
import matplotlib.pyplot as plt     # For plotting graphs

# Define the function for which we want to find the root
def f(x):                                       
    return x**3 - 5*x + 7                       # This is a cubic function

# Bisection method implementation
def bisection(a, b, tol):
    # First, check if the function has opposite signs at the endpoints
    if f(a) * f(b) >= 0:
        print("Bisection method fails: f(a) and f(b) must have opposite signs.")
        return None, []  # Return failure if no sign change

    iterations = []     # To store the midpoints of each iteration
    step = 1            # To keep track of the iteration number

    # Continue the loop until the interval size is less than the tolerance
    while (b - a) / 2 > tol:
        midpoint = (a + b) / 2   # Calculate the midpoint
        fm = f(midpoint)         # Evaluate the function at the midpoint

        # Print the current state of the iteration
        print(f"Iteration {step}: a = {a:.6f}, b = {b:.6f}, mid = {midpoint:.6f}, f(mid) = {fm:.6f}")
        iterations.append(midpoint)  # Store the midpoint for plotting

        # Check if the midpoint is a root (unlikely in floating point)
        if fm == 0:
            break
        # If the root lies between a and midpoint, update b
        elif f(a) * fm < 0:
            b = midpoint
        # Otherwise, update a
        else:
            a = midpoint

        step += 1  # Increment the step counter

    # Return the midpoint as the approximate root and the list of iterations
    return (a + b) / 2, iterations

# Choose an interval [a, b] where f(a) and f(b) have opposite signs
root, iter_list = bisection(-3, -2, tol=0.001)

# If a valid root is found, display and plot the results
if root is not None:
    print(f"\nApproximate root found by Bisection Method: {root:.6f}")

    # Generate x values for plotting the function
    x_vals = np.linspace(-4, 4, 400)
    y_vals = f(x_vals)  # Evaluate the function at all x values

    # Set up the plot
    plt.figure(figsize=(10, 6))
    plt.plot(x_vals, y_vals, label='f(x) = x³ - 5x + 7', color='blue')  # Function curve
    plt.axhline(0, color='black', linewidth=0.8)                        # x-axis
    plt.axvline(root, color='red', linestyle='--', label=f'Approx. Root ≈ {root:.4f}')  # Root line
    plt.scatter(iter_list, [f(x) for x in iter_list], color='green', s=30, label='Iterations')  # Midpoints
    plt.title("Bisection Method for f(x) = x³ - 5x + 7")  # Title of the plot
    plt.xlabel("x")       # x-axis label
    plt.ylabel("f(x)")    # y-axis label
    plt.grid(True)        # Add grid
    plt.legend()          # Show legend
    plt.show()            # Display the plot

