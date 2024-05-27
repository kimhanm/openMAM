from core.base import Base
from core.openGLUtils import OpenGLUtils
from OpenGL.GL import *

# renders a single point

class Test(Base):
    def initialize(self):
        print("Initializing...")
        
        # create GPU program
        # vertex shader Code
        vertexShaderCode = """
        void main() {
            // x,y,z,w
            gl_Position = vec4(0.0, 0.0, 0.0, 1.0);
        }
        """
        fragmentShaderCode = """
        out vec4 fragColor;
        void main() {
            // r,g,b,alpha
            fragColor = vec4(1.0, 1.0, 0.0, 1.0);
        }
        """
        # send code to GPU, compile and store program reference
        self.programRef = OpenGLUtils.initializeProgram(
            vertexShaderCode, fragmentShaderCode)
        
        vaoRef = glGenVertexArrays(1)
        glBindVertexArray(vaoRef)

        # render settings
        glPointSize(8)
    def update(self):
        # select program to use
        glUseProgram(self.programRef)
        # render geometric objects
        glDrawArrays(GL_POINTS, 0, 1)


Test().run()
        