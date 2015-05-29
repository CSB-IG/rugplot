import numpy as np
import svgwrite, random
from rugplot import CircleMarker, Scatter

N = 12
w = np.random.rand(N)
x = np.random.rand(N)
y = np.random.rand(N)
z = np.random.rand(N)

markers = []
for i in range(N):
    markers.append(CircleMarker(x=x[i], y=y[i], r=2.5,
                                fill=random.choice(['black', 'purple', 'grey','blue', 'green', 'blue', 'orange', 'red', 'brown'])))

s = Scatter(x, y, markers, insert=(100,30), size=(200,200))
s.drawBorder(stroke='grey', fill='white', stroke_width=0.4)
s.drawMarkers()
s.drawDotDash(['e','s'], dash_height=10, stroke="grey", stroke_width=0.4)


s1 = Scatter(w, y, markers, insert=(320,30), size=(350,200))
s1.drawBorder(stroke='grey', fill='white', stroke_width=0.4)
s1.drawMarkers()
s1.drawDotDash(['w'], dash_height=10, stroke="grey", stroke_width=0.4)


s2 = Scatter(x, z, markers, insert=(100,250), size=(200,300))
s2.drawBorder(stroke='grey', fill='white', stroke_width=0.4)
s2.drawMarkers()
s2.drawDotDash(['n','e', 'w'], dash_height=10, stroke="grey", stroke_width=0.4)


rug = svgwrite.Drawing('example.svg')
rug.add(s.dwg)
rug.add(s1.dwg)
rug.add(s2.dwg)
rug.save()
