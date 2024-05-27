#deprecated
from core.mesh import Mesh
from geometry.rectangleGeometry import RectangleGeometry
from material.surfaceBasicMaterial import SurfaceBasicMaterial

# 1 Octave is set to unit length
class Note(Mesh):
    def __init__(self, pitch=0,start=0,end=1,visible=True,color=[0,1,0]):
        self.visible = visible
        self.border = 0.02
        duration = end-start - self.border
        geometry = RectangleGeometry(duration, height=1/6)
        material = SurfaceBasicMaterial({"baseColor":color})
        super().__init__(geometry, material,visible=visible)
        self.translate(start + duration/2, pitch/12,0)
