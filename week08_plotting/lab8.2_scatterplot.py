# Author: Andrew Beatty
# Reproduced by: Elaine Cazetta
# This program plots the function y = x2

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array(range(1,101))
ypoints = xpoints * xpoints #multiply each entry by itself

plt.plot(xpoints, ypoints)
plt.show()
plt.savefig('lab8.2.2_scatterplot.png')