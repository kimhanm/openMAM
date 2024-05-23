from OpenGL.GL import *
from core.mesh import Mesh

class Renderer:
    def __init__(self, clearColor=[0,0,0]):
        glEnable(GL_DEPTH_TEST)
        glClearColor(clearColor[0], clearColor[1], clearColor[2],0.0)
    # we cannot just pull the camera from the scene, since
    # scene might have multiple cameras
    def render(self, scene, camera):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        camera.updateViewMatrix()
        
        # extract a list of all Mesh objects
        descendantList = scene.getDescendantList()
        meshFilter = lambda x: isinstance(x, Mesh)
        meshList = list(filter(meshFilter, descendantList))
        
        for mesh in meshList:
            if not mesh.visible:
                continue
            # programRef is stored in material of mesh
            glUseProgram(mesh.material.programRef)
            
            # bind VAO
            glBindVertexArray(mesh.vaoRef)
            
            # update uniform matrices
            mesh.material.uniforms["modelMatrix"].data = mesh.getWorldMatrix()
            mesh.material.uniforms["viewMatrix"].data = camera.viewMatrix
            mesh.material.uniforms["projectionMatrix"].data = camera.projectionMatrix
            
            # update uniforms stored in material
            for _variableName, uniformObject in mesh.material.uniforms.items():
                uniformObject.uploadData()
                
            # update render settings
            mesh.material.updateRenderSettings()

            glDrawArrays(
                mesh.material.settings["drawStyle"], 0, mesh.geometry.vertexCount
            )



