import numpy as np

def f(x):
    return 1/(1+(x*x))
    
a = float(input('Enter the lower limit for integration : '))
b = float(input('Enter the upper limit for integration : '))
n = int(input('Enter the number of segments : '))

while(n%2 != 0):
    n = int(input('Enter the number of segments : '))

h = (b - a)/n

x_values = np.empty(n+1)
y_values = np.empty(n+1)

for i in range(n+1):
    x_values[i] = a + i*h
    y_values[i] = float(f(x_values[i]))
                                                                                        
I1 = y_values[0]+y_values[n]
I2 = 0
for i in range(1,n):
    if(i%2 == 0):
        I2 += 2*y_values[i]
    else:
        I2 += 4*y_values[i]

I = round(((I1 + I2)/3),3)

print('The integrated value using 1/8 Simpsons method is : ',I)