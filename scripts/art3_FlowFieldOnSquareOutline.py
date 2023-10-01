##  Author      :   itsMohammedThaier
##  Description :   Flow field on square's outline
##  Showcase    :   https://www.instagram.com/p/Cx3tPB_o6td/

import math
from random import random
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from noise import pnoise3

#Data 1
c1 = (0,0,0)
c2 = (1,0,0)

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

def LineParticles(x1,y1,x2,y2,z,n):
    global c2

    xDiff = x2-x1
    yDiff = y2-y1
    for i in range(n):
        off = i/n
        x = x1+xDiff*off
        y = y1+yDiff*off
        EmmitParticle(x,y,z,c2,30,.01)


z = random()*1000
LineParticles(-.5,.5,.5,.5,z,40)
LineParticles(-.5,-.5,.5,-.5,z,40)
LineParticles(-.5,.5,-.5,-.5,z,40)
LineParticles(.5,.5,.5,-.5,z,40)
#Rendering
num = int(random()*1000)
plt.savefig(f'x{num}.jpg',dpi=1000)

