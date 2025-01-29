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

o0=np.empty([10,10,2])#indexing is o0[iy,ix][x,y]
o1=np.empty([10,10,2])
o2=np.empty([10,10,2])
o3=np.empty([10,10,2])

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

for i in range(10):
    for j in range(10):
        o0[i,j]=np.matmul(T,s0[i,j])
        o1[i,j]=np.matmul(T,s1[i,j])
        o2[i,j]=np.matmul(T,s2[i,j])
        o3[i,j]=np.matmul(T,s3[i,j])


fig,ax=plt.subplots(nrows=1,ncols=2,sharex=False,figsize=(6,3))
plt.subplots_adjust(wspace=0.6)
#plt.subplots_adjust(left=0.05, right=0.995, bottom=0.05, top=0.995)

ax0=ax[0]
ax1=ax[1]
clear=(0,0,0,0)
for i in range(5):
    for j in range(5):
        tri=plt.Polygon([o0[i,j],o1[i,j],o3[i,j]],facecolor=clear,edgecolor="black")
        ax0.add_patch(tri)
        tri=plt.Polygon([o0[i,j],o2[i,j],o3[i,j]],facecolor=clear,edgecolor="black")
        ax0.add_patch(tri)
        tri=plt.Polygon([s0[i,j],s1[i,j],s3[i,j]],facecolor=clear,edgecolor="red")
        ax1.add_patch(tri)
        tri=plt.Polygon([s0[i,j],s2[i,j],s3[i,j]],facecolor=clear,edgecolor="red")
        ax1.add_patch(tri)

i=2
j=3
tri=plt.Polygon([o0[i,j],o1[i,j],o3[i,j]],facecolor=(0,0,0,0.5),edgecolor="black")
ax0.add_patch(tri)
tri=plt.Polygon([s0[i,j],s1[i,j],s3[i,j]],facecolor=(0,0,0,0.5),edgecolor="red")
ax1.add_patch(tri)

        
ax0.text(0,0,"$(0,0)$",va="top",ha="right")
#ax0.text(1,1,"$(1,1)$",va="bottom",ha="left")
#ax0.text(1,0,"$(1,0)$",va="top",ha="left")
#ax0.text(0,1,"$(0,1)$",va="bottom",ha="right")
r3=np.sqrt(3)
ax1.text(0,0,"$(0,0)$",va="top",ha="right")
#ax1.text(1/r3,1/r3,r"$\left(\dfrac{1}{\sqrt{3}},\dfrac{1}{\sqrt{3}}\right)$",va="bottom",ha="left")
#ax1.text((r3+3)/6,(r3-3)/6,r"$\left(\dfrac{\sqrt{3}+3}{6},\dfrac{\sqrt{3}-3}{6}\right)$",va="top",ha="left")
#ax1.text((r3-3)/6,(r3+3)/6,r"$\left(\dfrac{\sqrt{3}-3}{6},\dfrac{\sqrt{3}+3}{6}\right)$",va="bottom",ha="right")

for i in range(2):
    ax[i].axis("square")
    #ax[i].grid()
    HI=6
    LO=-2
    line=plt.Polygon([[LO,0],[HI,0]],facecolor=(0,0,0,0),edgecolor=(0,0,0,0.5))
    ax[i].add_patch(line)
    line=plt.Polygon([[0,LO],[0,HI]],facecolor=(0,0,0,0),edgecolor=(0,0,0,0.5))
    ax[i].add_patch(line)

    ax[i].set(ylim=(LO,HI))
    ax[i].set(xlim=(LO,HI))
    #ax[i].text(0,-0.15,0,va="center",ha="center")
    #ax[i].text(-0.15,0,0,va="center",ha="center")
    OFF=0.5
    ax[i].text(HI-OFF,0,"x",fontsize=20,va="bottom",ha="center")
    ax[i].text(-OFF,HI-OFF,"y",fontsize=20,va="center",ha="center")
    ax[i].set_xticks([])
    ax[i].set_yticks([])

#plt.savefig("simplex-grid-2d-compare.svg")
plt.show()
