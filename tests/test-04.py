from core.base import Base

class Test(Base):
    def initialize(self):
        print("Initializing...")


    def update(self):
        pass
        


Test().run()