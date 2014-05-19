import numpy as np

for i in xrange(len(a)):
	for j in xrange(len(red)):
		if a[i] - 0.0375 < red[j] < a[i] + 0.0375 :
			tmp = u_g[j]
			mid_u_g.append(tmp)
	tmp = np.median(mid_u_g)
	med_u_g.append(tmp)
	mid_u_g=[]