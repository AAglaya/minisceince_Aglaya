import gmsh
import sys
import os
import math

gmsh.initialize()

gmsh.model.add("skull")

path = os.path.dirname(os.path.abspath(__file__))
gmsh.merge(os.path.join(path, "Skull.stl"))

gmsh.model.mesh.classifySurfaces(180 * math.pi/180, True, True, 180 * math.pi /180)

s = gmsh.model.getEntities(2)
l = gmsh.model.geo.addSurfaceLoop([s[i][1] for i in range(len(s))])
gmsh.model.geo.addVolume([l])

gmsh.model.geo.synchronize()

gmsh.model.mesh.generate(3)

if '-nopopup' not in sys.argv:
    gmsh.fltk.run()

gmsh.finalize()