import matplotlib.pyplot as plt
import numpy as np

#Dawid Syty 302923 zad 3 pierwsze zajecia

def fun(x):
   return x**2+5
	

x = np.linspace(-1,1,100)
y = fun(x)


fig, axs = plt.subplots(3)
fig.suptitle('Vertically stacked subplots')
axs[0].plot(x, y)
axs[0].set_title('-1 do 1')
axs[0].set_ylabel('y')
axs[0].set_xlabel('x')
axs[0].legend(['legenda'])
x = np.linspace(-6,6,100)
y = fun(x)
axs[1].plot(x, y)
axs[1].set_title('-1 do 1')
axs[1].set_xlabel('x')
axs[1].set_ylabel('y')
axs[1].legend(['legenda'])
x = np.linspace(0,5,100)
y = fun(x)
axs[2].plot(x,y)
axs[2].set_title('-1 do 1')
axs[2].set_xlabel('x')
axs[2].set_ylabel('y')
axs[2].legend(['legenda'])

plt.show()
