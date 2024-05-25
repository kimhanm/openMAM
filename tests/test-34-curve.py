from core.base      import Base
from core.renderer  import Renderer
from core.scene     import Scene
from core.camera    import Camera
from core.mesh      import Mesh
from geometry.circle2DGeometry import Circle2DGeometry
from material.lineBasicMaterial import LineBasicMaterial

# render a scene
class Test(Base):
    def initialize(self):
        # setup objects
        self.renderer   = Renderer()
        self.scene      = Scene()
        self.camera     = Camera()
        self.camera.setPosition(0,0,4)

        geometry        = Circle2DGeometry(segments=10)
        material        = LineBasicMaterial({"lineWidth":16,"lineType":"connected","useVertexColors":1})
        #material        = LineBasicMaterial({"useVertexColors":1,"lineWidth":4})
        self.mesh = Mesh(geometry, material)
        self.scene.add(self.mesh)


    def update(self):
        self.mesh.rotateX(0.01)
        self.mesh.rotateY(0.013)
        self.renderer.render(self.scene, self.camera)
        

# instantiate and run class
Test().run()
