from geometry.parametricCurveGeometry import ParametricCurveGeometry
from numpy import cos, sin, pi

class Circle2DGeometry(ParametricCurveGeometry):
    def __init__(self,radius=1,segments=10):
        start,stop = 0,2 * pi
        def c(t):
            return [cos(t), sin(t), 0]
        super().__init__(start, stop, segments, c)
            


