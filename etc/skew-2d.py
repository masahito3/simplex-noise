import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import *

A=-0.3
B=-0.3
T=np.array([[1,A],
            [B,1]])

def applyT(points):
    return np.array([np.matmul(T,p) for p in points])

S0=np.array(([0,0],[1,0],[1,1],[0,1]))
F0=np.array([[0,0],[1,0],[1,3],[4,3],[4,4],[1,4],[1,6],[5,6],[5,7],[0,7]])
F0=(F0+np.array([3,1]))*0.1

S1=applyT(S0)
F1=applyT(F0)


fig,ax=plt.subplots(nrows=1,ncols=2,sharex=False,figsize=(6,3))
plt.subplots_adjust(wspace=0.6)
ax0=ax[0]
ax1=ax[1]

def polygon(ax,points,color):
    poly=plt.Polygon(points,facecolor=(0,0,0,0),edgecolor=color)
    ax.add_patch(poly)

polygon(ax0,S0,"black")
polygon(ax0,F0,"black")
polygon(ax1,S1,"red")
polygon(ax1,F1,"red")

ax0.text(0,0,"$(0,0)$",va="top",ha="right")
ax0.text(1,1,"$(1,1)$",va="bottom",ha="left")
r3=np.sqrt(3)
ax1.text(0,0,"$(0,0)$",va="top",ha="right")
ax1.text(S1[2,0],S1[2,1],r"$(1+a,b+1)$",va="bottom",ha="left")
ax1.text(S1[1,0],S1[1,1],r"$(1,b)$",va="top",ha="left")
ax1.text(S1[3,0],S1[3,1],r"$(a,1)$",va="bottom",ha="right")

for i in range(2):
    ax[i].axis("square")
    #ax[i].grid()
    HI=1.8
    LO=-1
    line=plt.Polygon([[LO,0],[HI,0]],facecolor=(0,0,0,0),edgecolor=(0,0,0,0.5))
    ax[i].add_patch(line)
    line=plt.Polygon([[0,LO],[0,HI]],facecolor=(0,0,0,0),edgecolor=(0,0,0,0.5))
    ax[i].add_patch(line)

    ax[i].set(ylim=(LO,HI))
    ax[i].set(xlim=(LO,HI))
    OFF=0.2
    ax[i].text(HI-OFF,0,"x",fontsize=20,va="bottom",ha="center")
    ax[i].text(-OFF,HI-OFF,"y",fontsize=20,va="center",ha="center")
    ax[i].set_xticks([])
    ax[i].set_yticks([])

plt.savefig("skew-2d.svg")
plt.show()
