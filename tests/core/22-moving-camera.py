from core.base import Base
from core.attribute import Attribute
from core.openGLUtils import OpenGLUtils
from core.uniform import Uniform
from core.matrix import Matrix
import numpy as np
from OpenGL.GL import *


class Test(Base):
    def initialize(self):
        vertexShaderCode = """
        in vec3 position;
        uniform mat4 projectionMatrix;
        uniform mat4 modelMatrix;
        void main() {
            gl_Position = projectionMatrix * modelMatrix * vec4(position, 1.0);
        }
        """
        
        fragmentShaderCode = """
        out vec4 fragColor;
        void main() {
            gl_FragColor = vec4(0.0,1.0,0.0,1.0);
        }
        """
        
        self.programRef = OpenGLUtils.initializeProgram(
            vertexShaderCode, fragmentShaderCode
        )
        # render settings
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glEnable(GL_DEPTH_TEST)
        
        # setup VAOs
        vaoRef = glGenVertexArrays(1)
        glBindVertexArray(vaoRef)
        
        # vertex attributes
        # small triangle
        positionData = [[ 0.0 , 0.1, 0.0],
                        [ 0.05,-0.1, 0.0],
                        [-0.05,-0.1, 0.0]]
        self.vertexCount = len(positionData)

        positionDataAttribute = Attribute("vec3", positionData)
        # associate vertex buffer to variable
        positionDataAttribute.associateVariable(self.programRef, "position")
        
        # set camera (facing +z)
        mMatrix = Matrix.makeTranslation(0,0,-1)
        self.modelMatrix = Uniform("mat4", mMatrix)
        self.modelMatrix.locateVariable(self.programRef, "modelMatrix")
        # set projection matrix
        pMatrix = Matrix.makePerspective()
        self.projectionMatrix = Uniform("mat4", pMatrix)
        self.projectionMatrix.locateVariable(self.programRef, "projectionMatrix")


    
    def update(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        ds = 0.01
        dphi = 0.05
        # global transformations
        if self.input.isKeyPressed("w"):
            m = Matrix.makeTranslation( 0, ds, 0)
            # @ symbol for matrix mult
            self.modelMatrix.data = m @ self.modelMatrix.data
        if self.input.isKeyPressed("a"):
            m = Matrix.makeTranslation(-ds, 0, 0)
            self.modelMatrix.data = m @ self.modelMatrix.data
        if self.input.isKeyPressed("s"):
            m = Matrix.makeTranslation( 0, -ds, 0)
            self.modelMatrix.data = m @ self.modelMatrix.data
        if self.input.isKeyPressed("d"):
            m = Matrix.makeTranslation(ds, 0, 0)
            self.modelMatrix.data = m @ self.modelMatrix.data

        if self.input.isKeyPressed("space"):
            m = Matrix.makeTranslation( 0, 0, ds)
            self.modelMatrix.data = m @ self.modelMatrix.data
        if self.input.isKeyPressed("left control"):
            m = Matrix.makeTranslation( 0, 0,-ds)
            self.modelMatrix.data = m @ self.modelMatrix.data
        # rotations
        if self.input.isKeyPressed("q"):
            m = Matrix.makeRotationZ(dphi)
            self.modelMatrix.data = m @ self.modelMatrix.data
        if self.input.isKeyPressed("e"):
            m = Matrix.makeRotationZ(-dphi)
            self.modelMatrix.data = m @ self.modelMatrix.data
            
        # local transformations
        if self.input.isKeyPressed("i"):
            m = Matrix.makeTranslation( 0, ds, 0)
            self.modelMatrix.data = self.modelMatrix.data @ m
        if self.input.isKeyPressed("j"):
            m = Matrix.makeTranslation(-ds, 0, 0)
            self.modelMatrix.data = self.modelMatrix.data @ m
        if self.input.isKeyPressed("k"):
            m = Matrix.makeTranslation( 0, -ds, 0)
            self.modelMatrix.data = self.modelMatrix.data @ m
        if self.input.isKeyPressed("l"):
            m = Matrix.makeTranslation(ds, 0, 0)
            self.modelMatrix.data = self.modelMatrix.data @ m
        if self.input.isKeyPressed("n"):
            m = Matrix.makeTranslation( 0, 0, ds)
            self.modelMatrix.data = self.modelMatrix.data @ m
        if self.input.isKeyPressed("m"):
            m = Matrix.makeTranslation( 0, 0,-ds)
            self.modelMatrix.data = self.modelMatrix.data @ m
        if self.input.isKeyPressed("u"):
            m = Matrix.makeRotationZ(dphi)
            self.modelMatrix.data = self.modelMatrix.data @ m
        if self.input.isKeyPressed("o"):
            m = Matrix.makeRotationZ(-dphi)
            self.modelMatrix.data = self.modelMatrix.data @ m
        
        glUseProgram(self.programRef)
        self.projectionMatrix.uploadData()
        self.modelMatrix.uploadData()
        glDrawArrays(GL_TRIANGLES, 0, self.vertexCount)

Test().run()