from core.base import Base
from core.openGLUtils import OpenGLUtils
from core.attribute import Attribute
from core.uniform import Uniform
from OpenGL.GL import *


class Test(Base):
    def initialize(self):
        vertexShaderCode = """
        in vec3 position;
        uniform vec3 translation;
        void main() {
            vec3 pos = position + translation;
            gl_Position = vec4(pos.x, pos.y, pos.z, 1.0);
        }
        """
        
        fragmentShaderCode = """
        out vec4 fragColor;
        void main() {
            fragColor = vec4(0.0, 1.0, 0.0, 1.0);
        }
        """
        self.programRef = OpenGLUtils.initializeProgram(
            vertexShaderCode, fragmentShaderCode
        )
        # render settings
        glPointSize(8)
        glLineWidth(4)
        
        vaoRef = glGenVertexArrays(1)
        glBindVertexArray(vaoRef)
        
        positionData = [[ 0.0, 0.2, 0.0],
                        [ 0.2,-0.2, 0.0],
                        [-0.2,-0.2, 0.0]]
        positionAttribute = Attribute("vec3", positionData)
        positionAttribute.associateVariable(self.programRef, "position")
        self.vertexCount = len(positionData)
        
        self.translation = Uniform("vec3", [ 0.0, 0.0, 0.0])
        self.translation.locateVariable(self.programRef, "translation")
        

    def update(self):
        glClear(GL_COLOR_BUFFER_BIT)
        glUseProgram(self.programRef)
        # move triangle
        distance = 0.01
        if self.input.isKeyPressed("up"):
            self.translation.data[1] += distance
        if self.input.isKeyPressed("down"):
            self.translation.data[1] -= distance
        if self.input.isKeyPressed("left"):
            self.translation.data[0] -= distance
        if self.input.isKeyPressed("right"):
            self.translation.data[0] += distance
        if self.input.isKeyPressed("return"):
            self.translation.data[2] += distance
        if self.input.isKeyPressed("space"):
            self.translation.data[2] -= distance
        self.translation.uploadData()
        
        glDrawArrays(GL_TRIANGLES, 0, self.vertexCount)


Test().run()