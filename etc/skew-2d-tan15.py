import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import *

def tand(d):
    return np.tan(np.radians(d))

A=-tand(15)
B=-tand(15)
T=np.array([[1,A],
            [B,1]])

def applyT(points):
    return np.array([np.matmul(T,p) for p in points])

S0=np.array(([0,0],[1,0],[1,1],[0,0],[0,1],[1,1]))

S1=applyT(S0)


fig,ax=plt.subplots(sharex=False,figsize=(5,3))
plt.subplots_adjust(wspace=0.6)

def polygon(ax,points,color):
    poly=plt.Polygon(points,facecolor=(0,0,0,0),edgecolor=color,closed=False)
    ax.add_patch(poly)

polygon(ax,S1,"red")

ax.text(0,0,"$(0,0)$",va="top",ha="right")
ax.text(S1[2,0]-0.05,S1[2,1]+0.05,r"$(1-\tan{15^\circ},\!-\tan{15^\circ}+1)$",va="bottom",ha="left")
ax.text(S1[1,0],S1[1,1],r"$(1,-\tan{15^\circ})$",va="top",ha="left")
ax.text(S1[4,0],S1[4,1],r"$(-\tan{15^\circ},1)$",va="bottom",ha="right")

ax.axis("square")
HI=1.8
LO=-1
line=plt.Polygon([[LO,0],[HI,0]],facecolor=(0,0,0,0),edgecolor=(0,0,0,0.5))
ax.add_patch(line)
line=plt.Polygon([[0,LO],[0,HI]],facecolor=(0,0,0,0),edgecolor=(0,0,0,0.5))
ax.add_patch(line)

ax.set(ylim=(LO,HI))
ax.set(xlim=(LO,HI))
OFF=0.2
ax.text(HI-OFF,0,"x",fontsize=20,va="bottom",ha="center")
ax.text(-OFF,HI-OFF,"y",fontsize=20,va="center",ha="center")
ax.set_xticks([])
ax.set_yticks([])

plt.savefig("skew-2d-tan15.svg")
plt.show()
