from core.base      import Base
from core.renderer  import Renderer
from core.scene     import Scene
from core.camera    import Camera
from music.note     import Note
from music.midi     import parse_midi
from core.matrix    import Matrix
import mido
from extras.movementRig import MovementRig


# render a scene
class Test(Base):
    def initialize(self):
        # setup objects
        self.renderer   = Renderer()
        self.scene      = Scene()
        self.part = Scene()
        # add camera to movement rig
        self.camera     = Camera()
        self.bpm = 180
        self.rig = MovementRig(unitsPerSecond=self.bpm/10)
        self.rig.add(self.camera)
        self.scene.add(self.rig)
        self.paused = False
        
        self.rig.setPosition(0,0,6)

        mido.set_backend('mido.backends.pygame')
        print("Using backend: ")
        print(mido.backend)
        
        violin1 = './midi/violin1.mid'
        violin2 = './midi/violin2.mid'
        viola = './midi/viola.mid'
        cello = './midi/cello.mid'
        self.noteQueue = []
        self.noteQueue += parse_midi(violin1,scaling_factor = 1/500,properties={"baseColor":[1.0, 0.9, 0.0]})
        self.noteQueue += parse_midi(violin2,scaling_factor = 1/500,properties={"baseColor":[0.1, 0.9, 0.1]})
        self.noteQueue += parse_midi(viola, scaling_factor = 1/500, properties={"baseColor":[0.9, 0.1, 0.1]})
        self.noteQueue += parse_midi(cello, scaling_factor = 1/500, properties={"baseColor":[0.1, 0.2, 0.8]})
        self.removeQueue = []

        self.time = -1
        self.timeWindow = 2 * self.bpm/self.fps 
        
        self.scene.add(self.part)
        print("number of notes: ")
        print(len(self.noteQueue))
        
        print("move: wasd\n" + "up/down/sprint: space,ctrl,shift\n" + "look: hjkl")

    def update(self):
        for note in self.noteQueue:
            if note.start_time <= self.time:
                self.part.add(note)
                self.noteQueue.remove(note)
                self.removeQueue.append(note)
        for note in self.removeQueue:
            if note.start_time + note.duration + self.timeWindow <= self.time:
                self.part.remove(note)
                self.removeQueue.remove(note)

        if self.input.isKeyDown("left shift"):
            self.bpm *= 4
        if self.input.isKeyUp("left shift"):
            self.bpm /= 4
        if self.input.isKeyDown("return"):
            # reset rig and camera on rig
            self.camera.setPosition(0,0,0)
            self.camera.transform = Matrix.makeIdentity()
            self.rig.transform = Matrix.makeIdentity()
            self.rig.setPosition(0,-1,6)
            self.part.setPosition(0,0,0)
            self.time = 0
        self.rig.update(self.input, 1/60)
        if self.input.isKeyDown("p"):
            self.paused = not self.paused
        if not self.paused:
            self.part.translate(-self.bpm/(self.fps * 60),0,0)
            self.time += self.bpm / (self.fps * 60)
        self.renderer.render(self.scene, self.camera)

        

# instantiate and run class
Test().run()

