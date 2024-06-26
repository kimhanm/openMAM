from geometry.parametricSurfaceGeometry import ParametricSurfaceGeometry
from numpy import cos, sin, pi

# cylinder along y-axis
# low radialSegment count gives prism
class CylinderGeometry(ParametricSurfaceGeometry):
    def __init__(self,radius=1,length=1,radialSegments=10,heightSegments=10, resolution=0):

        yStart,yEnd = -length/2, length/2
        phiStart,phiEnd = -pi,+pi
        def f(y,phi):
            return [radius*cos(phi), y, radius*sin(phi)]
        if not resolution == 0:
            radialsegments = resolution
            heightSegments = resolution
        super().__init__(
                yStart, yEnd, heightSegments,
                phiStart, phiEnd, radialSegments,
                f)

