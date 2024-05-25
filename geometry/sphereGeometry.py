from geometry.ellipsoidGeometry import EllipsoidGeometry

class SphereGeometry(EllipsoidGeometry):
    def __init__(self,radius=1, resolution=10):

        super().__init__(radius,radius,radius,resolution)


