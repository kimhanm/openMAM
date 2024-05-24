from core.base      import Base
from core.renderer  import Renderer
from core.scene     import Scene
from core.camera    import Camera
from core.mesh      import Mesh
from geometry.circleGeometry import CircleGeometry
from geometry.boxGeometry import BoxGeometry
from material.surfaceBasicMaterial import SurfaceBasicMaterial

# render a scene
class Test(Base):
    def initialize(self):
        # setup objects
        self.renderer   = Renderer()
        self.scene      = Scene()
        self.camera     = Camera()
        self.camera.setPosition(0,0,4)

        #geometry        = BoxGeometry(width=0.5, height=0.5, depth=0.5)
        geometry        = CircleGeometry(radius=1, sides=2**14)
        material        = SurfaceBasicMaterial({"useVertexColors":1})
        self.mesh = Mesh(geometry, material)
        self.scene.add(self.mesh)


    def update(self):
        self.renderer.render(self.scene, self.camera)
        

# instantiate and run class
Test().run()
