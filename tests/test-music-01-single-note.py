from core.base      import Base
from core.renderer  import Renderer
from core.scene     import Scene
from core.camera    import Camera
from music.note     import Note
#from core.mesh      import Mesh

# render a scene
class Test(Base):
    def initialize(self):
        # setup objects
        self.renderer   = Renderer()
        self.scene      = Scene()
        self.camera     = Camera()
        self.camera.setPosition(0,0,4)

        self.note = Note(0,0,1)
        self.scene.add(self.note)


    def update(self):
        self.note.translate(-0.01,0,0)
        self.renderer.render(self.scene, self.camera)
        

# instantiate and run class
Test().run()

