import numpy as np

def f(x):
  return x*np.sin(x)+np.cos(x)

print('Enter 1 for Gaussian 2 point implementation : ')
print('Enter 2 for Gaussian 3 point implementation : ')

choice = int(input())

a = float(input('Enter the lower limit : '))
b = float(input('Enter the upper limit : '))

c = float((b-a)/2)
d = float((a+b)/2)

if(choice == 1):
  # Gaussian 2-point quadrature
  z1 = -1/np.sqrt(3)
  z2 = 1/np.sqrt(3)
  w1 = 1
  w2 = 1
  I = c * (w1 * f(c * z1 + d) + w2 * f(c * z2 + d))
  print(f'The approximate integral using Gaussian 2-point quadrature is: {I}')

elif(choice == 2):
  # Gaussian 3-point quadrature
  z1 = -np.sqrt(3/5)
  z2 = 0
  z3 = np.sqrt(3/5)
  w1 = 5/9
  w2 = 8/9
  w3 = 5/9
  I = c * (w1 * f(c * z1 + d) + w2 * f(c * z2 + d) + w3 * f(c * z3 + d))
  print(f'The approximate integral using Gaussian 3-point quadrature is: {I}')

else:
  print('Invalid choice')