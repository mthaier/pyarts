##  Author      :   itsMohammedThaier
##  Description :   A simple flow field implementation
##  Showcase    :   https://www.instagram.com/p/CxvITn-IjGa/?img_index=1
##  Notes       :   It's not identical for the showcase, it's edited a little for a more general look


import math
from random import random
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from noise import pnoise3

#Data 1
c1 = (1,1,1)
c2 = (0,0,0)

#Figure setup
mpl.rcParams['savefig.facecolor'] = c1
mpl.rcParams['axes.facecolor'] = c1
fig,ax = plt.subplots(figsize=(5,5))
ax.set_xlim(-1,1)
ax.set_ylim(-1,1)
ax.axis("off")

#Helpers
def EmmitParticle(x,y,z,c,iterations,speed):
    global ax
    xCur,yCur = x,y
    xPrev,yPrev = x,y
    for i in range(iterations):
        eff = pnoise3(xCur,yCur,z,octaves=1)
        angleEff = math.pi*2*eff
        xCur += math.cos(angleEff)*speed
        yCur += math.sin(angleEff)*speed
        ax.plot((xPrev,xCur),(yPrev,yCur),c=c,lw=.3,alpha=.3,ls='-')
        xPrev,yPrev = xCur,yCur

        #Particle reached the edge
        if math.fabs(xCur)>1 or math.fabs(yCur)>1:
            return 

#Drawing Flow field
n = 100
z = random()*1000
for i in range(n):
    x = (random()-.5)*2
    y = (random()-.5)*2
    c = c2
    EmmitParticle(x,y,z,c,1200,.01)

#Rendering
plt.show()
