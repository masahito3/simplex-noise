import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import *

plt.rcParams["text.usetex"] = True

def k(r):
    if np.sqrt(0.6)>r:
        return 8*(0.6-r**2)**4
    return 0

def cosd(d):
    return np.cos(np.radians(d))

def sind(d):
    return np.sin(np.radians(d))

o0=np.array([0,0])
o1=np.array([1,0])
o2=np.array([cosd(60),sind(60)])

v0=np.array([cosd(-30),sind(-30)])
v1=np.array([cosd(60),sind(60)])
v2=np.array([cosd(165),sind(165)])


def simplex2d(x,y):
    p0=np.array([x,y])-o0
    p1=np.array([x,y])-o1
    p2=np.array([x,y])-o2
    z0=np.dot(v0,p0)*k(np.linalg.norm(p0))
    z1=np.dot(v1,p1)*k(np.linalg.norm(p1))
    z2=np.dot(v2,p2)*k(np.linalg.norm(p2))
    return z0+z1+z2

fig,ax = plt.subplots(figsize=(5,5))
plt.subplots_adjust(left=0.30,right=0.75,bottom=0.25)

X=Y=np.arange(0,1.05,0.005)
X,Y=np.meshgrid(X,Y,indexing="ij") #x[nx,ny]
Z=np.empty(X.shape)
for nx in range(X.shape[0]):
    for ny in range(X.shape[1]):
        x=X[nx,ny]
        y=Y[nx,ny]
        if x>=0 and y<=np.sqrt(3)*x and y<=-np.sqrt(3)*(x-1):
            Z[nx,ny]=simplex2d(X[nx,ny],Y[nx,ny])
        else:
            Z[nx,ny]=0

print(np.max(Z),np.min(Z))

level=np.arange(-0.16,0.16,0.01)
CS=ax.contourf(X,Y,Z,level,cmap="bwr")

X=[o0[0],o1[0],o2[0]]
Y=[o0[1],o1[1],o2[1]]

U=[v0[0],v1[0],v2[0]]
V=[v0[1],v1[1],v2[1]]

P=[0.6,0.4]

PU=[P[0]-o0[0],P[0]-o1[0],P[0]-o2[0]]
PV=[P[1]-o0[1],P[1]-o1[1],P[1]-o2[1]]


#ax.plot(P[0],P[1],marker=".")

ax.quiver(X,Y,U,V,angles="xy",scale_units="xy",scale=1,clip_on=False,color="red",width=0.02)
#ax.quiver(X,Y,PU,PV,angles="xy",scale_units="xy",scale=1,clip_on=False,color=(0,0,0,0.3),width=0.02)


tri=plt.Polygon([o0,o1,o2],facecolor=(0,0,0,0),edgecolor=(0,0,0))
ax.add_patch(tri)


#ax.text(0.62,0.42,r"P",fontsize=20)
#ax.text(-0.12,-0.12,r"$O_0$",fontsize=20)
#ax.text(1.02,-0.12,r"$O_1$",fontsize=20)
#ax.text(cosd(60)+0.02,sind(60)+0.02,r"$O_2$",fontsize=20)

#ax.text(0.4,-0.4,r"$v_0$",fontsize=20,color="red")
#ax.text(1.13,0.5,r"$v_1$",fontsize=20,color="red")
#ax.text(-0.1,1.05,r"$v_2$",fontsize=20,color="red")





ax.axis("square")
ax.xaxis.set_major_locator(MultipleLocator(base=1))
ax.yaxis.set_major_locator(MultipleLocator(base=1))
ax.axis("off")
plt.show()
