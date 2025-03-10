import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import *

np.set_printoptions(precision=4)

#random number table
p=[151,160,137,91,90,15,
   131,13,201,95,96,53,194,233,7,225,140,36,103,30,69,142,8,99,37,240,21,10,23,
   190, 6,148,247,120,234,75,0,26,197,62,94,252,219,203,117,35,11,32,57,177,33,
   88,237,149,56,87,174,20,125,136,171,168, 68,175,74,165,71,134,139,48,27,166,
   77,146,158,231,83,111,229,122,60,211,133,230,220,105,92,41,55,46,245,40,244,
   102,143,54, 65,25,63,161, 1,216,80,73,209,76,132,187,208, 89,18,169,200,196,
   135,130,116,188,159,86,164,100,109,198,173,186, 3,64,52,217,226,250,124,123,
   5,202,38,147,118,126,255,82,85,212,207,206,59,227,47,16,58,17,182,189,28,42,
   223,183,170,213,119,248,152, 2,44,154,163, 70,221,153,101,155,167, 43,172,9,
   129,22,39,253, 19,98,108,110,79,113,224,232,178,185, 112,104,218,246,97,228,
   251,34,242,193,238,210,144,12,191,179,162,241, 81,51,145,235,249,14,239,107,
   49,192,214, 31,181,199,106,157,184, 84,204,176,115,121,50,45,127, 4,150,254,
   138,236,205,93,222,114,67,29,24,72,243,141,128,195,78,66,215,61,156,180]

rng = np.random.default_rng()
random_table=rng.integers(0,16,(256,256))
def hash3_ref(n,m,l):
    return rng.integers(0,256)

def h(n):
    return hash(str(n).encode())
def hash3_ref2(n,m,l):
    return h(h(h(n)+m)+l)

def hash3(n,m,l):
    return p[(p[(p[n%256]+m)%256]+l)%256]

def hash2(n,m):
    return p[(p[n%256]+m)%256]

def hash1(n):
    return p[n%256]

HI=256

def create_XYZ():
    global X,Y,Z
    X=Y=np.arange(0,HI,1)
    X,Y=np.meshgrid(X,Y,indexing="ij") #x[nx,ny]
    Z=np.empty(X.shape)
    
def get_data():
    global Z
    for n in range(X.shape[0]):
        for m in range(X.shape[1]):
            #Z[n,m]=hash3(n,m,100) & 0b1111
            #Z[n,m]=hash3(n,m,256) & 0b1111
            #Z[n,m]=hash3(n,m,0) & 0b1111
            Z[n,m]=hash3_ref2(n,m,0)%12
            #Z[n,m]=hash3(n,m,100) & 0b1111
            #Z[n,m]=hash3(150,n,m) & 0b1111
            #Z[n,m]=hash2(n,m) & 0b111
            #Z[n,m]=hash1(n) & 0b111

def draw():
    fig, ax = plt.subplots(figsize=(5,5),layout="constrained")
    level=np.arange(0,8.1,1)
    CS=ax.contourf(X,Y,Z,level,cmap="gray")
    fig.colorbar(CS,shrink=0.75)
    ax.axis("square")

create_XYZ()
get_data()
draw()
plt.show()
