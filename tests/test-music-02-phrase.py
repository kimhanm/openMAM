from core.base      import Base
from core.renderer  import Renderer
from core.scene     import Scene
from core.camera    import Camera
from music.phrase   import Phrase
from extras.movementRig import MovementRig

# render a scene
class Test(Base):
    def initialize(self):
        # setup objects
        self.renderer   = Renderer()
        self.scene      = Scene()
        self.subScene   = Scene()
        self.scene.add(self.subScene)
        # add camera to movement rig
        self.camera     = Camera()
        self.rig = MovementRig(unitsPerSecond=4)
        self.rig.add(self.camera)
        self.scene.add(self.rig)
        
        self.rig.setPosition(0,0,4)

        self.bpm = 120
        # pitch, duration
        noteList = [[0,5],[1,2],[10,2],[9,2],[1,2],[2,1],[11,1],[12,0.25],[14,0.25],[12,0.25],[11,0.25],[12,1]]
        self.phrase = Phrase(noteList)
        self.phrase.translate(1,0,0)
        self.subScene.add(self.phrase)
        self.paused = False

    def update(self):
        if len(self.input.keyDownList) > 0:
            print ("Keys down:", self.input.keyDownList)
        self.rig.update(self.input, 1/60)
        if self.input.isKeyDown("p"):
            self.paused = not self.paused
        if not self.paused:
            self.subScene.translate(-self.bpm/(60 * 60),0,0)
        self.renderer.render(self.scene, self.camera)

# instantiate and run class
Test().run()


