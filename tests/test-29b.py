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
    def __init__(self,x,y,z,duration):
        geometry    = BoxGeometry(width=duration, height=0.5, depth=0.1)
        material    = SurfaceBasicMaterial({"baseColor":[0,1,0]})
        super().__init__(geometry, material)
        self.translate(x,y,z)




# render a scene
class Test(Base):
    def initialize(self):
        print("Initializing Program...")
        
        # setup objects
        self.renderer   = Renderer()
        self.scene      = Scene()
        self.camera     = Camera()
        note1 = Note(0,0,0,1)
        note2 = Note(1,1,0,0.5)
        note3 = Note(2,0,0,0.5)
        note4 = Note(3,-1,0,1)
        self.scene.add(note1)
        self.scene.add(note2)
        self.scene.add(note3)
        self.scene.add(note4)
        
        # pull camera towards +z axis
        self.camera.setPosition(0,0,4)

    def update(self):
        self.camera.translate(0.01,0,0)
        self.renderer.render(self.scene, self.camera)
        

# instantiate and run class
Test().run()
