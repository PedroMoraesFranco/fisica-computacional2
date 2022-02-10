import numpy as np
import matplotlib.pyplot as plt

N = int(50)
h = 1/N   
y = float(1)
x = np.zeros(N+1)
ye = np.zeros(N+1)
yt = np.zeros(N+1)
ya = np.zeros(N+1)
ye[0] = y
yt[0] = y
ya[0] = y

for i in range(0,N):
    ye[i+1]=ye[i]+h*(-x[i]*ye[i])
    yt[i+1]=yt[i]+h*(-x[i]*yt[i])+0.5*h**2*yt[i]*(x[i]**2-1)
    ya[i+1] = np.exp(-x[i]**2/2) 
    x[i+1] = i*h

plt.figure(figsize = (12, 8))
plt.plot(x,ye, color = 'blue', label='Euler')
plt.plot(x,yt, color='red', label='Taylo 2a')
plt.scatter(x,ya, color='green', label='Analítico')
plt.title('Exercício 1')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.legend(loc='upper right')
plt.show()