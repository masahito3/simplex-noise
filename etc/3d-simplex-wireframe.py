import numpy as np
from mayavi import mlab
from tvtk.api import tvtk

append= tvtk.AppendPolyData()

#1
points = np.array([[0,0,0], [5/6,-1/6,-1/6], [2/3,2/3,-1/3], [1/2,1/2,1/2]], 'f')
triangles = np.array([[0,1,3], [0,3,2], [1,2,3], [0,2,1]])
mesh = tvtk.PolyData(points=points, polys=triangles)
append.add_input_data(mesh)

#2
points = np.array([[0,0,0], [5/6,-1/6,-1/6], [2/3,-1/3,2/3], [1/2,1/2,1/2]], 'f')
mesh = tvtk.PolyData(points=points, polys=triangles)
append.add_input_data(mesh)
#3
points = np.array([[0,0,0], [-1/6,-1/6,5/6], [2/3,-1/3,2/3], [1/2,1/2,1/2]], 'f')
mesh = tvtk.PolyData(points=points, polys=triangles)
append.add_input_data(mesh)
#4
points = np.array([[0,0,0], [-1/6,-1/6,5/6], [-1/3,2/3,2/3], [1/2,1/2,1/2]], 'f')
mesh = tvtk.PolyData(points=points, polys=triangles)
append.add_input_data(mesh)
#5
points = np.array([[0,0,0], [-1/6,5/6,-1/6], [-1/3,2/3,2/3], [1/2,1/2,1/2]], 'f')
mesh = tvtk.PolyData(points=points, polys=triangles)
append.add_input_data(mesh)
#6
points = np.array([[0,0,0], [-1/6,5/6,-1/6], [2/3,2/3,-1/3], [1/2,1/2,1/2]], 'f')
mesh = tvtk.PolyData(points=points, polys=triangles)
append.add_input_data(mesh)

fig=mlab.figure()

mapper=tvtk.PolyDataMapper()
mapper.set_input_connection(append.output_port)
#mapper.set_input_data(mesh)
p=tvtk.Property(opacity=1,color=(1,1,1),ambient=1,representation="wireframe",line_width=1)
#p=tvtk.Property(opacity=0.5,color=(1,1,1),line_width=1)
actor=tvtk.Actor(mapper=mapper,property=p)
fig.scene.add_actor(actor)

#mlab.points3d([1/2],[1/2],[1/2])

#MAX=2
#MIN=-2
#mlab.axes(extent=[MIN,MAX,MIN,MAX,MIN,MAX],ranges=[MIN,MAX,MIN,MAX,MIN,MAX])
mlab.show()
