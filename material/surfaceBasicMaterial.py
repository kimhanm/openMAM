from material.basicMaterial import BasicMaterial
from OpenGL.GL import *

class SurfaceBasicMaterial(BasicMaterial):
    def __init__(self, properties={}):
        super().__init__()

        # render settings for surfaces
        self.settings["drawStyle"] = GL_TRIANGLES
        self.settings["doubleSide"] = True
        self.settings["wireframe"] = False
        # if using wireframe, set frame width
        self.settings["lineWidth"] = 2
        
        self.setProperties(properties) 
    
    def updateRenderSettings(self):
        if self.settings["doubleSide"]:
            glDisable(GL_CULL_FACE)
        else:
            glEnable(GL_CULL_FACE)
        if self.settings["wireframe"]:
            glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
        else:
            glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
        glLineWidth(self.settings["lineWidth"])