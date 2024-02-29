import gmsh
import sys

gmsh.initialize()

gmsh.model.add("torus")

lc = 1e-2

gmsh.model.geo.addPoint(0, 0, 0, lc, 1)

gmsh.model.geo.addPoint(.1, 0, 0, lc, 2)
gmsh.model.geo.addPoint(-.1, 0, 0, lc, 3)

gmsh.model.geo.addPoint(.2, 0, 0, lc, 4)
gmsh.model.geo.addPoint(-.2, 0, 0, lc, 5)

gmsh.model.geo.addPoint(.15, 0, 0, lc, 10)
gmsh.model.geo.addPoint(-.15, 0, 0, lc, 11)
gmsh.model.geo.addPoint(.15, 0, .05, lc, 12)
gmsh.model.geo.addPoint(-.15, 0, .05, lc, 13)
gmsh.model.geo.addPoint(.15, 0, -.05, lc, 14)
gmsh.model.geo.addPoint(-.15, 0, -.05, lc, 15)

gmsh.model.geo.addPoint(0, 0, .05, lc, 16)
gmsh.model.geo.addPoint(0, 0, -.05, lc, 17)


gmsh.model.geo.addCircleArc(2, 1, 3, 1)
gmsh.model.geo.addCircleArc(3, 1, 2, 2)
gmsh.model.geo.addCircleArc(4, 1, 5, 3)
gmsh.model.geo.addCircleArc(5, 1, 4, 4)

gmsh.model.geo.addCircleArc(2, 10, 12, 5)
gmsh.model.geo.addCircleArc(12, 10, 4, 6)
gmsh.model.geo.addCircleArc(4, 10, 14, 7)
gmsh.model.geo.addCircleArc(14, 10, 2, 8)

gmsh.model.geo.addCircleArc(3, 11, 13, 9)
gmsh.model.geo.addCircleArc(13, 11, 5, 10)
gmsh.model.geo.addCircleArc(5, 11, 15, 11)
gmsh.model.geo.addCircleArc(15, 11, 3, 12)

gmsh.model.geo.addCircleArc(13, 16, 12, 13)
gmsh.model.geo.addCircleArc(12, 16, 13, 14)
gmsh.model.geo.addCircleArc(14, 17, 15, 15)
gmsh.model.geo.addCircleArc(15, 17, 14, 16)

gmsh.model.geo.addCurveLoop([6, 3, -10, -14], 1)
gmsh.model.geo.addSurfaceFilling([1], 1)

gmsh.model.geo.addCurveLoop([-9, -1, 5, 14], 2)
gmsh.model.geo.addSurfaceFilling([2], 2)

gmsh.model.geo.addCurveLoop([11, -15, -7, 3], 3)
gmsh.model.geo.addSurfaceFilling([3], 3)

gmsh.model.geo.addCurveLoop([12, -1, -8, 15], 4)
gmsh.model.geo.addSurfaceFilling([4], 4)

gmsh.model.geo.addCurveLoop([-9, 2, 5, -13], 5)
gmsh.model.geo.addSurfaceFilling([5], 5)

gmsh.model.geo.addCurveLoop([-12, 16, 8, -2], 6)
gmsh.model.geo.addSurfaceFilling([6], 6)

gmsh.model.geo.addCurveLoop([10, 4, -6, -13], 7)
gmsh.model.geo.addSurfaceFilling([7], 7)

gmsh.model.geo.addCurveLoop([11, 16, -7, -4], 8)
gmsh.model.geo.addSurfaceFilling([8], 8)

gmsh.model.geo.addSurfaceLoop([1, 2, 3, 4, 5, 6, 7, 8], 1)
gmsh.model.geo.addVolume([1], 1)

gmsh.model.geo.synchronize()

gmsh.model.mesh.generate(3)

gmsh.write("torus.msh")

if '-nopopup' not in sys.argv:
    gmsh.fltk.run()

gmsh.finalize()
