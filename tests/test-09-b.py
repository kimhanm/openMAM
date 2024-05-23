from core.base import Base
from core.openGLUtils import OpenGLUtils
from core.attribute import Attribute
from OpenGL.GL import *


class Test(Base):
    def initialize(self):
        vertexShaderCode = """
        // declare variables before main
        in vec3 position;
        void main() {
           gl_Position = vec4(position.x, position.y, position.z, 1.0);
        }
        """
        fragmentShaderCode = """
        out vec4 fragColor;
        void main() {
            fragColor = vec4(0.0,1.0,0.0,1.0);
        }
        """
        self.programRef = OpenGLUtils.initializeProgram(
            vertexShaderCode, fragmentShaderCode)
        

        # render settings
        glPointSize(8)
        glLineWidth(4)
        
        # set up VAO for Triangle
        self.vaoTri = glGenVertexArrays(1)
        glBindVertexArray(self.vaoTri)
        
        positionDataTri =  [[-0.5, 0.8, 0.0 ],
                            [-0.2, 0.2, 0.0 ],
                            [-0.8, 0.2, 0.0 ]]
        positionAttributeTri = Attribute("vec3", positionDataTri)
        # returns -1 if "position" is not used
        positionAttributeTri.associateVariable(self.programRef, "position") 
    
        self.vertexCountTri = len(positionDataTri)

        # set up VAO for Square
        self.vaoSq = glGenVertexArrays(1)
        glBindVertexArray(self.vaoSq)
        
        positionDataSq =   [[ 0.8, 0.8, 0.0 ],
                            [ 0.8, 0.2, 0.0 ],
                            [ 0.2, 0.2, 0.0 ],
                            [ 0.2, 0.8, 0.0 ]]
        positionAttributeSq = Attribute("vec3", positionDataSq)
        # returns -1 if "position" is not used
        positionAttributeSq.associateVariable(self.programRef, "position") 
    
        self.vertexCountSq = len(positionDataSq)
    def update(self):
        # tell openGL which program is used
        glUseProgram(self.programRef)
        # bind and unbind vertex arrays
        glBindVertexArray(self.vaoTri)
        glDrawArrays(GL_LINE_LOOP, 0, self.vertexCountTri)
        glBindVertexArray(self.vaoSq)
        glDrawArrays(GL_TRIANGLE_FAN, 0, self.vertexCountSq)
        
Test().run()
