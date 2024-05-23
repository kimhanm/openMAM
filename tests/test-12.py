from core.base import Base
from core.openGLUtils import OpenGLUtils
from core.attribute import Attribute
from core.uniform import Uniform
from OpenGL.GL import *
from numpy import sin, cos


# render multiple triangles with only 1 vertex buffer
class Test(Base):
    def initialize(self):
        vertexShaderCode = """
        // declare variables before main
        in vec3 position;
        uniform vec3 translation;
        void main() {
            // overloaded + for vectors
            vec3 pos = position + translation;
           gl_Position = vec4(pos.x, pos.y, pos.z, 1.0);
        }
        """
        fragmentShaderCode = """
        uniform vec3 color;
        out vec4 fragColor;
        void main() {
            fragColor = vec4(color.r,color.g,color.b,1.0);
        }
        """
        self.programRef = OpenGLUtils.initializeProgram(
            vertexShaderCode, fragmentShaderCode)
        

        # render settings
        glPointSize(8)
        glLineWidth(4)
        glClearColor(0.01, 0.0, 0.02, 1.0)

        
        # set up VAO
        vaoRef = glGenVertexArrays(1)
        glBindVertexArray(vaoRef)
        
        # triangle
        positionData = [[ 0.0, 0.2, 0.0 ],
                        [ 0.2,-0.2, 0.0 ],
                        [-0.2,-0.2, 0.0 ]]
        positionAttribute = Attribute("vec3", positionData)
        # returns -1 if "position" is not used
        positionAttribute.associateVariable(self.programRef, "position") 
        self.vertexCount = len(positionData)

        self.translation1 = Uniform("vec3", [-0.5, 0.0, 0.0])
        self.translation1.locateVariable(self.programRef, "translation")

        self.translation2 = Uniform("vec3", [ 0.5, 0.0, 0.0])
        self.translation2.locateVariable(self.programRef, "translation")
        
        self.color1 = Uniform("vec3", [1.0, 0.0, 0.0])
        self.color1.locateVariable(self.programRef, "color")

        self.color2 = Uniform("vec3", [0.0, 1.0, 0.0])
        self.color2.locateVariable(self.programRef, "color")
        
        # keep track of time
        self.time = 0
    
    def update(self):
        glClear(GL_COLOR_BUFFER_BIT)
        self.time += 1/60 # assume 60 FPS
        
        # tell openGL which program is used
        glUseProgram(self.programRef)
        # move left triangle up
        self.translation1.data[1] += cos(self.time)/120
        self.translation1.uploadData()
        self.color1.uploadData()
        glDrawArrays(GL_TRIANGLES, 0, self.vertexCount)

        # change color of right triangle
        self.color2.data[0] = (1 + sin(self.time))/2
        self.color2.data[1] = (1 + cos(self.time))/2
        self.color2.data[2] = (1 - sin(self.time))/2
        self.translation2.uploadData()
        self.color2.uploadData()
        glDrawArrays(GL_TRIANGLES, 0, self.vertexCount)

Test().run()