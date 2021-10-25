# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 15:55:40 2021

@author: Adhimar
"""

import numpy as np
from matplotlib import pyplot as plt

data=np.loadtxt('map.txt', skiprows=1)
position = data[:,0]
Temperature = data[:,1]


heatmap = np.empty((3, len(position)))

for i in range(3):
    for j in range(len(position)):
        heatmap[i,j] = Temperature[j]
        
fig = plt.figure()
ax = fig.add_subplot(111)
im = ax.imshow(heatmap, cmap='jet', aspect='auto')
ax.set_yticks(range(3))
ax.set_yticklabels(['1','0','-1'])
#ax.set_xticks(position)
ax.set_xlabel('x(cm)')
ax.set_ylabel('y(cm)')
cbar = fig.colorbar(ax=ax, mappable=im, orientation='horizontal')
cbar.set_label('Temperature, $^\circ\mathrm{C}$')
plt.show()
plt.savefig('Temperature.png', dpi=600)