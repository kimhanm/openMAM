# creating an application requires
# Base, Renderer, Scene, Camera, Mesh
# at least one geometry and one material class
# may optionally need Input class to handle input

from core.base      import Base
from core.renderer  import Renderer
from core.scene     import Scene
from core.camera    import Camera
from core.mesh      import Mesh
from geometry.boxGeometry import BoxGeometry
from material.surfaceBasicMaterial import SurfaceBasicMaterial

class Note(Mesh):
    def __init__(self,startTime,y,duration):
        geometry    = BoxGeometry(width=duration, height=0.2, depth=0.1)
        material    = SurfaceBasicMaterial({"baseColor":[0,1,0]})
        super().__init__(geometry, material)
        self.translate(startTime + duration/2,y,0)

# render a scene
class Test(Base):
    def initialize(self):
        # setup objects
        self.renderer   = Renderer()
        self.scene      = Scene()
        self.camera     = Camera()
        self.notes = []
        self.notes.append(Note(0,0,5))
        self.notes.append(Note(5,0.1,2))
        self.notes.append(Note(7,1,2))
        self.notes.append(Note(9,0.9,2))
        self.notes.append(Note(11,0.1,2))
        self.notes.append(Note(13,0.2,1))
        self.notes.append(Note(14,1.1,1))
        self.notes.append(Note(15,1.2,0.25))
        self.notes.append(Note(15.25,1.4,0.25))
        self.notes.append(Note(15.5,1.2,0.25))
        self.notes.append(Note(15.75,1.1,0.25))
        self.notes.append(Note(16,1.2,1))

        for note in self.notes:
            self.scene.add(note)
        
        # pull camera towards +z axis
        self.camera.setPosition(0,0,4)

    def update(self):
        for note in self.notes:
            note.translate(-2*1/60,0,0)
        self.renderer.render(self.scene, self.camera)
        

# instantiate and run class
Test().run()
