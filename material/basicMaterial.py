from material.material import Material
from core.uniform import Uniform


class BasicMaterial(Material):
    def __init__(self):
        vertexShaderCode = """
        uniform mat4 projectionMatrix;
        uniform mat4 viewMatrix;
        uniform mat4 modelMatrix;
        
        in vec3 vertexPosition;
        in vec3 vertexColor;
        out vec3 color;
        void main() {
            vec4 position = vec4(vertexPosition, 1.0);
            gl_Position = projectionMatrix * viewMatrix * modelMatrix * position;
            color = vertexColor;
        }
        """
        
        fragmentShaderCode = """
        uniform vec3 baseColor;
        uniform bool useVertexColors;
        in vec3 color;
        out vec4 fragColor;
        void main() {
            vec4 tmpColor = vec4(baseColor, 1.0);
            if ( useVertexColors ) {
                tmpColor *= vec4(color, 1.0);
            }
            fragColor = tmpColor;
        }
        """

        super().__init__(
            vertexShaderCode, fragmentShaderCode
        )
        self.uniforms["baseColor"] = Uniform("vec3", [1.0,1.0,1.0])
        self.uniforms["useVertexColors"] = Uniform("bool", 0)
        
        self.locateUniforms()
