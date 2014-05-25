# -*- coding: utf-8 -*-
"""
Created on Thu May 15 23:32:03 2014
Modified on Sun May 25 13:40:xx 2014

---> a modified version has been appended to the end of this code
---> this version makes use of numpy arrays instead of solely relying 
---> on python lists, which are cumbersome and not optimied!

@author: rahul.poruri
"""

import matplotlib.pyplot as plt

fin = open("table2.dat","r")
lines = fin.readlines()

redshift = []
u, g, r, i, z = [], [], [], [], []
u_g, g_r, r_i, i_z = [], [], [], []

for j in xrange(1,len(lines)):
    tmp = lines[j][31:36]
    redshift.append(float(tmp))  
    tmp = lines[j][66:71]
    u.append(float(tmp))
    tmp = lines[j][78:83]
    g.append(float(tmp))
    tmp = lines[j][90:95]
    r.append(float(tmp))
    tmp = lines[j][101:107]
    i.append(float(tmp))
    tmp = lines[j][114:119]
    z.append(float(tmp))

for j in xrange(len(u)):
    tmp = u[j]-g[j]
    u_g.append(tmp)
    tmp = g[j]-r[j]
    g_r.append(tmp)
    tmp = r[j]-i[j]
    r_i.append(tmp)
    tmp = i[j]-z[j]
    i_z.append(tmp)

plt.hold(True)

subplot(221)
plt.ylim(-4,6)
plt.scatter(redshift, u_g, s=4)
plt.ylabel('u-g')

subplot(222)
plt.ylim(-4,6)
plt.scatter(redshift, g_r, s=4)
plt.ylabel('g-r')

subplot(223)
plt.ylim(-4,6)
plt.scatter(redshift, r_i, s=4)
plt.ylabel('r-i')
plt.xlabel('redshift')

subplot(224)
plt.ylim(-4,6)
plt.scatter(redshift, i_z, s=4)
plt.ylabel('i-z')
plt.xlabel('redshift')

plt.show()

"""

data = [line.split() for line in open('table2.dat')]

redshift = np.zeros(len(data)-1)
u, g, r, i, z = np.zeros(len(data)-1),np.zeros(len(data)-1),np.zeros(len(data)-1),np.zeros(len(data)-1),np.zeros(len(data)-1)
u_g, g_r, r_i, i_z = np.zeros(len(data)-1),np.zeros(len(data)-1),np.zeros(len(data)-1),np.zeros(len(data)-1)

for j in xrange(1,len(data)):
    redshift[j-1] = data[j][2]
    u[j-1] = data[j][10]
    g[j-1] = data[j][12]
    r[j-1] = data[j][14]
    i[j-1] = data[j][16]
    z[j-1] = data[j][18]

for j in xrange(len(u)):
    u_g[j] = u[j] - g[j]
    g_r[j] = g[j] - r[j]
    r_i[j] = r[j] - i[j]
    i_z[j] = i[j] - z[j]



plt.hold(True)

subplot(221)
plt.xlim(-1,6)
plt.ylim(-4,6)
plt.scatter(redshift, u_g, s=4)
plt.ylabel('u-g')

subplot(222)
plt.xlim(-1,6)
plt.ylim(-4,6)
plt.scatter(redshift, g_r, s=4)
plt.ylabel('g-r')

subplot(223)
plt.xlim(-1,6)
plt.ylim(-4,6)
plt.scatter(redshift, r_i, s=4)
plt.ylabel('r-i')
plt.xlabel('redshift')

subplot(224)
plt.xlim(-1,6)
plt.ylim(-4,6)
plt.scatter(redshift, i_z, s=4)
plt.ylabel('i-z')
plt.xlabel('redshift')

plt.show()

"""