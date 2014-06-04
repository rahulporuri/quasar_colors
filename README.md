This reporitory contains codes related to my work over the summer of 2013 under the guidance of Prof. Anand Narayanan at IIST, Trivandrum, India.

Colors of quasars can be used to estimate their redshift. Richards et al (2001) studies the accuracy of this method. My work over the summer of 2013 was to reproduce these results. Putting together the original data set was harder than expected so i downloaded a more up-to-date data set by querying the DR9 using the limits on u, g, r, i & z magnitudes set by the original paper. Querying DR9 or DR10 for that matter was a bit taxing my system so it is suggested the query is run through SDSS CASjobs instead. The final data set ended up being a csv file ~20 MB in size with ~150,000 rows and 12 columns, so in hind sight, it was a bad decision letting firefox open this in the browser.

(Part of) The original data set is available on [VizieR](http://vizier.cfa.harvard.edu/viz-bin/Cat?cat=J%2FAJ%2F121%2F2308&target=brief&) for download. It can be viewed on [Simbad](http://simbad.harvard.edu/simbad/sim-ref?querymethod=bib&simbo=on&submit=submit+bibcode&bibcode=2001AJ....121.2308R) and [NED](http://ned.ipac.caltech.edu/cgi-bin/nph-objsearch?search_type=Search&refcode=2001AJ....121.2308R). The readme file helps.

The sql query file is available in the directory under the same name. To understand the syntax, one should go through the SDSS Schema browser.

colors.png is the u-g, g-r, r-i and i-z color vs redshift plot.

colors.py is the python script to generate the figure. NOTE : pandas needs to be installed for the script to run.

colors_of _quasars.ipynb is an ipython notebook regarding the same.
you can access the ipython notebook using nbviewer [here](http://nbviewer.ipython.org/github/rahulporuri/quasar_colors/blob/master/colors_of_quasars.ipynb)

work so far - 

* sql query
* downloaded data
* histogram of redshift
* python script, ipynb notebook and colors
* original data uploaded.
* median color code - not yet tested!
* python_history file added which includes notes on numpy,matplotlib,atpy,pyfits,astropy,pandas,csv and other interesting libraries.

* data on the anomolous (vertically aligned) data points in the color-redshift relations have been reacquired, plotted on the sky.
* their spectra were initially studied to reveal stellar nature but their classification/confirmation as quasars still aludes me!

to be done - 

* template spectrum and simulated color-redshift relation
* variation from the median color

* plot the spatial distribution of the quasars. replicate the plot available on the sdss site.

for help with markdown, refer to the [*mastering markdown guide*](https://guides.github.com/features/mastering-markdown/) by github.
