import numpy as np
import matplotlib.pyplot as plt

def f(dados):
    theta = dados[0]
    omega = dados[1]
    ftheta = omega
    fomega = - (g /l)*np.sin(theta)
    return np.array([ftheta, fomega])
    


g = 9.8        
l=1         
a = 0
b = 10
N = 2000
h = (b - a) / N
t=np.arange(a, b, h)



theta1=np.pi/2
omega1=0
dados1 = np.array([theta1, omega1])
theta1rk = []
omega1rk = []
for i in range(0,N):
    theta1rk.append(dados1[0])
    omega1rk.append(dados1[1])
    k1i = h * f(dados1)
    k2i = h * f(dados1 + 0.5 * k1i)
    dados1 += (k1i + 2 * k2i ) / 6

###############################################################
theta2=np.pi*0.9
omega2=0
dados2 = np.array([theta2, omega2])
theta2rk = []
omega2rk = []
for j in range(0,N):
    theta2rk.append(dados1[0])
    omega2rk.append(dados1[1])
    k1j = h * f(dados2)
    k2j = h * f(dados2 + 0.5 * k1j)
    dados2 += (k1j + 2 * k2j ) / 6
      
plt.figure(figsize = (12, 8))
plt.plot(t,theta1rk, color = 'blue', label='Theta(0)=pi/2')
plt.plot(t,theta2rk,color = 'red', label='Theta(0)=0.9pi')
plt.title('Exercício 2')
plt.xlabel('t')
plt.ylabel('omega(t)')
plt.grid()
plt.legend(loc='upper right')
plt.show()
