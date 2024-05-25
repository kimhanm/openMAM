from geometry.parametricSurfaceGeometry import ParametricSurfaceGeometry
from numpy import cos, sin, pi

# hole in y-axis
class TorusGeometry(ParametricSurfaceGeometry):
    def __init__(self,bigRadius=1,smallRadius=0.3,bigResolution=10,smallResolution=10,resolution=0):
        thetaStart,thetaEnd = -pi,pi # big circle
        phiStart,phiEnd = -pi,+pi    # small circle
        R = bigRadius
        r = smallRadius
        def f(theta,phi):
            return [R * cos(theta) + r*cos(theta)*cos(phi), r*sin(phi),R * sin(theta) + r*sin(theta)*cos(phi)]
        if not resolution == 0:
            bigResolution = resolution
            smallResolution = resolution
        super().__init__(
                thetaStart,thetaEnd, bigResolution,
                phiStart, phiEnd, smallResolution,
                f)

