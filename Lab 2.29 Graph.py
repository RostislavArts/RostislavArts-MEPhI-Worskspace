import matplotlib.pyplot as plt
import numpy as np

import matplotlib as mpl

fig, ax = plt.subplots()

#data for errors
err1 = [0, 0.04, 0.04, 0.05, 0.06, 0.07, 0.08]
err2 = [0, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08]
err3 = [0, 0.03, 0.04, 0.04, 0.05, 0.06, 0.07]

ax.set_xlabel('τ, sec')
ax.set_ylabel('lg(H3\')')

# graph 1
ax.errorbar([0, 3.03, 6.25, 8.96, 12.1, 15.23, 18.03], [1.733, 1.62, 1.56, 1.51, 1.45, 1.32, 1.28], yerr = err1, color = 'red', ecolor = 'lightcoral', fmt = 'x')
ax.axline((0, 1.733), slope = -0.024, color="red", label = 'H1 = 200mm')

#graph 2
ax.errorbar([0, 3.16, 6.20, 9.18, 12.03, 15.25, 17.94], [1.75, 1.66, 1.58, 1.52, 1.45, 1.36, 1.3], yerr = err2, color = 'green', ecolor = 'lightgreen', fmt = 'x')
ax.axline((0, 1.75), slope = -0.024, color="green", label = 'H1 = 210mm')

#graph 3
ax.errorbar([0, 3.16, 5.94, 9.12, 12.19, 15, 18.09], [1.779, 1.68, 1.62, 1.56, 1.48, 1.4, 1.32], yerr = err3, color = 'blue', ecolor = 'lightblue', fmt = 'x')
ax.axline((0, 1.779), slope = -0.024, color="blue", label = 'H1 = 220mm')

#border lines for graph 2
ax.axline((3.16, 1.69), (17.94, 1.22), color="grey")
ax.axline((3.16, 1.63), (17.94, 1.38), color="grey")

#misc settings
ax.grid()
ax.legend()

plt.show()