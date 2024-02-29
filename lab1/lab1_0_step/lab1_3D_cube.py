import gmsh
import sys

gmsh.initialize()

gmsh.model.add("cube")

lc = 1e-2
gmsh.model.geo.addPoint(0, 0, 0, lc, 1)
gmsh.model.geo.addPoint(.1, 0, 0, lc, 2)
gmsh.model.geo.addPoint(.1, .1, 0, lc, 3)
gmsh.model.geo.addPoint(0, .1, 0, lc, 4)
gmsh.model.geo.addPoint(0, 0, .1, lc, 5)
gmsh.model.geo.addPoint(.1, 0, .1, lc, 6)
gmsh.model.geo.addPoint(.1, .1, .1, lc, 7)
gmsh.model.geo.addPoint(0, .1, .1, lc, 8)

for i in range(3):
    gmsh.model.geo.addLine(i + 1, i + 2, i + 1)

gmsh.model.geo.addLine(4, 1, 4)

for i in range(3):
    gmsh.model.geo.addLine(i + 5, i + 6, i + 5)

gmsh.model.geo.addLine(8, 5, 8)

for i in range(4):
    gmsh.model.geo.addLine(i + 1, i + 5, i + 9)


gmsh.model.geo.addCurveLoop([1, 2, 3, 4], 1)
gmsh.model.geo.addPlaneSurface([1], 1)

gmsh.model.geo.addCurveLoop([5, 6, 7, 8], 2)
gmsh.model.geo.addPlaneSurface([2], 2)

gmsh.model.geo.addCurveLoop([9, -8, -12, 4], 3)
gmsh.model.geo.addPlaneSurface([3], 3)

gmsh.model.geo.addCurveLoop([10, -5 , -9, 1], 4)
gmsh.model.geo.addPlaneSurface([4], 4)

gmsh.model.geo.addCurveLoop([11, -6, -10, 2], 5)
gmsh.model.geo.addPlaneSurface([5], 5)

gmsh.model.geo.addCurveLoop([12, -7, -11, 3], 6)
gmsh.model.geo.addPlaneSurface([6], 6)


l = gmsh.model.geo.addSurfaceLoop([i + 1 for i in range(6)])
gmsh.model.geo.addVolume([l])

gmsh.model.geo.synchronize()

gmsh.model.mesh.generate(3)

gmsh.write("cube.msh")

if '-nopopup' not in sys.argv:
    gmsh.fltk.run()

gmsh.finalize()