from material.BasicMaterial import BasicMaterial
from OpenGL.GL import *

class PointBasicMaterial(BasicMaterial):
    def __init__(self, properties={})
        super().__init_()

        # render settings for points
        self.settings["drawStyle"] = GL_POINTS
        self.settings["pointSize"] = 4
        self.settings["roundedPoints"] = True
        
       self.setProperties(properties) 
    
    def updateRenderSettings(self):
        glPointSize(self.settings["pointSize"])
        if self.settings["roundedPoints"]:
            glEnable(GL_POINT_SMOOTH)
        else:
            glDisable(GL_POINT_SMOOTH)