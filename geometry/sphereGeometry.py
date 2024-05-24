from geometry.parametricSurfaceGeometry import ParametricSurfaceGeometry
from numpy import cos, sin, pi

class SphereGeometry(ParametricSurfaceGeometry):
    def __init__(self,radius=1, resolution=10):
        thetaStart,thetaEnd = 0,pi
        phiStart,phiEnd = -pi,+pi
        def f(theta,phi):
            return [radius * sin(theta)* cos(phi), radius * sin(theta)*sin(phi),radius*cos(theta)]
        super().__init__(
                thetaStart,thetaEnd, resolution,
                phiStart, phiEnd, resolution,
                f)

