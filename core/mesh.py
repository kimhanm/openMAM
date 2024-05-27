from core.object3D import Object3D
from OpenGL.GL import *

# stores VAO, geometry and material
# and sets up associations between 
# vertex buffers and shader vars

# geometry contains dictionary of
#  variable names and attribute objects
# material contains program
class Mesh(Object3D):
    def __init__(self, geometry, material,visible=True):
        super().__init__()
        self.geometry = geometry
        self.material = material
        self.visible = visible
        
        # set up associations between 
        # attributes in geometry and 
        # variables in material
        self.vaoRef = glGenVertexArrays(1)
        glBindVertexArray(self.vaoRef)
        for variableName, attributeObject in geometry.attributes.items():
            attributeObject.associateVariable(material.programRef, variableName)
        
        # unbind VAO
        glBindVertexArray(0)
