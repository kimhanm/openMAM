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
        
        # set up VAO
        vaoRef = glGenVertexArrays(1)
        glBindVertexArray(vaoRef)
        
        positionData = [[ 0.8, 0.0, 0.0 ],
                        [ 0.4, 0.6, 0.0 ],
                        [-0.4, 0.6, 0.0 ],
                        [-0.8, 0.0, 0.0 ],
                        [-0.4,-0.6, 0.0 ],
                        [ 0.4,-0.6, 0.0 ]]
        positionAttribute = Attribute("vec3", positionData)
        # returns -1 if "position" is not used
        positionAttribute.associateVariable(self.programRef, "position") 
    
        self.vertexCount = len(positionData)
    def update(self):
        # tell openGL which program is used
        glUseProgram(self.programRef)
        # 6 points are drawn
        #glDrawArrays(GL_POINTS, 0, self.vertexCount)
        #glDrawArrays(GL_LINE_LOOP, 0, self.vertexCount)
        #glDrawArrays(GL_LINES, 0, self.vertexCount)
        #glDrawArrays(GL_TRIANGLES, 0, self.vertexCount)
        glDrawArrays(GL_TRIANGLE_FAN, 0, self.vertexCount)
        
Test().run()