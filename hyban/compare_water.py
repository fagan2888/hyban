#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import numpy as np
import matplotlib.pyplot as plt
from utils import *

# -- set the indices for comparison
ind = np.array([215, 256, 297])

# -- get scan conditions
sc = get_scan_conditions().iloc[ind]

# -- read in the scans
cubes = [read_hyper(os.path.join("..", "data", i)) for i in sc.filename]

# -- get rgb images
print("generating rgbs...")
rgbs = [make_rgb8(i.data, i.waves) for i in cubes]

# -- plot the three scans
fig, ax = plt.subplots(3, 1, figsize=(5, 8))
fig.subplots_adjust(0.05, 0.05, 0.95, 0.95)
dum     = [i.axis("off") for i in ax]
dum     = [i.imshow(j, aspect=0.45) for i, j in zip(ax, rgbs)]
dum     = [i.set_title(j) for i, j in zip(ax, sc.time)]
fig.canvas.draw()

# -- set the spatial indices
rr = [1110, 1460]
cc = [1355, 1430]

# -- get the spectra
specs = [i.data[:, rr[0]:rr[1], cc[0]:cc[1]].mean(-1).mean(-1) for i in cubes]

# figure()
# plot(cubes[0].waves, i) for i in specs]