from core.matrix import Matrix

# represents nodes of Scene Graph
# stores matrix representing local transformation
# reference to child objects and parent
class Object3D():
    def __init__(self):
        self.transform = Matrix.makeIdentity()
        self.parent = None
        self.children = []
        
    def add(self, child):
        self.children.append(child)
        self.children[-1].parent = self

    def remove(self, child):
        self.children.remove(child)
        child.parent = None

    def getWorldMatrix(self):
        if self.parent == None:
            return self.transform
        else:
            return self.parent.getWorldMatrix() @ self.transform
        
    
    # get descandants using DFS
    def getDescendantList(self):
        descendants = []
        nodesToProcess = [self]
        while len(nodesToProcess) > 0:
            node = nodesToProcess.pop(0)
            descendants.append(node)
            nodesToProcess = node.children + nodesToProcess
        return descendants
    

    def applyMatrix(self, matrix, localCoord=True):
        if localCoord:
            self.transform = self.transform @ matrix
        else:
            self.transform = matrix @ self.transform
    
    def translate(self, x,y,z, localCoord=True):
        m = Matrix.makeTranslation(x,y,z)
        self.applyMatrix(m,localCoord)

    def rotateX(self, angle, localCoord=True):
        m = Matrix.makeRotationX(angle)
        self.applyMatrix(m,localCoord)
    def rotateY(self, angle, localCoord=True):
        m = Matrix.makeRotationY(angle)
        self.applyMatrix(m,localCoord)

    def rotateZ(self, angle, localCoord=True):
        m = Matrix.makeRotationZ(angle)
        self.applyMatrix(m,localCoord)
    
    def scale(self, factor, localCoord=True):
        m = Matrix.makeScale(factor)
        self.applyMatrix(m,localCoord)
        
    # get/set position components of transformation matrix
    def getPosition(self):
        return [ self.transform.item(0,3),
                 self.transform.item(1,3),
                 self.transform.item(2,3) ]

    def setPosition(self, x, y, z):
        self.transform.itemset((0,3), x)
        self.transform.itemset((1,3), y)
        self.transform.itemset((2,3), z)