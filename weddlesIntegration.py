import numpy as np

def f(x):
    return 1/(1+(x*x))
    
a = float(input('Enter the lower limit for integration : '))
b = float(input('Enter the upper limit for integration : '))
n = int(input('Enter the number of segments : '))

while(n%6 != 0):
    n = int(input('Enter the number of segments : '))

h = (b - a)/n
c = int(n/6)

x_values = np.empty(n+1)
y_values = np.empty(n+1)

for i in range(n+1):
    x_values[i] = a + i*h
    y_values[i] = float(f(x_values[i]))

I = 0                                                                                       
for i in range(0,c):
    I = y_values[i*6]+5*y_values[i*6+1]+y_values[i*6+2]+6*y_values[i*6+3]+y_values[i*6+4]+5*y_values[i*6+5]+y_values[i*6+6]

I = round((3*h*I/10),3)

print('The integrated value using Booles method is : ',I)