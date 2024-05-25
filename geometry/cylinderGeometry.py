from geometry.parametricSurfaceGeometry import ParametricSurfaceGeometry
from numpy import cos, sin, pi

# cylinder along y-axis
class CylinderGeometry(ParametricSurfaceGeometry):
    def __init__(self,radius=1,length=1,resolution=10):

        yStart,yEnd = -length/2, length/2
        phiStart,phiEnd = -pi,+pi
        def f(y,phi):
            return [radius*cos(phi), y, radius*sin(phi)]
        super().__init__(
                yStart, yEnd, resolution,
                phiStart, phiEnd, resolution,
                f)

