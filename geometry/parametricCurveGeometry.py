from geometry.geometry import Geometry
from numpy import linspace, vectorize

# geometry from curve c: R -> R^3
class ParametricCurveGeometry(Geometry):
    def __init__(self,  start, stop, segments,
                        c):
        super().__init__()
        
        dt = (stop - start)/segments
        positionData = []
        for i in range (segments+1):
            positionData.append(c(start + i * dt))

        colorData = [0,1,0]*(segments+1)
        self.addAttribute("vec3", "vertexPosition", positionData)
        self.addAttribute("vec3", "vertexColor", colorData)
        self.countVertices()

                




