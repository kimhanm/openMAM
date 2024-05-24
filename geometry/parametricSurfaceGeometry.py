from geometry.geometry import Geometry

# surface from embedding: f: R^2 -> R^3
# uResolution: number of sides in u-axis
class ParametricSurfaceGeometry(Geometry):
    def __init__(self,  uStart, uEnd, uResolution,
                        vStart, vEnd, vResolution, 
                        f):
        super().__init__()
        # greate grid
        du = (uEnd - uStart) / uResolution
        dv = (vEnd - vStart) / vResolution

        grid = []
        # number of points per side = resolution+1
        for i in range (uResolution+1):
            vArray = []
            for j in range (vResolution+1):
                u = uStart + i * du
                v = vStart + j * dv
                vArray.append(f(u,v))
            grid.append(vArray)
        
        positionData = []
        colorData = []
        # default vertex colors
        C1,C2,C3 = [1,0,0], [0,1,0], [0,0,1]
        C4,C5,C6 = [0,1,1], [1,0,1], [1,1,0]
        
        # group grid into triangles
        # (i,j+1)---(i+1,j+1)
        #   |      /    |
        #   |     /     |
        #   |    /      |
        # (i,j)-----(i+1,j)
        for i in range(uResolution):
            for j in range(vResolution):
                positionData += [grid[i][j], grid[i+1][j], grid[i+1][j+1]]
                positionData += [grid[i][j], grid[i+1][j+1], grid[i][j+1]]
                colorData += [C1, C2, C3, C4, C5, C6]
        self.addAttribute("vec3", "vertexPosition", positionData)
        self.addAttribute("vec3", "vertexColor", colorData)
        self.countVertices()

                



