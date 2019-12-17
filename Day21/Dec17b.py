import plotly.graph_objects as gro
import numpy as np

x = np.array([1,2,3,4,5])
y = np.array([2,1,4,1,3])

myFig = gro.Figure(
        data = gro.Bar(x= x, y= y))

# myFig.show()

'''
Save to html
'''
myFig.write_html("plotlyTes.html", auto_open=True)