import pygame

class Input:
    def __init__(self):
        self.quit = False
        
        # store keystates in list
        self.keyDownList = []
        self.keyUpList = []
        self.keyPressedList = []
    
    def update(self):
        # reset discrete key states
        self.keyDownList = []
        self.keyUpList = []
        # iterate over all input events since last check
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit = True
            elif event.type == pygame.KEYDOWN:
                keyName = pygame.key.name( event.key )
                self.keyDownList.append( keyName )
                self.keyPressedList.append( keyName )
            elif event.type == pygame.KEYUP:
                keyName = pygame.key.name( event.key )
                self.keyUpList.append( keyName )
                self.keyPressedList.remove( keyName )

    # query key states
    def isKeyDown(self, keyName):
        return keyName in self.keyDownList
    def isKeyUp(self, keyName):
        return keyName in self.keyUpList
    def isKeyPressed(self, keyName):
        return keyName in self.keyPressedList
