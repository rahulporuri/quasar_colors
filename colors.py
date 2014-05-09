# -*- coding: utf-8 -*-
"""
Created on Fri May 09 17:02:45 2014

@author: rahul.poruri
"""

import matplotlib.pyplot as plt
import pandas as pd

# pandas is a library used to work with huge data sets.
# it is not installed by default and is a very heavy library.
# it was used primarily because there exist pre-defined functions in pandas
# which are very powerful, like the ability to import data 
# using the column name, as is shown below.

# a more generic implementation will be done in the future.

data = pd.read_csv('quasar_colors_rahul.poruri.csv')

redshift = []
u, g, r, i, z = [], [], [], [], []
u_g, g_r, r_i, i_z = [], [], [], []

# u_g is the colo u-g and so on, for the other 3 colors g-r, r-i and i-z.

redshift = data['z']
u, g, r, i, z = data['modelMag_u'], data['modelMag_g'], data['modelMag_r'], data['modelMag_i'], data['modelMag_z']
u_g, g_r, r_i, i_z = data['modelMag_u'] - data['modelMag_g'], data['modelMag_g'] - data['modelMag_r'], data['modelMag_r'] - data['modelMag_i'], data['modelMag_i'] - data['modelMag_z']

# the arguments modelMag_* are the column names in the file *.csv

plt.hold(True)

subplot(221)
plt.ylim(-4,5)
plt.scatter(redshift, u_g, s=4)
plt.ylabel('u-g')

subplot(222)
plt.ylim(-4,5)
plt.scatter(redshift, g_r, s=4)
plt.ylabel('g-r')

subplot(223)
plt.ylim(-4,5)
plt.scatter(redshift, r_i, s=4)
plt.ylabel('r-i')
plt.xlabel('redshift')

subplot(224)
plt.ylim(-4,5)
plt.scatter(redshift, i_z, s=4)
plt.ylabel('i-z')
plt.xlabel('redshift')

plt.show()