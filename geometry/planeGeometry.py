from geometry.parametricSurfaceGeometry import ParametricSurfaceGeometry

class PlaneGeometry(ParametricSurfaceGeometry):
    def __init__(self):
        def f(u,v):
            return [u,v,0]
        super().__init__(-1,1,8,-1,1,5,f)