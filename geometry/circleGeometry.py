from geometry.geometry import Geometry
from numpy import sin, cos, pi

class CircleGeometry(Geometry):
    def __init__(self,radius=1,sides=3):
        super().__init__()
        phi = 2 * pi / sides
        positionData = []
        colorData = []
        for i in range(sides):
            positionData.append([0,0,0])
            positionData.append([radius*cos(i*phi),radius*sin(i*phi),0])
            positionData.append([radius*cos((i+1)*phi),radius*sin((i+1)*phi),0])
            colorData.append([1,1,1])
            colorData.append([1,0,0])
            colorData.append([0,1,0])


        self.addAttribute("vec3", "vertexPosition", positionData)
        self.addAttribute("vec3", "vertexColor", colorData)
        self.countVertices()
