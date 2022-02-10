import numpy as np
import matplotlib.pyplot as plt

def edo_1(x,y):
    q=0.5
    omegad=2./3.
    Fd=1.2
    g=9.8
    l=9.8
    f=np.zeros(2)
    f[0]=y[1]
    f[1]=-g/l*np.sin(y[0])-q*y[1]+Fd*np.sin(omegad*x)
    return f

def rk4_1(x,y,h):
    k1=edo_1(x,y)
    k2=edo_1(x+h/2.,y+h*k1/2.)
    k3=edo_1(x+h/2.,y+h*k2/2.)
    k4=edo_1(x+h,y+h*k3)
    y=(k1+2*k2+2*k3+k4)/6
    return y


def edo_2(x,y):
    q=0.5
    omegad=2./3.
    Fd=0.5
    g=9.8
    l=9.8
    f=np.zeros(2)
    f[0]=y[1]
    f[1]=-g/l*np.sin(y[0])-q*y[1]+Fd*np.sin(omegad*x)
    return f

def rk4_2(x,y,h):
    k1=edo_2(x,y)
    k2=edo_2(x+h/2.,y+h*k1/2.)
    k3=edo_2(x+h/2.,y+h*k2/2.)
    k4=edo_2(x+h,y+h*k3)
    y=(k1+2*k2+2*k3+k4)/6
    return y


dt=0.04
tf=60
N=int(tf/dt)
y_1=np.zeros(2)
y_1[0]=0.2 #condição inicial do ângulo
# a condição inicial da velocidade é zero
t=np.zeros(N+1) # tempo inicial é zero também
theta_1=np.zeros(N+1)
omega_1=np.zeros(N+1)
theta_1[0]=y_1[0]
omega_1[0]=y_1[1]
tempo=0.
for k in range(N):
    y=rk4_1(tempo,y_1,dt)
    t[k+1]=t[k]+dt
    tempo+=dt
    theta_1[k+1]=y[0]
    omega_1[k+1]=y[1]

y_2=np.zeros(2)
y_2[0]=0.201 #condição inicial do ângulo
theta_2=np.zeros(N+1)
omega_2=np.zeros(N+1)
theta_2[0]=y_2[0]
omega_2[0]=y_2[1]
tempo=0.
for i in range(N):
    y=rk4_2(tempo,y_2,dt)
    t[i+1]=t[i]+dt
    tempo+=dt
    theta_2[i+1]=y[0]
    omega_2[i+1]=y[1]

Delta_theta = np.abs(theta_1-theta_2)

plt.figure(figsize = (12, 8))
plt.yscale("log")
plt.plot(t,Delta_theta, color = 'k')
plt.title('Exercício 3')
plt.xlabel('t')
plt.ylabel('Delta_theta(t)')
plt.grid()
plt.legend(loc='upper right')
plt.show()    
    






