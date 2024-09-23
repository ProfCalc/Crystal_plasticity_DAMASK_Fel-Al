import damask
import numpy as np
N= 100
g= 64
geom = damask.GeomGrid.from_Voronoi_tessellation(np.ones(3,dtype=int)*g,np.ones(3),np.random.random(N*3).reshape(N,3))
geom.save(f"{N}_{g}.vtr")