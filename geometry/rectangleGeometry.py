from geometry.geometry import Geometry
from core.attribute import Attribute

class RectangleGeometry(Geometry):
    # create rectangle in xy-plane centered around origin
    # set default colors to make shape visible from any angle
    def __init__(self, width=1, height=1):
        super().__init__()
        # vertex ordering 
        # 2---3
        # | / |   triangles: 0-1-3, 0-3-2
        # 0---1
        P0 = [-width/2,-height/2, 0]
        P1 = [ width/2,-height/2, 0]
        P2 = [-width/2, height/2, 0]
        P3 = [ width/2, height/2, 0]
        # vertex colors listed in same order
        # default: w,r,g,b
        C0,C1,C2,C3 = [1,1,1], [1,0,0], [0,1,0], [0,0,1]
        
        positionData = [P0, P1, P3,  P0, P3, P2]
        colorData =    [C0, C1, C3,  C0, C3, C2]
        
        self.attributes["vertexPosition"] = Attribute("vec3", positionData)
        self.attributes["vertexColor"]    = Attribute("vec3", colorData)
        
        self.countVertices()
        
    