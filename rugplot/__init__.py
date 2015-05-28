import svgwrite
from svgwrite import cm, mm


class Rug:
    def __init__(self):
        pass    




class Scatter:
    def __init__(self, markers, insert, size, **extra):
        self.dwg     = svgwrite.Drawing()
        self.markers = markers
        self.dwg.add(self.dwg.rect(insert=insert, size=size, **extra))

    def draw(self):
        for m in self.markers:
            self.dwg.add(m.getDwg())            

        


class CircleMarker:

    def __init__(self, x=0, y=0, r=1, **extra):
        self.dwg    = svgwrite.Drawing()
        self.x      = x
        self.y      = y
        self.r      = r
        self.extra  = extra

    def draw(self):
        self.dwg.add(self.dwg.circle(center=(self.x, self.y),
                                     r=self.r, **self.extra))
        
    def getDwg(self):
        return self.dwg
