import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import *

N=2
F=(np.sqrt(N+1)-1)/N
G=(1-1/np.sqrt(N+1))/N

T=np.array([[1+F,  F],
            [  F,1+F]])

S=np.array([[1-G, -G],
            [ -G,1-G]])

SQUARE=np.array(([0,0],[1,0],[1,1],[0,0],[0,1],[1,1]))

o=np.empty([10,10,6,2]) #indexing is o[iy,ix][p][x,y]
for i in range(10):
    for j in range(10):
        o[i,j]=SQUARE+[j,i]

s=np.empty([10,10,6,2])
for i in range(10):
    for j in range(10):
        for p in range(6):
            s[i,j,p]=np.matmul(S,o[i,j,p])

fig,ax=plt.subplots(nrows=1,ncols=2,sharex=False,figsize=(8,4))
plt.subplots_adjust(wspace=0.6)
ax0=ax[0]
ax1=ax[1]

#for i in range(5):
#    for j in range(5):
#        #tri=plt.Polygon(o[i,j],facecolor=(0,0,0,0),edgecolor=(0,0,0,1),closed=False)
#        #ax0.add_patch(tri)
#        tri=plt.Polygon(s[i,j],facecolor=(0,0,0,0),edgecolor="red",closed=False)
#        ax0.add_patch(tri)


P=np.array([2.2,1.8])
ax0.plot(*P,".")
ax0.text(*(P+[0.2,0]),"P(x,y)",va="bottom",ha="left",fontsize=16)

Q=np.matmul(T,P)
ax1.plot(*Q,".")
ax1.text(*(Q+[0.4,0]),"P'(x',y')",va="center",ha="left",fontsize=16)


def add_poly(ax,points,color,fill=(0,0,0,0)):
    poly=plt.Polygon(points,facecolor=fill,edgecolor=color,closed=False)
    ax.add_patch(poly)

add_poly(ax0,s[3,3],"red")
add_poly(ax0,s[3,3][0:3],"red",(0,0,0,0.2))
add_poly(ax1,o[3,3],"black")
add_poly(ax1,o[3,3][0:3],"black",(0,0,0,0.2))

ax1.text(*o[3,3][0],"$(x'_0,y'_0)$",va="top",ha="right")
ax1.text(*o[3,3][1],"$(x'_1,y'_1)$",va="top",ha="left")
ax1.text(*o[3,3][2],"$(x'_2,y'_2)$",va="bottom",ha="left")

ax0.text(*s[3,3][0],"$(x_0,y_0)$",va="top",ha="right")
ax0.text(*s[3,3][1],"$(x_1,y_1)$",va="top",ha="left")
ax0.text(*s[3,3][2],"$(x_2,y_2)$",va="bottom",ha="left")



def draw_axes(ax):
    ax.axis("square")
    HI=5
    LO=-0.8
    OFF=0.1
    ax.set(ylim=(LO,HI))
    ax.set(xlim=(LO,HI))

    line=plt.Polygon([[LO,0],[HI,0]],facecolor=(0,0,0,0),edgecolor=(0,0,0,0.5))
    ax.add_patch(line)
    line=plt.Polygon([[0,LO],[0,HI]],facecolor=(0,0,0,0),edgecolor=(0,0,0,0.5))
    ax.add_patch(line)

    for i in range(0,HI):
        ax.text(i,-OFF,i,va="top",ha="center")
        ax.text(-OFF,i,i,va="center",ha="right")
    ax.text(HI,0,"x",fontsize=16,va="top",ha="right")
    ax.text(0,HI,"y",fontsize=16,va="top",ha="right")
    ax.set_xticks([])
    ax.set_yticks([])

draw_axes(ax0)
draw_axes(ax1)

#fig.delaxes(ax1)

#plt.savefig("P-2d.svg")
plt.show()
