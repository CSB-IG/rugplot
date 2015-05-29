import svgwrite
from svgwrite import cm, mm


class Rug:
    def __init__(self):
        pass    




class Scatter:
    def __init__(self, x, y, markers, insert, size):

        assert len(x) == len(y) == len(markers)

        self.x = x
        self.y = y
        self.markers = markers

        self.insert = insert
        self.size   = size
        self.dwg    = svgwrite.Drawing()        


    def drawBorder(self, **extra):
        # draw enclosing rectangle
        self.dwg.add(self.dwg.rect(insert=self.insert, size=self.size, **extra))

        
    def drawMarkers(self):
        for i in range(len(self.markers)):
            m   = self.markers[i]
            # set coords for mark
            m.x = ((self.x[i] / self.x.max()) * self.size[0]) + self.insert[0]
            m.y = ((self.y[i] / self.y.max()) * self.size[1]) + self.insert[1]
            # add it
            self.dwg.add(m.getDwg())            


    def drawDotDash(self, which):
        for m in self.markers:
            if 'n' in which:
                self.dwg.add(self.dwg.line((m.x, self.insert[1]), (m.x, self.insert[1]+10), stroke="black", stroke_width="1"))
                




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
        self.draw()
        return self.dwg
