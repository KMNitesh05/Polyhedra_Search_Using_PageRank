import sys
import numpy as np
import matplotlib.mlab as mlab
#from dump import dump
import seaborn as sns
#from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator 
plt.style.use('classic')
import plotly.plotly as py
import plotly.tools as tls
import os, sys

plt.style.use('classic')
inputfile = sys.argv[1]
infile = open(inputfile, 'r')
lines = infile.readlines()
lengthfile = len(lines)
infile.close()
poly = []
dist = []
a = []
b = []
c = []
d = []
e = []

for i in xrange(0,lengthfile):
	poly.append(float(lines[i].split()[0][:-1]))
	dist.append(float(lines[i].split()[1][:-1])) 


for i in xrange(0,lengthfile):
	print int(poly[i])
	if int(poly[i]) == 4 : 
		a.append(dist[i])

for i in xrange(0,lengthfile):
	print int(poly[i])
	if int(poly[i]) == 5 : 
		b.append(dist[i])

for i in xrange(0,lengthfile):
	print int(poly[i])
	if int(poly[i]) == 6 : 
		c.append(dist[i])


for i in xrange(0,lengthfile):
	print int(poly[i])
	if int(poly[i]) == 7 : 
		d.append(dist[i])

for i in xrange(0,lengthfile):
	print int(poly[i])
	if int(poly[i]) == 8 : 
		e.append(dist[i])	



num_bins = 20
#sns.set_style('darkgrid')
sns.distplot(a, hist=False)
sns.distplot(b)
sns.distplot(c, hist=False)
sns.distplot(d, hist=False)
sns.distplot(e, hist=False)
#n, bins, patches = plt.hist(a, num_bins, facecolor='blue', alpha=0.5, density = True)
#plt.plot(a, 'r--')
plt.xlabel('Distance')
plt.ylabel('Density')
plt.title(r'Histogram of Distance between density of Polyhedra eligible Solvation shell atoms')
plt.savefig('plot_multiple.pdf', bbox_inches='tight', ppi=1200)
#np.savetxt('list_sorted.csv', a )	

	 



