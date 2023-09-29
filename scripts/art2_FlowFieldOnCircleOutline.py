##  Author      :   itsMohammedThaier
##  Description :   Flow field on circle's outline
##  Showcase    :   https://www.instagram.com/p/Cxva8JAo_zE/?img_index=1

import math
from random import random
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from noise import pnoise3

#Data 1
c2 = (0,0,0)
c1 = (1,1,1)

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

#Emmit particles at circle outline
def circ(r,m,z,iterations):
    global c2
    for i in range(m):
        off = i/m
        angle = off*math.pi*2
        x = math.cos(angle)*r
        y = math.sin(angle)*r
        c = c2
        EmmitParticle(x,y,z,c,iterations,.01)

circ(.5,100,0,30)
#Rendering
plt.show()
