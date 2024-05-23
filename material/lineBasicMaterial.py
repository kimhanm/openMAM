from material.BasicMaterial import BasicMaterial
from OpenGL.GL import *

class LineBasicMaterial(BasicMaterial):
    def __init__(self, properties={})
        super().__init_()

        # render settings for lines
        # drawStyle: GL_LINE_STRIP, GL_LINE_LOOP, GL_LINES
        self.settings["drawStyle"] = GL_LINE_STRIP
        # lineType: "connected", "loop", "segments"
        self.settings["lineType"] = "connected"
        self.settings["lineWidth"] = 2
        
       self.setProperties(properties) 
    
    def updateRenderSettings(self):
        glLineWidth(self.settings["lineWidth"])
        lt = self.settings["lineType"]
        if lt == "connected":
            self.settings["drawStyle"] = GL_LINE_STRIP
        elif lt == "loop":
            self.settings["drawStyle"] = GL_LINE_LOOP
        elif lt == "segments":
            self.settings["drawStyle"] = GL_LINES
        else:
            raise Exception("Unkown line style: " + lt)