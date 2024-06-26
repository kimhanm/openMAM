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

# render a scene
class Test(Base):
    def initialize(self):
        # setup objects
        self.renderer   = Renderer()
        self.scene      = Scene()
        self.camera     = Camera()
        geometry        = BoxGeometry(width=0.5, height=0.5, depth=0.5)
        material        = SurfaceBasicMaterial({"useVertexColors":1})
        #material        = SurfaceBasicMaterial({"baseColor":[0,1,0]})
        self.cube = Mesh(geometry, material)
        self.scene.add(self.cube)
        
        # pull camera towards +z axis
        self.camera.setPosition(0,0,4)
        
        # backdrop
        #backGeometry = BoxGeometry(width=5, height=5, depth=0.5)
        #backMaterial = SurfaceBasicMaterial({"baseColor" : [1,1,0]})
        #backdrop = Mesh(backGeometry, backMaterial)
        #backdrop.translate(0.0,0.0,-10.0)
        #self.scene.add(backdrop)

    def update(self):
        self.cube.rotateX(0.01)
        self.cube.rotateY(0.015)
        self.cube.rotateZ(0.0175)
        self.renderer.render(self.scene, self.camera)
        

# instantiate and run class
Test().run()