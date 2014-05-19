import matplotlib.pyplot as plt
import pyfits as pf

spec_plot(file):
	hdulist = pf.open(file)
	print hdulist.info()
	print len(hdulist[1].data)
	flux = []
	loglam = []

	for i in xrange(len(hdulist[1].data)):
		tmp = (hdulist[1].data)[i][0:1]
		flux.append(tmp)
		temp = (hdulist[1].data)[i][1:2]
		loglam.append(temp)

	print len(flux)
	print len(loglam)

	plt.plot(loglam, flux,lw=0.3)