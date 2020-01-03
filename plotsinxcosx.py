#Generating a sine vs cosine curve
#For this project, you will have a generate a sine vs cosine curve. 
#You will need to use the numpy library to access the sine and cosine functions. 
#You will also need to use the matplotlib library to draw the curve. 
#To make this more difficult, make the graph go from -360° to 360°, with there being a 180° difference between each point on the x-axis.

import numpy as np
import matplotlib.pyplot as plt

#x-axis
x = np.arange(-2*np.pi, 2*np.pi, 0.2)
#y-axis
siny = np.sin(x)
cosy = np.cos(x)

#-360 to 360 with 180 ticks
xloc = [-2*np.pi, -np.pi, 0, np.pi, 2*np.pi]
xlbl = [-360, -180, 0, 180, 360]

#plotting legend, titles and labels
plt.plot(x, siny, color= 'b')
plt.plot(x, cosy, color= 'g')
plt.xlabel('Degrees')
plt.ylabel('Value')
plt.title('Sine and Cosine waves between -360 to 360 Degrees')
plt.legend(['Sin(x)','Cos(x)'])
plt.xticks(xloc, xlbl)
plt.show()