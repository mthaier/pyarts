##  Author      :   itsMohammedThaier
##  Description :   Random lines within a circle
##  Showcase    :   https://www.instagram.com/p/CyB-qn1o7Uy/

import math
from random import random
import matplotlib as mpl
import matplotlib.pyplot as plt

#Data 1
c1 = (0,0,0)
c2 = (1,1,1)

#Customization
mpl.rcParams['savefig.facecolor'] = c1
mpl.rcParams['axes.facecolor'] = c1

#Figure setup
fig,ax = plt.subplots(figsize=(5,5))
ax.set_xlim(-1,1)
ax.set_ylim(-1,1)
ax.axis("off")

#Helpers
def Circ(n):
    global ax,c2

    xPrev,yPrev=0,0
    for i in range(n):
        fac = random()
        x = math.cos(fac*math.pi*2)
        y = math.sin(fac*math.pi*2)
        ax.plot((xPrev,x),(yPrev,y),c=c2,lw=.3,alpha=.2)
        xPrev,yPrev=x,y

Circ(500)
#Rendering
plt.show()
