from geometry.parametricSurfaceGeometry import ParametricSurfaceGeometry

class PlaneGeometry(ParametricSurfaceGeometry):
    def __init__(self,width=1,height=1,resolution=8):
        def f(u,v):
            return [u,v,0]
        super().__init__(-width/2,width/2,resolution,-height/2,height/2,resolution,f)
