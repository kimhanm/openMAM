from core.base import Base
from core.input import Input

class Test(Base):
    def initialize(self):
        pass
    def update(self):
        #if self.input.isKeyDown("return"):
        #    print("return on investment")

            
        # debug input
        if len(self.input.keyDownList) > 0:
            print ("Keys down:", self.input.keyDownList)
        if len(self.input.keyUpList) > 0:
            print ("Keys up:", self.input.keyUpList)
        if len(self.input.keyPressedList) > 0:
            print ("Keys pressed:", self.input.keyPressedList)


Test().run()