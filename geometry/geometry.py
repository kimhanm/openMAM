# base geometry class stores dictionary between 
# variable names and attribute objects
# aswell as attribute data 

# default objects will contain default colors
# to make shape understandable


class Geometry():
    def __init__(self):
        # dictionary
        self.attributes = {}
        
        self.vertexCount = None
        
    def countVertices(self):
        # number of vertices is length of
        # _any_ attribute object's array
        attrib = list (self.attributes.values() )[0]
        self.vertexCount = len(attrib.data)
