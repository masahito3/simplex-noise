import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import *

np.set_printoptions(precision=4)

CANDIDATES0=np.array([
[ 0,  3, 15, 10,],
#[0, 4, 7, 5,],
#[ 0,  4, 15, 13,],
#[0, 7, 4, 5,],
#[ 0,  9, 12, 11,],
#[ 0, 12,  9, 11,],
##[ 0, 15,  3, 10,],
#[ 0, 15,  4, 13,],
#[ 1,  2, 14,  7,],
[ 1,  6, 10,  7,],
##[ 1, 10,  6,  7,],
##[ 1, 14,  2,  7,],
[ 2,  1,  5, 12,],
#[ 2,  1,  6, 15,],
##[ 2,  5,  1, 12,],
#[ 2,  6,  1, 15,],
#[2, 6, 9, 7,],
#[2, 9, 6, 7,],
#[ 2, 11, 14, 13,],
#[ 2, 14, 11, 13,],
#[3, 0, 4, 9,],
##[3, 4, 0, 9,],
[ 3,  8, 12,  9,],
##[ 3, 12,  8,  9,],
#[ 4,  0, 13, 15,],
#[ 4,  3,  7, 14,],
#[4, 3, 8, 1,],
##[ 4,  7,  3, 14,],
#[4, 8, 3, 1,],
#[ 4,  8, 11,  9,],
#[ 4, 11,  8,  9,],
#[ 4, 13,  0, 15,],
#[ 5,  2,  6, 11,],
#[ 5,  6,  2, 11,],
#[ 5, 10, 14, 11,],
#[ 5, 14, 10, 11,],
#[ 6,  2, 15,  1,],
[6, 5, 9, 0,],
#[ 6,  5, 10,  3,],
##[6, 9, 5, 0,],
#[ 6, 10,  5,  3,],
#[ 6, 10, 13, 11,],
#[ 6, 13, 10, 11,],
#[ 6, 15,  2,  1,],
[ 7,  0, 12, 13,],
#[ 7,  4,  8, 13,],
##[ 7,  8,  4, 13,],
##[ 7, 12,  0, 13,],
#[8, 1, 4, 3,],
#[8, 4, 1, 3,],
[ 8,  7, 11,  2,],
#[ 8,  7, 12,  5,],
##[ 8, 11,  7,  2,],
#[ 8, 12,  7,  5,],
#[ 8, 12, 15, 13,],
#[ 8, 15, 12, 13,],
#[ 9,  2, 14, 15,],
#[ 9,  6, 10, 15,],
#[ 9, 10,  6, 15,],
#[ 9, 14,  2, 15,],
#[10,  1, 14, 15,],
#[10,  3,  6,  5,],
#[10,  6,  3,  5,],
#[10,  9, 13,  4,],
#[10,  9, 14,  7,],
#[10, 13,  9,  4,],
#[10, 14,  1, 15,],
#[10, 14,  9,  7,],
#[11,  0,  4,  1,],
#[11,  4,  0,  1,],
#[11,  8, 12,  1,],
#[11, 12,  8,  1,],
#[12,  0,  3,  1,],
#[12,  0, 11,  9,],
#[12,  3,  0,  1,],
#[12,  5,  8,  7,],
#[12,  8,  5,  7,],
#[12, 11,  0,  9,],
[12, 11, 15,  6,],
##[12, 15, 11,  6,],
#[13,  2,  6,  3,],
#[13,  6,  2,  3,],
#[13, 10, 14,  3,],
#[13, 14, 10,  3,],
#[14,  1, 13,  8,],
#[14,  2,  5,  3,],
#[14,  2, 13, 11,],
#[14,  5,  2,  3,],
#[14,  7, 10,  9,],
#[14, 10,  7,  9,],
#[14, 13,  1,  8,],
#[14, 13,  2, 11,],
#[15,  0, 12,  5,],
#[15,  4,  8,  5,],
#[15,  8,  4,  5,],
#[15, 12,  0,  5,]
])

#CANDIDATES=[[0x5,0x8,0x2,0xc],
#            [0,10,12,7],
#            [14,13,2,11],
#            [2,1,5,12], #Good
#            [0,3,15,10], #Good, this is last value
#            [7,0,12,13], #Good
#            ]

CANDIDATES=np.array([
    [0,3,15,10]])

def HASH(n,m):
    return (b(n,m,0)+b(m,n,1)+b(n,m,2)+b(m,n,3)+
            b(n,m,4)+b(m,n,5)+b(n,m,6)+b(m,n,7))

rng = np.random.default_rng()
random_table=rng.integers(0,16,(256,256))
def HASH_reference(n,m):
    return random_table[m,n]

#pattern=[0x15,0x38,0x32,0x2c]
#pattern=[0x5,0x8,0x2,0xc]
#pattern=[0x15,0x38,0x32,0x2c,0x0d,0x13,0x07,0x2a ]

def b(n,m,B):
    id=2*bit(n,B)+bit(m,B)
    return pattern[id]

def bit(n,B):
    return n>>B & 1

HI=80

def create_XYZ():
    global X,Y,Z
    X=Y=np.arange(0,HI,1)
    X,Y=np.meshgrid(X,Y,indexing="ij") #x[nx,ny]
    Z=np.empty(X.shape)
create_XYZ()
    
def get_data(ref=False):
    global Z
    if ref:
        hash=HASH_reference
    else:
        hash=HASH
    for nx in range(X.shape[0]):
        for ny in range(X.shape[1]):
            Z[nx,ny]=hash(nx,ny) & 0b1111

def KAI(d,E):
    return sum(map(lambda s: (np.sum(d==s)-E)**2/E,range(16)))

def TEST(data):
    d=np.ravel(data)
    K0=KAI(d,d.size/16)

    si=data.shape[0]

    def ij():
        for i in range(1,si-1):
            for j in range(1,si-1):
                yield i,j

    sm=lambda i,j: np.abs(data[i+1,j+1]-data[i,j])+np.abs(data[i-1,j-1]-data[i,j])
    s=sum(sm(i,j) for i,j in ij())
    K1=s/(si-1)**2

    sm=lambda i,j: np.abs(data[i-1,j+1]-data[i,j])+np.abs(data[i+1,j-1]-data[i,j])
    s=sum(sm(i,j) for i,j in ij())
    K2=s/(si-1)**2

    sm=lambda i,j: np.abs(data[i,j+1]-data[i,j])+np.abs(data[i,j-1]-data[i,j]) 
    s=sum(sm(i,j) for i,j in ij())
    K3=s/(si-1)**2

    sm=lambda i,j: np.abs(data[i+1,j]-data[i,j])+np.abs(data[i-1,j]-data[i,j])
    s=sum(sm(i,j) for i,j in ij())
    K4=s/(si-1)**2

    return K0,K1,K2,K3,K4

def prn(K):
    f="{:.5f}"
    for k in range(len(K)):
        print(f.format(K[k]),end=" ")
    print()

#at size 30, K0 K1 K2 K3 K4
#          5.28000 9.69529 9.21330 9.22715 9.46814 
#          5.28000 9.69529 9.21330 9.22715 9.46814
#         17.84000 9.72576 9.60665 9.56233 9.88920 38.78393
#         12.48000 9.66205 9.60388 8.96122 9.67590 37.90305 

get_data(True)
prn(TEST(Z))

def ijkl():
    for i in range(16):
        for j in range(16):
            for k in range(16):
                for l in range(16):
                    yield (i,j,k,l)

def test_scan():
    global pattern
    index=np.zeros([16**4,4])
    #candidates=np.zeros([1000,4])
    ddd=np.zeros([CANDIDATES.shape[0],5])
    id=0
    #for i0,i1,i2,i3 in ijkl():
    for i0,i1,i2,i3 in CANDIDATES:
        pattern=[i0,i1,i2,i3]
        get_data()
        k=TEST(Z)
        ddd[id]=(k[0],i0,i1,i2,i3)
        id+=1
        #size 30 criteria
        #if k[0]<17 and k[1]>9.6 and k[2]>9.6 and k[3]>9.6 and k[4]>9.6:
        #    if id<candidates.style[0]:
        #        candidates[id]=(i0,i1,i2,i3)
        #        print("candidates",(i0,i1,i2,i3),k[0],k[1],k[2],k[3],k[4])
        #        id+=1
    #if id==candidates.style[0]:
    #    print("over")
    #for i in range(id):
    #    print(candidates[i])

    def key(e):
        return e[0]
    sss=list(ddd)
    sss.sort(key=key)
    for i in range(id):
        print(sss[i])
#test_scan()


def draw():
    fig, ax = plt.subplots(figsize=(5,5),layout="constrained")
    level=np.arange(0,15.1,1)
    CS=ax.contourf(X,Y,Z,level,cmap="bwr")
    ax.axis("square")

def candidates_plot():
    global pattern
    id=0
    for i0,i1,i2,i3 in CANDIDATES:
        pattern=[i0,i1,i2,i3]
        get_data()
        draw()
        plt.savefig("candidate-{0}-{1}-{2}-{3}.svg".format(i0,i1,i2,i3))
        plt.close()
        print(id)
        id+=1

#candidates_plot()

#pattern=[14,13,2,11]
#get_data()
#draw()
#plt.show()

def draw_compare():
    global pattern
    pattern=[0,1,2,3]
    patterns=[[0,3,15,10],[0x5,0x8,0x2,0xc],[0,1,2,3]]
    fig,ax=plt.subplots(nrows=1,ncols=3,sharex=False,figsize=(6,3),layout="constrained")
    for i,p in enumerate(patterns):
        pattern=p
        get_data()
        level=np.arange(0,15.1,1)
        CS=ax[i].contourf(X,Y,Z,level,cmap="gray")
        ax[i].set_title("pattern\n{0},{1},{2},{3}".format(*pattern))
        ax[i].axis("square")
        ax[i].set_xlabel("n")
        ax[i].set_ylabel("m",rotation=0)
    fig.colorbar(CS, ax=ax[-1],shrink=0.5)

HI=256
create_XYZ()    
get_data()
draw_compare()
plt.show()
