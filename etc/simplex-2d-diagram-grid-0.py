import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import *

root3=np.sqrt(3)
root6=np.sqrt(6)
cos15=np.cos(np.radians(15))
sin15=np.sin(np.radians(15))
cos45=np.cos(np.radians(45))
sin45=np.sin(np.radians(45))

o0=np.empty([11,11,2])
o1=np.empty([11,11,2])
o2=np.empty([11,11,2])

o0[0,5]=np.array([0,0])
o1[0,5]=np.array([root3,root3])
o2[0,5]=np.array([root6*cos15,-root6*sin15])

M1=np.array([[1,0, root6*cos15],[0,1,-root6*sin15],[0,0,1]])
M2=np.array([[1,0,-root6*cos15],[0,1, root6*sin15],[0,0,1]])
L1=np.array([[1,0, root6*cos45],[0,1, root6*sin45],[0,0,1]])

def m(m,v):
    return np.matmul(m,np.append(v,1))[:-1]

for i in range(1,6):
    o0[0,5+i]=m(M1,o0[0,5+i-1])
    o1[0,5+i]=m(M1,o1[0,5+i-1])
    o2[0,5+i]=m(M1,o2[0,5+i-1])
    o0[0,5-i]=m(M2,o0[0,5-i+1])
    o1[0,5-i]=m(M2,o1[0,5-i+1])
    o2[0,5-i]=m(M2,o2[0,5-i+1])

for i in range(1,11):
    for j in range(11):
        o0[i,j]=m(L1,o0[i-1,j])
        o1[i,j]=m(L1,o1[i-1,j])
        o2[i,j]=m(L1,o2[i-1,j])

fig,ax = plt.subplots(figsize=(5,5))

for i in range(11):
    for j in range(11):
        tri=plt.Polygon([o0[i,j],o1[i,j],o2[i,j]],facecolor=(0,0,0,0),edgecolor="red")
        ax.add_patch(tri)


ax.axis("square")
ax.grid()
ax.set(ylim=(-2,8))
ax.set(xlim=(-2,8))
ax.xaxis.set_major_locator(MultipleLocator(base=50))
ax.yaxis.set_major_locator(MultipleLocator(base=50))

plt.show()
