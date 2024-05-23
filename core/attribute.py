import numpy as np
from OpenGL.GL import *



class Attribute:
    def __init__(self, dataType, data):
        # int | float | vec2 | vec3 | vec4 | mat4
        self.dataType = dataType
        # array to be stored in buffer
        self.data = data
        
        # get reference to available buffer in GPU
        self.bufferRef = glGenBuffers(1)
        # upload data
        self.uploadData()
        
        
    def uploadData(self):
        # convert data to np array of floats
        data = np.array(self.data).astype(np.float32)
        
        # select buffer used by following functions
        
        glBindBuffer(GL_ARRAY_BUFFER, self.bufferRef)
        
        # store data in bound buffer, ravel == flatten
        glBufferData(GL_ARRAY_BUFFER, data.ravel(), GL_STATIC_DRAW)
        
    # associate variablein GPU program with this buffer
    def associateVariable(self, programRef, variableName):
        # get reference for program variable
        variableRef = glGetAttribLocation(programRef, variableName)
        # error check
        if variableRef == -1:  
            return
        # select buffer used by following functions
        glBindBuffer(GL_ARRAY_BUFFER, self.bufferRef)
        
        # specify how data will be read from currently bound buffer
        if self.dataType == "int":
            glVertexAttribPointer(variableRef, 1, GL_INT, False, 0, None)
        elif self.dataType == "float":
            glVertexAttribPointer(variableRef, 1, GL_FLOAT, False, 0, None)
        elif self.dataType == "vec2":
            glVertexAttribPointer(variableRef, 2, GL_FLOAT, False, 0, None)
        elif self.dataType == "vec3":
            glVertexAttribPointer(variableRef, 3, GL_FLOAT, False, 0, None)
        elif self.dataType == "vec4":
            glVertexAttribPointer(variableRef, 4, GL_FLOAT, False, 0, None)
        elif self.dataType == "mat4":
            glVertexAttribPointer(variableRef, 16, GL_FLOAT, False, 0, None)
        else:
            raise Exception("Unkown Uttribute type: " + self.dataType)
        
        glEnableVertexAttribArray(variableRef)


    