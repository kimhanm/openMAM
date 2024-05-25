from core.base      import Base
from core.renderer  import Renderer
from core.scene     import Scene
from core.camera    import Camera
from core.mesh      import Mesh
from geometry.coneGeometry import ConeGeometry
from material.surfaceBasicMaterial import SurfaceBasicMaterial

# render a scene
class Test(Base):
    def initialize(self):
        # setup objects
        self.renderer   = Renderer()
        self.scene      = Scene()
        self.camera     = Camera()
        self.camera.setPosition(0,0,4)

        #geometry        = ConeGeometry(radius=0.5, height=2, resolution=16)
        geometry        = ConeGeometry(radius=1, height=1, radialSegments=4, heightSegments=10)
        material        = SurfaceBasicMaterial({"useVertexColors":1})
        self.mesh = Mesh(geometry, material)
        self.scene.add(self.mesh)


    def update(self):
        self.mesh.rotateX(0.01)
        self.mesh.rotateY(0.013141)
        self.renderer.render(self.scene, self.camera)
        

# instantiate and run class
Test().run()

