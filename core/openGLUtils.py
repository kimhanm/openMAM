from OpenGL.GL import *

# static methods to load/compile shaders
# and link to create GPU programs
class OpenGLUtils:
    @staticmethod
    def initializeShader(shaderCode, shaderType):
        # specify OpenGL version and requirements
        #extension = "#extension GL_ARB_shading_language_420pack: require \n"
        #shaderCode = "#version 330 \n " + extension + shaderCode
        shaderCode = "#version 330 \n " + shaderCode

        # create empty shader object
        shaderRef = glCreateShader(shaderType)
        glShaderSource(shaderRef, shaderCode)
        glCompileShader(shaderRef)

        # error checking
        compileSuccess = glGetShaderiv(shaderRef, GL_COMPILE_STATUS)
        if not compileSuccess:
            # retrieve error (as bytestring) and convert to character string
            errorMessage = glGetShaderInfoLog(shaderRef)
            errorMessage = "\n" + errorMessage.decode("utf-8")
            # free memory and raise exception, printing message
            glDeleteShader(shaderRef)
            raise Exception(errorMessage)

        # compilation successful, return reference
        return shaderRef

    @staticmethod
    def initializeProgram(vertexShaderCode, fragmentShaderCode):
        # program shaders and store refs
        vertexShaderRef = OpenGLUtils.initializeShader(vertexShaderCode, GL_VERTEX_SHADER)
        fragmentShaderRef = OpenGLUtils.initializeShader(fragmentShaderCode, GL_FRAGMENT_SHADER)

        # create program and attach shaders
        programRef = glCreateProgram()
        glAttachShader(programRef, vertexShaderRef)
        glAttachShader(programRef, fragmentShaderRef)
        
        # link and error handling
        glLinkProgram(programRef)
        linkSuccess = glGetProgramiv(programRef, GL_LINK_STATUS)
        if not linkSuccess:
            errorMessage = glGetProgramInfoLog(programRef)
            errorMessage = "\n" + errorMessage.decode("utf-8")
            glDeleteProgram(programRef)
            
            raise Exception(errorMessage)
        # linking successful, return program reference
        return programRef


#
#    @staticmethod
#    def printSystemInfo():
#        #print("Vendor  : " + glGetString(GL_VENDOR).decode("utf-8"))
#        #print("Renderer: " + glGetString(GL_RENDERER).decode("utf-8"))
#        #print("OpenGL version supported: " + glGetString(GL_VERSION).decode("utf-8"))
#        #print("GLSL version supported  : " + glGetString(GL_SHADING_LANGUAGE_VERSION).decode("utf-8"))
#        print("Vendor  : " + glGetString(GL_VENDOR).str())
#        print("Renderer: " + glGetString(GL_RENDERER).str())
#        print("OpenGL version supported: " + glGetString(GL_VERSION).str())
#        print("GLSL version supported  : " + glGetString(GL_SHADING_LANGUAGE_VERSION).str())
