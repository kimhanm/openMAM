from core.base      import Base
from core.renderer  import Renderer
from core.scene     import Scene
from core.camera    import Camera
from music.note     import Note
from extras.movementRig import MovementRig
from midi.midi      import parse_midi
import mido


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
        
        #midi_file_path = './midi/chaconne.mid'
        #midi_file_path = './midi/arpa.mid' # super laggy
        #midi_file_path = './midi/playing-minecraft.mid'
        midi_file_path = './midi/outro.mid'
        notes = parse_midi(midi_file_path,scaling_factor = 1/500)
        
        for note in notes:
            self.part.add(note)
        self.scene.add(self.part)
        
        print("move: wasd\n" + "up/down/sprint: space,ctrl,shift\n" + "look: hjkl")

    def update(self):
        if self.input.isKeyDown("return"):
            # reset rig and camera on rig
            self.camera.setPosition(0,0,0)
            self.camera.transform = Matrix.makeIdentity()
            self.rig.transform = Matrix.makeIdentity()
            self.rig.setPosition(0,-1,6)
            self.part.setPosition(0,0,0)
        self.rig.update(self.input, 1/60)
        if self.input.isKeyDown("p"):
            self.paused = not self.paused
        if not self.paused:
            self.part.translate(-self.bpm/(60 * 60),0,0)
        self.renderer.render(self.scene, self.camera)

        

# instantiate and run class
Test().run()



