from core.base      import Base
from core.renderer  import Renderer
from core.scene     import Scene
from core.camera    import Camera
from core.mesh      import Mesh
from geometry.torusGeometry import TorusGeometry
from material.surfaceBasicMaterial import SurfaceBasicMaterial

# render a scene
class Test(Base):
    def initialize(self):
        # setup objects
        self.renderer   = Renderer()
        self.scene      = Scene()
        self.camera     = Camera()
        self.camera.setPosition(0,0,4)
        
        resolution = 100

        #geometry        = TorusGeometry(bigRadius=1,smallRadius=0.3,resolution=resolution)
        geometry        = TorusGeometry(bigRadius=1,smallRadius=0.3,bigResolution=resolution, smallResolution=resolution//3)
        material        = SurfaceBasicMaterial({"useVertexColors":1})
        self.mesh = Mesh(geometry, material)
        self.scene.add(self.mesh)


    def update(self):
        self.mesh.rotateX(0.01)
        self.mesh.rotateY(0.013)
        self.renderer.render(self.scene, self.camera)
        

# instantiate and run class
Test().run()


