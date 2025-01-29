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

o0=np.empty([10,10,2])
o1=np.empty([10,10,2])
o2=np.empty([10,10,2])
o3=np.empty([10,10,2])

#indexing is o0[iy,ix][x,y]

for i in range(10):
    for j in range(10):
        o0[i,j]=np.array([j  ,i  ])
        o1[i,j]=np.array([j+1,i  ])
        o2[i,j]=np.array([j  ,i+1])
        o3[i,j]=np.array([j+1,i+1])

s0=np.empty([10,10,2])
s1=np.empty([10,10,2])
s2=np.empty([10,10,2])
s3=np.empty([10,10,2])

for i in range(10):
    for j in range(10):
        s0[i,j]=np.matmul(S,o0[i,j])
        s1[i,j]=np.matmul(S,o1[i,j])
        s2[i,j]=np.matmul(S,o2[i,j])
        s3[i,j]=np.matmul(S,o3[i,j])

fig,ax = plt.subplots(figsize=(5,5))

for i in range(5):
    for j in range(5):
        tri=plt.Polygon([o0[i,j],o1[i,j],o3[i,j]],facecolor=(0,0,0,0),edgecolor=(0,0,0,1))
        ax.add_patch(tri)
        tri=plt.Polygon([o0[i,j],o2[i,j],o3[i,j]],facecolor=(0,0,0,0),edgecolor=(0,0,0,1))
        ax.add_patch(tri)
        #tri=plt.Polygon([s0[i,j],s1[i,j],s3[i,j]],facecolor=(0,0,0,0),edgecolor="red")
        #ax.add_patch(tri)
        #tri=plt.Polygon([s0[i,j],s2[i,j],s3[i,j]],facecolor=(0,0,0,0),edgecolor="red")
        #ax.add_patch(tri)

ax.axis("square")
HI=6
LO=-1
OFF=0.2
ax.set(ylim=(LO,HI))
ax.set(xlim=(LO,HI))

line=plt.Polygon([[LO,0],[HI,0]],facecolor=(0,0,0,0),edgecolor=(0,0,0,0.5))
ax.add_patch(line)
line=plt.Polygon([[0,LO],[0,HI]],facecolor=(0,0,0,0),edgecolor=(0,0,0,0.5))
ax.add_patch(line)

for i in range(0,HI):
    ax.text(i,-OFF,i,va="top",ha="center")
    ax.text(-OFF,i,i,va="center",ha="right")
ax.text(HI-OFF,0,"x",fontsize=20,va="bottom",ha="center")
ax.text(-OFF,HI-OFF,"y",fontsize=20,va="top",ha="center")
ax.set_xticks([])
ax.set_yticks([])

plt.savefig("simplex-grid-2d.svg")
plt.show()
