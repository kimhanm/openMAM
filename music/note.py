#deprecated
from core.mesh import Mesh
from geometry.rectangleGeometry import RectangleGeometry
from material.surfaceBasicMaterial import SurfaceBasicMaterial

# 1 Octave is set to unit length
# middle C = note 60
class Note(Mesh):
    def __init__(self, note=60,start_time=0,duration=1,velocity=80):
        self.note=note
        self.start_time = start_time
        self.duration= duration
        self.border = 0.03

        geometry = RectangleGeometry(self.duration - self.border, height=1/6 - self.border)
        material = SurfaceBasicMaterial({"baseColor":[0,1,0]})
        super().__init__(geometry, material)
        self.translate(self.start_time + self.duration/2, (self.note - 60)/12,0)

    def __repr__(self):
        return f"Note(note={self.note}, start_time={self.start_time}, duration={self.duration}, velocity={self.velocity})"