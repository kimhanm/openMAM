from core.mesh import Mesh
from geometry.rectangleGeometry import RectangleGeometry
from material.surfaceBasicMaterial import SurfaceBasicMaterial

# 1 Octave is set to unit length
class Note(Mesh):
    def __init__(self, pitch=0,start=0,end=1):
        duration = end-start
        geometry = RectangleGeometry(duration, height=1/6)
        material = SurfaceBasicMaterial({"baseColor":[0,1,0]})
        super().__init__(geometry, material)
        self.translate(start + duration/2, pitch/12,0)
