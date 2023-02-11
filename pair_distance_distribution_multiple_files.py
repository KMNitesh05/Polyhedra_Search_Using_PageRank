import sys
import numpy as np
#from dump import dump
#from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator 
plt.style.use('classic')
import plotly.plotly as py
import plotly.tools as tls
import os, sys
import matplotlib.mlab as mlab
#from dump import dump
import seaborn as sns
print "molecule_name, start_snap, end_snap, deltaT"
print "eg. WATER/OCTA_OH, 0, 10000, 2"

plt.style.use('classic')
n = 15
m = 100000
mole_name = sys.argv[1]
#mole_name2 = sys.argv[5]
#mole_name3 =sys.argv[6]
time_b = int(sys.argv[2])  #0
time_e = int(sys.argv[3])  #10000
delta_t = int(sys.argv[4]) #1
t= time_b
a = []
b = []
c = []
d = []
e = []
f = []
h = []
while t <= time_e:
	with open(mole_name + str(t) + '.input.pdfs.csv','r') as inputfile:
		print(t)
		lines = inputfile.readlines()
		lengthfile = len(lines)
		inputfile.close()
		poly = []
		dist = []
		for i in xrange(0,lengthfile):
			poly.append(float(lines[i].split()[0][:-1]))
			dist.append(float(lines[i].split()[1][:-1])) 

		for i in xrange(0,lengthfile):
			poly.append(float(lines[i].split()[0][:-1]))
			dist.append(float(lines[i].split()[1][:-1])) 

		g = []
		for i in xrange(0,lengthfile):
			print int(poly[i])
			if int(poly[i]) == 6 : 
				g.append(int(poly[i]))
				print g 
				a.append(dist[i])
		f.append(t)		
		h.append(len(g))

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



	t += delta_t

num_bins = 20
#sns.set_style('darkgrid')
#sns.distplot(a, hist=False)
#sns.distplot(b)
#sns.distplot(c, hist=False)
#sns.distplot(d, hist=False)
#sns.distplot(e, hist=False)
#sns.kdeplot(e,e shade=True);
with sns.axes_style("white"):
    sns.jointplot(e,e, kind="hex");
#with sns.axes_style("white"):
    #sns.jointplot(a,a, kind="kde");    
#n, bins, patches = plt.hist(a, num_bins, facecolor='blue', alpha=0.5, density = True)
#plt.plot(a, 'r--')
#plt.xlabel('Distance')
#plt.ylabel('Density')
#plt.title(r'Histogram of Distance between density of Polyhedra eligible Solvation shell atoms')
plt.savefig('plot_multiple_2d_8_jointplot.pdf', bbox_inches='tight', ppi=1200)
#np.savetxt('number_of6_with_time.csv', zip(f,h), delimiter=',', fmt='%f')	

	 



