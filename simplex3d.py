import numpy as np
from mayavi import mlab
from tvtk.api import tvtk

N=3
F=(np.sqrt(N+1)-1)/N
T=np.array([[1+F,  F,  F],
            [  F,1+F,  F],
            [  F,  F,1+F]])

G=(1-1/np.sqrt(N+1))/N
S=np.array([[1-G, -G, -G],
            [ -G,1-G, -G],
            [ -G, -G,1-G]])

def HASH(n,m,l):
    return (b(n,m,l,0)+b(m,l,n,1)+b(l,n,m,2)+b(n,m,l,3)+
            b(m,l,n,4)+b(l,n,m,5)+b(n,m,l,6)+b(m,l,n,7))

pattern=[0x15,0x38,0x32,0x2c,0x0d,0x13,0x07,0x2a]

def b(n,m,l,B):
    id=4*bit(n,B)+2*bit(m,B)+bit(l,B)
    return pattern[id]

def bit(n,B):
    return n>>B & 1

def k(r2): #r2 means r squared
    if 0.6>r2:
        return 8*(0.6-r2)**4
    return 0

def grad(h,x,y,z):
    h3,b2,b3,b4,b5=h&3,bit(h,2),bit(h,3),bit(h,4),bit(h,5)
    h3==1 and (p:=x,q:=y,r:=z) or (h3==2 and (p:=y,q:=z,r:=x) or (p:=z,q:=x,r:=y))
    b5==b3 and (p:=-p)
    b5==b4 and (q:=-q)
    b5!=(b4^b3) and (r:=-r)
    h3 and (b2 and (q:=0,) or (r:=0))
    return k(x**2+y**2+z**2)*(p+q+r)

#reference
#def h(n):
#    return hash(str(n).encode())
#def HASH(n,m,l):
#    return h(h(h(n)+m)+l)
#g=((1,1,0),(-1,1,0),(1,-1,0),(-1,-1,0),
#   (1,0,1),(-1,0,1),(1,0,-1),(-1,0,-1),
#   (0,1,1),(0,-1,1),(0,1,-1),(0,-1,-1))
#def grad(h,x,y,z):
#    return k(x**2+y**2+z**2)*np.dot(g[h%12],(x,y,z))

def calc(n,m,l,xin,yin,zin):
    xn,ym,zl=np.matmul(S,(n,m,l))
    x,y,z=xin-xn,yin-ym,zin-zl # the relative vector in a simplex grid
    h=HASH(n,m,l)
    return grad(h,x,y,z)

def simplex3d(xin,yin,zin): # the coordinates of a point in a simplex grid
    xp,yp,zp=np.matmul(T,(xin,yin,zin)) # the coordinates of a point in a cubic grid
    o0=np.array((int(xp),int(yp),int(zp))) # the grid point
    x,y,z=xp-o0[0],yp-o0[1],zp-o0[2] # the relative vector in a cubic grid
    if x>=y and x>=z and y>=z: #1
        a=1,0,0
        b=1,1,0
    elif x>=y and x>=z and z>=y: #2
        a=1,0,0
        b=1,0,1
    elif x>=y and z>=x and z>=y: #3
        a=0,0,1
        b=1,0,1
    elif y>=x and z>=x and z>=y: #4
        a=0,0,1
        b=0,1,1
    elif y>=x and z>=x and y>=z: #5
        a=0,1,0
        b=0,1,1
    elif y>=x and x>=z and y>=z: #6
        a=0,1,0
        b=1,1,0
    o1=o0+a
    o2=o0+b
    o3=o0+(1,1,1)
    return calc(*o0,xin,yin,zin)+ \
           calc(*o1,xin,yin,zin)+ \
           calc(*o2,xin,yin,zin)+ \
           calc(*o3,xin,yin,zin)

if __name__=="__main__":
    def ijk(n,m,l):
        for i in range(n):
            for j in range(m):
                for k in range(l):
                    yield i,j,k
    #make plot data
    MAX=2
    X=Y=Z=np.arange(0,MAX+0.05,0.05)
    X,Y,Z=np.meshgrid(X,Y,Z,indexing="ij") #x[nx,ny,nz]
    W=np.empty(X.shape)
    for nx,ny,nz in ijk(*X.shape):
        W[nx,ny,nz]=simplex3d(X[nx,ny,nz],Y[nx,ny,nz],Z[nx,ny,nz])
    print(np.max(W),np.min(W))

    #plot
    fig=mlab.figure()
    #render the contour. the indexing must be x[nx,ny,nz]
    contour=mlab.contour3d(X,Y,Z,W,contours=20)
    #contour=mlab.contour3d(X,Y,Z,W,contours=[0.0])

    scalar=mlab.pipeline.scalar_field(X,Y,Z,W)
    plane=mlab.pipeline.image_plane_widget(scalar,
                                           plane_orientation='y_axes',
                                           slice_index=10,)

    #show the axes
    mlab.axes(extent=[0,MAX,0,MAX,0,MAX],ranges=[0,MAX,0,MAX,0,MAX])

    #show the color bar
    scalar_bar=tvtk.ScalarBarActor()
    fig.scene.renderer.add_actor2d(scalar_bar)

    #make the color lookup table
    HI=0.32
    LO=-0.32
    TS=256
    ctf=tvtk.ColorTransferFunction()
    ctf.add_rgb_point(LO,0,0,1) #the low values show blue
    ctf.add_rgb_point((HI+LO)/2,1,1,1) #near zero values show white
    ctf.add_rgb_point(HI,1,0,0) #the high values show red
    lut=tvtk.LookupTable()
    lut.table_range=[LO,HI]
    lut.table=[np.array((ctf.get_color(LO+i*(HI-LO)/TS)+(0.5,)))*255 for i in np.arange(TS+1)]
    #set it
    contour.actor.mapper.lookup_table=lut
    scalar_bar.lookup_table=lut
    plane.use_lookup_table=False
    plane.module_manager.scalar_lut_manager.lut=lut
    plane.use_lookup_table=True
    mlab.show()
