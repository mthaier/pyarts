##  Author      :   itsMohammedThaier
##  Description :   Flow field from a sin wave
##  Showcase    :   https://www.instagram.com/p/Cx_QH7UISjx/

import math
from random import random
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from noise import pnoise3

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
def EmmitParticle(x,y,z,c,iterations,speed):
    global ax

    xCur,yCur = x,y
    xPrev,yPrev = x,y
    for i in range(iterations):
        eff = pnoise3(xCur,yCur,z,octaves=1)
        angleEff = math.pi*2*eff
        xCur += math.cos(angleEff)*speed
        yCur += math.sin(angleEff)*speed

        #Particle reached the edge
        if math.fabs(xCur)>1 or math.fabs(yCur)>1:
            return 

        ax.plot((xPrev,xCur),(yPrev,yCur),c=c,lw=.3,alpha=.4,ls='-')
        xPrev,yPrev = xCur,yCur

z = random()*1000
t = np.linspace(-1,1,150)
y = np.sin(t*math.pi)
for pX,pY in zip(t,y):
    EmmitParticle(pX,pY,z,c2,60,.01)

#Rendering
plt.show()
