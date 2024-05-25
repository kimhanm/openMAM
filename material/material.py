from core.openGLUtils import OpenGLUtils
from core.uniform import Uniform

class Material(object):
    def __init__(self, vertexShaderCode, fragmentShaderCode):
        self.programRef = OpenGLUtils.initializeProgram(
            vertexShaderCode, fragmentShaderCode
        )
        
        # standard uniform objects
        self.uniforms = {}
        self.uniforms["modelMatrix"] = Uniform("mat4", None)
        self.uniforms["viewMatrix"] = Uniform("mat4", None)
        self.uniforms["projectionMatrix"] = Uniform("mat4", None)
        
        # OpenGL render settings
        self.settings = {}
        self.settings["drawStyle"] = None
        
    # initialize all Uniform variable references
    def locateUniforms(self):
        for variableName, uniformObject in self.uniforms.items():
            uniformObject.locateVariable(self.programRef, variableName)
    def updateRenderSettings(self):
        pass
    
    def setProperties(self, properties={}):
        for name, data in properties.items():
            # update uniforms
            if name in self.uniforms.keys():
                self.uniforms[name].data = data
            elif name in self.settings.keys():
                self.settings[name] = data
            else:
                raise Exception("Material has no property: " + name)
