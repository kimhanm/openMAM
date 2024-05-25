from geometry.parametricSurfaceGeometry import ParametricSurfaceGeometry
from numpy import cos, sin, pi

# cone along y-axis
# low radialSegments makes a pyramid
class ConeGeometry(ParametricSurfaceGeometry):
    def __init__(self,radius=1,height=1,radialSegments=10,heightSegments=10,resolution=0):
        yStart,yEnd = 0,height
        phiStart,phiEnd = -pi,+pi
        def f(y,phi):
            return [radius * y * cos(phi), y, radius * y * sin(phi)]
        if not resolution == 0:
            radialSegments = resolution
            heightSegments = resolution
        super().__init__(
                yStart, yEnd, heightSegments,
                phiStart, phiEnd, radialSegments,
                f)
            


