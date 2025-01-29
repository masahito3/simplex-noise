import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patheffects as patheffects
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
 
P=np.array([1.5,2])
def draw_P():
    ax0.plot(*P,".")
    ax0.text(*(P),"P",va="bottom",ha="left",fontsize=16)
draw_P()

def draw_U():
    X,Y=s[3,2][0]
    U,V=P[0]-X,P[1]-Y
    ax0.quiver(X,Y,U,V,angles="xy",scale_units="xy",scale=1,clip_on=False,color=(0,0,0,0.3),width=0.02)
    ax0.text(X+0.3,Y+0.05,r"$\vec u$",va="bottom",ha="right",fontsize=16)
draw_U()

def draw_V():
    X,Y=s[3,2][0]
    U,V=1,-1
    ax0.quiver(X,Y,U,V,angles="xy",scale_units="xy",scale=1,clip_on=False,hatch="///",color="red",edgecolor="white",width=0.02)
    ax0.text(X+0.5,Y-0.5,r"$\vec v$",va="bottom",ha="left",fontsize=16)
draw_V()

def draw_Q():
    Q=np.matmul(T,P)
    ax1.plot(*Q,".")
    ax1.text(*(Q+[0.4,0]),"P'(x',y')",va="center",ha="left",fontsize=16)
#draw_Q()

def add_poly(ax,points,color,fill=(0,0,0,0),closed=False):
    poly=plt.Polygon(points,facecolor=fill,edgecolor=color,closed=closed)
    ax.add_patch(poly)

#for i in range(4):
#    for j in range(4):
#        add_poly(ax0,s[i,j],"red")
#        add_poly(ax1,o[i,j],"black")


#add_poly(ax0,s[3,3],"red")
add_poly(ax0,s[3,2][0:3],"red",(0,0,0,0),True)
#add_poly(ax1,o[3,3],"black")
#add_poly(ax1,o[3,3][0:3],"black",(0,0,0,0.2))

#ax1.text(*o[3,3][0],"$(x'_0,y'_0)$",va="top",ha="right")
#ax1.text(*o[3,3][1],"$(x'_1,y'_0)$",va="top",ha="left")
#ax1.text(*o[3,3][2],"$(x'_1,y'_1)$",va="bottom",ha="left")

#ax0.text(*s[3,3][0],"$(x_0,y_0)$",va="top",ha="right")
#ax0.text(*s[3,3][1],"$(x_1,y_1)$",va="top",ha="left")
#ax0.text(*s[3,3][2],"$(x_2,y_2)$",va="bottom",ha="left")

effect=patheffects.withStroke(linewidth=3, foreground='white', capstyle="round")
def draw_index(i,j,text="none",fontsize="none"):
    text=text
    if text=="none":
        text="{0},{1}".format(i,j)
    ax0.text(*s[i,j][0],text,va="top",ha="center",path_effects=[effect],fontsize=fontsize)
    ax1.text(*o[i,j][0],text,va="top",ha="center",path_effects=[effect],fontsize=fontsize)

def draw_indices():
    for i in range(5):
        for j in range(5):
            draw_index(i,j)

#draw_indices()
draw_index(3,2,"m,n",16)

def draw_axes(ax):
    ax.axis("square")
    CE=np.array((1.5,2))
    WH=np.array((1.5,1.5))
    LO=CE-WH*0.5
    HI=CE+WH*0.5
    #P=np.array([2.2,1.8])

    OFF=0.1
    ax.set(xlim=(LO[0],HI[0]))
    ax.set(ylim=(LO[1],HI[1]))

    def draw_axes_lines():
        line=plt.Polygon([[LO[0],0],[HI[0],0]],facecolor=(0,0,0,0),edgecolor=(0,0,0,0.5))
        ax.add_patch(line)
        line=plt.Polygon([[0,LO[0]],[0,HI[0]]],facecolor=(0,0,0,0),edgecolor=(0,0,0,0.5))
        ax.add_patch(line)

        for i in range(0,int(np.max(HI))):
            ax.text(i,-OFF,i,va="top",ha="center")
            ax.text(-OFF,i,i,va="center",ha="right")
        ax.text(HI[0],0,"x",fontsize=16,va="top",ha="right")
        ax.text(0,HI[1],"y",fontsize=16,va="top",ha="right")
    draw_axes_lines()
    ax.set_xticks([])
    ax.set_yticks([])

draw_axes(ax0)
draw_axes(ax1)

for o in fig.findobj():
    o.set_clip_on(False)


fig.delaxes(ax1)
ax0.axis("off")
plt.savefig("random-2d.svg")
plt.show()
