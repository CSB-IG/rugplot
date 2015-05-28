import numpy as np
from rugplot import *


N = 50
x = np.random.rand(N)
y = np.random.rand(N)

markers = [CircleMarker(x=x[i], y=y[i], r=3, fill='red', stroke='blue') for i in range(0,N)]

s = Scatter(markers, (10,10), (300,200), stroke='black', fill='white')
s.draw()
s.dwg.filename='example.svg'
s.dwg.save()
