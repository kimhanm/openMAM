from core.base      import Base
from core.renderer  import Renderer
from core.scene     import Scene
from core.camera    import Camera
from core.mesh      import Mesh
from geometry.sphereGeometry import SphereGeometry
from geometry.ellipsoidGeometry import EllipsoidGeometry
from geometry.cylinderGeometry import CylinderGeometry
from material.surfaceBasicMaterial import SurfaceBasicMaterial

# render a scene
class Test(Base):
    def initialize(self):
        # setup objects
        self.renderer   = Renderer()
        self.scene      = Scene()
        self.camera     = Camera()
        self.camera.setPosition(0,0,4)

        #geometry        = SphereGeometry(radius=1, resolution=16)
        #geometry        = EllipsoidGeometry(width=1, height=0.8, depth=1.5, resolution=16)
        geometry        = CylinderGeometry(radius=0.5, length=2, resolution=16)
        material        = SurfaceBasicMaterial({"useVertexColors":1})
        self.mesh = Mesh(geometry, material)
        self.scene.add(self.mesh)


    def update(self):
        self.mesh.rotateX(0.01)
        self.mesh.rotateY(0.013)
        self.renderer.render(self.scene, self.camera)
        

# instantiate and run class
Test().run()

