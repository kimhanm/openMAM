#deprecated
from core.base      import Base
from core.renderer  import Renderer
from core.scene     import Scene
from core.camera    import Camera
from core.matrix    import Matrix
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
        self.rig = MovementRig(unitsPerSecond=8)
        self.rig.add(self.camera)
        self.scene.add(self.rig)
        
        self.rig.setPosition(0,-1,6)

        self.bpm = 180
        # pitch, duration
        # bars 1-4
        ## v1
        noteList     = []
        noteList    += [[7,2],[0,1]]
        noteList    += [[0,0.5,False], [-5,0.5],[-3,0.5],[-1,0.5],[0,0.5],[2,0.5]]
        noteList    += [[3,0.5],[2,0.5],[5,0.5],[3,0.5],[2,0.5],[0,0.5]]
        noteList    += [[0,0.5],[-2,0.5],[-3,0.5],[-2,0.5],[-7,1]]
        noteList    += [[7,2],[0,1]]
        noteList    += [[0,0.5,False], [-5,0.5],[-3,0.5],[-1,0.5],[0,0.5],[2,0.5]]
        noteList    += [[3,0.5],[2,0.5],[5,0.5],[3,0.5],[2,0.5],[0,0.5]]
        noteList    += [[-2,3]]
        phrasev1 = Phrase(noteList)
        phrasev1.translate(1,0,0)
        self.subScene.add(phrasev1)
        ## v2
        noteList     = [[-2,3,True],[0,1,False],[-2,1,True], [-2,1,True],[-2,1,True],[-2,1,True],[-3,1,True], [-7,3,True]]
        noteList     += [[-2,3,True],[0,1,False],[-2,1,True], [-2,1,True],[-2,1,True],[-2,1,True],[-3,1,True], [-7,3,True]]
        # add color yellow
        for note in noteList:
            note.append([1,1,0])
        phrasev2 = Phrase(noteList)
        phrasev2.translate(1,0,0)
        self.subScene.add(phrasev2)

        noteList     = [[-5,3,True],[0,1,False],[-5,1,True], [-5,1,True],[-5,1,True],[-5,1,True],[0,4,False]]
        noteList     += [[-5,3,True],[0,1,False],[-5,1,True], [-5,1,True],[-5,1,True],[-5,1,True]]
        for note in noteList:
            note.append([1,1,0])
        phrasev2b = Phrase(noteList)
        phrasev2b.translate(1,0,0)
        self.subScene.add(phrasev2b)
        
        ## vla
        noteList     = [[-12,3,True],[0,1,False],[-12,1,True], [-12,1,True],[-12,1,True],[-12,1,True],[-9,1,True], [-9,2,True],[-10,1,True]]
        noteList     += [[-12,3,True],[0,1,False],[-12,1,True], [-12,1,True],[-12,1,True],[-12,1,True],[-9,1,True], 
                        [-9,0.5,True],[-10,0.5,True],[-12,0.5,True],[-10,0.5,True],[-14,1,True]]
        # add color red
        for note in noteList:
            note.append([1,0,0])
        phrasevla = Phrase(noteList)
        phrasevla.translate(1,0,0)
        self.subScene.add(phrasevla)
        
        ## cl
        noteList      = [[-21,3,True],[0,1,False],[-21,1,True], [-21,1,True],[-21,1,True],[-21,1,True],[-19,1,True], [-28,3,True]]
        noteList     += [[-21,3,True],[0,1,False],[-21,1,True], [-21,1,True],[-21,1,True],[-21,1,True],[-19,1,True], [-28,3,True]]
        # add color blue
        for note in noteList:
            note.append([0,0,1])
        phrasecl = Phrase(noteList)
        phrasecl.translate(1,0,0)
        self.subScene.add(phrasecl)



        self.paused = False

    def update(self):
        if self.input.isKeyDown("return"):
            # reset rig and camera on rig
            self.camera.setPosition(0,0,0)
            self.camera.transform = Matrix.makeIdentity()
            self.rig.transform = Matrix.makeIdentity()
            self.rig.setPosition(0,-1,6)
            self.subScene.setPosition(0,0,0)
        self.rig.update(self.input, 1/60)
        if self.input.isKeyDown("p"):
            self.paused = not self.paused
        if not self.paused:
            self.subScene.translate(-self.bpm/(60 * 60),0,0)
        self.renderer.render(self.scene, self.camera)

# instantiate and run class
Test().run()



