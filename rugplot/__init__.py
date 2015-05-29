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


    def drawDotDash(self, which, dash_height=20, **extra):
        for m in self.markers:
            if 'n' in which:
                self.dwg.add(self.dwg.line((m.x, self.insert[1]-dash_height),
                                           (m.x, self.insert[1]), **extra))

            if 's' in which:
                self.dwg.add(self.dwg.line((m.x, self.insert[1] + self.size[1]),
                                           (m.x, self.insert[1] + self.size[1] + dash_height), **extra))

            if 'e' in which:
                self.dwg.add(self.dwg.line((self.insert[0] + self.size[0], m.y),
                                           (self.insert[0] + self.size[0] + dash_height, m.y), **extra))

            if 'w' in which:
                self.dwg.add(self.dwg.line((self.insert[0] - dash_height, m.y),
                                           (self.insert[0], m.y), **extra))
                




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
