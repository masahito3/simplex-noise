import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import *

#np.set_printoptions(precision=4)

N=2
F=(np.sqrt(N+1)-1)/N
T=np.array([[1+F,  F],
            [  F,1+F]])

G=(1-1/np.sqrt(N+1))/N
S=np.array([[1-G, -G],
            [ -G,1-G]])

def HASH(n,m):
    return (b(n,m,0)+b(m,n,1)+b(n,m,2)+b(m,n,3)+
            b(n,m,4)+b(m,n,5)+b(n,m,6)+b(m,n,7))

pattern=[0,3,15,10]

def b(n,m,B):
    id=2*bit(n,B)+bit(m,B)
    return pattern[id]

def bit(n,B):
    return n>>B & 1

def k(r2): #r2 means r squared
    if 0.6>r2:
        return 8*(0.6-r2)**4
    return 0

def calc(n,m,xin,yin):
    xn,ym=np.matmul(S,(n,m))
    x,y=xin-xn,yin-ym
    h=HASH(n,m)
    bit(h,0)==0 and (p:=x,q:=y) or (p:=y,q:=x)
    bit(h,1)==1 and (q:=0)
    bit(h,2)==0 and (q:=-q)
    bit(h,3)==0 and (p:=-p)
    return (p+q)*k(x**2+y**2)

#reference
#g=((-1,-1),(-1,-1),(-1,0),(0,-1),
#   (-1,1),(1,-1),(-1,0),(0,-1),
#   (1,-1),(-1,1),(1,0),(0,1),
#   (1,1),(1,1),(1,0),(0,1))
#rng = np.random.default_rng()
#random_table=rng.integers(0,16,(256,256))
#def calc_reference(n,m,xin,yin):
#    xn,ym=np.matmul(S,(n,m))
#    x,y=xin-xn,yin-ym
#    grad=g[random_table[m,n]]
#    return np.dot(grad,(x,y))*k(x**2+y**2)
#calc=calc_reference

def simplex2d(xin,yin):
    xp,yp=np.matmul(T,(xin,yin))
    n0,m0=int(xp),int(yp)
    yp-m0 > xp-n0 and (m1:=m0+1,n1:=n0) or (m1:=m0,n1:=n0+1)
    n2,m2=n0+1,m0+1
    return calc(n0,m0,xin,yin)+calc(n1,m1,xin,yin)+calc(n2,m2,xin,yin)

if __name__=="__main__":
    def ij(m,n):
        for i in range(m):
            for j in range(n):
                yield i,j
    #make plot data
    HI=3
    X=Y=np.arange(0,HI+0.05,0.05)
    X,Y=np.meshgrid(X,Y,indexing="ij") #x[nx,ny]
    Z=np.empty(X.shape)
    for nx,ny in ij(*X.shape):
        Z[nx,ny]=simplex2d(X[nx,ny],Y[nx,ny])
    #print(np.max(Z),np.min(Z))
    fig, ax = plt.subplots(figsize=(6,6),layout="constrained")
    level=np.arange(-0.31,0.31,0.01)
    CS=ax.contourf(X,Y,Z,level,cmap="bwr")
    cbar=fig.colorbar(CS,shrink=0.75)
    cbar.set_ticks([-0.3,0.0,0.3])
    ax.axis("square")
    def show_grid():
        SQUARE=np.array(([0,0],[1,0],[1,1],[0,0],[0,1],[1,1]))
        M=20
        s=np.zeros([M,M,6,2])
        for i,j in ij(M,M):
            s[i,j]=[np.matmul(S,p) for p in SQUARE+(j,i)]
            options={"facecolor":(0,0,0,0),
                     "edgecolor":(1,0,0,0.3),
                     "closed":False}
            poly=plt.Polygon(s[i,j],**options)
            ax.add_patch(poly)
    show_grid()
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.xaxis.set_major_locator(MultipleLocator(base=1.0))
    ax.yaxis.set_major_locator(MultipleLocator(base=1.0))
    #plt.savefig("simplex2d.svg")
    plt.show()
