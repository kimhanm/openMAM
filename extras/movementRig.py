from core.object3D import Object3D
from numpy import pi, float32, array
from numpy.linalg import norm

class MovementRig(Object3D):
    def __init__(self, unitsPerSecond=1, degreesPerSecond=60):
        
        super().__init__()
        self.unitsPerSecond = unitsPerSecond
        self.degreesPerSecond = degreesPerSecond

        # attach object for looking up/down
        self.lookAttachment = Object3D()
        self.children = [self.lookAttachment]
        self.lookAttachment.parent = self
        
        # customizable key bindings
        self.KEY_MOVE_FORWARDS  = "w"
        self.KEY_MOVE_LEFT      = "a"
        self.KEY_MOVE_BACKWARDS = "s"
        self.KEY_MOVE_RIGHT     = "d"
        
        self.KEY_TURN_LEFT      = "h"
        self.KEY_TURN_RIGHT     = "l"
        self.KEY_MOVE_UP        = "space"
        self.KEY_MOVE_DOWN      = "left ctrl"
        self.KEY_LOOK_UP        = "k"
        self.KEY_LOOK_DOWN      = "j"


    def add(self, child):
        # add child to lookAttachment
        self.lookAttachment.add(child)
    def update(self, inputObject, dt):
        dphi = self.degreesPerSecond * pi / 180 * dt
        direction = array([0.0,0.0,0.0])

        if inputObject.isKeyPressed(self.KEY_MOVE_FORWARDS):
            direction += array([0,0,-1])
        if inputObject.isKeyPressed(self.KEY_MOVE_BACKWARDS):
            direction += array([0,0,+1])
        if inputObject.isKeyPressed(self.KEY_MOVE_LEFT):
           direction += array([-1,0,0])
        if inputObject.isKeyPressed(self.KEY_MOVE_RIGHT):
            direction += array([+1,0,0])
        if inputObject.isKeyPressed(self.KEY_MOVE_UP):
            direction += array([0,+1,0])
        if inputObject.isKeyPressed(self.KEY_MOVE_DOWN):
            direction += array([0,-1,0])
        # normalize movement to length unitPerSecond * dt, unless zero
        if not norm(direction) == 0:
            factor = self.unitsPerSecond * dt / norm(direction)
            direction *= factor
        self.translate(direction[0],direction[1],direction[2])

        if inputObject.isKeyPressed(self.KEY_TURN_LEFT):
            self.rotateY(-dphi)
        if inputObject.isKeyPressed(self.KEY_TURN_RIGHT):
            self.rotateY(dphi)
        # use lookattachment for looking instead of turning
        if inputObject.isKeyPressed(self.KEY_LOOK_UP):
            self.lookAttachment.rotateX(dphi)
        if inputObject.isKeyPressed(self.KEY_LOOK_DOWN):
            self.lookAttachment.rotateX(-dphi)
