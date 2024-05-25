from geometry.parametricSurfaceGeometry import ParametricSurfaceGeometry
from numpy import cos, sin, pi

# theta=0 along y-axis
class EllipsoidGeometry(ParametricSurfaceGeometry):
    def __init__(self,width=1,height=1,depth=1, resolution=10):
        thetaStart,thetaEnd = 0,pi
        phiStart,phiEnd = -pi,+pi
        def f(theta,phi):
            return [width*sin(theta)*cos(phi), height*cos(theta)*sin(phi),depth*sin(theta)*cos(theta)]
        super().__init__(
                thetaStart,thetaEnd, resolution,
                phiStart, phiEnd, resolution,
                f)

