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

print "molecule_name, start_snap, end_snap, deltaT"
print "eg. WATER/OCTA_OH, 0, 10000, 2"


mole_name = sys.argv[1]
mole_name2 = sys.argv[5]
mole_name3 =sys.argv[6]
n = 7205 
time_b = int(sys.argv[2])  #0
time_e = int(sys.argv[3])  #10000
delta_t = int(sys.argv[4]) #1
t= time_b
amsum = []
while t <= time_e:
    with open(mole_name + str(t) + mole_name2 + mole_name3 + str(t) + '.xyz.' + mole_name3 + str(t) + '.xyz.' + 'GraphGeod','r') as inputfile:
        print(t)
        lines = inputfile.readlines()
        lengthfile = len(lines)
        inputfile.close()
        edge_u = []
        edge_v = []
        for i in xrange(0, lengthfile):
            #if (lines[i].find('# Fix ') != -1):
            edge_u.append(int(lines[i].split()[0]))
            edge_v.append(int(lines[i].split()[1]))
        adjMatrix = [[0 for i in range(n)] for k in range(n)]
        for i in range(len(edge_u)):
            u = edge_u[i]
            v = edge_v[i]
            print u,v
            adjMatrix[u-1][v-1] = 1
            adjMatrix[v-1][u-1] = 1
        
        #print("Adjacency matrix: ")
        #printMatrix(adjMatrix)	
        for i in range(n):
            sum_rows = np.sum(adjMatrix[i][0:])
            amsum.append(sum_rows)
    t += delta_t
plt.hist(amsum, bins='auto')
plt.savefig('amsum.pdf', bbox_inches='tight', ppi=1200)
np.savetxt('amsum.csv',amsum)


























	
	
	
	


 


	
	









#sum_rows = np.sum(adjMatrix , axis=1)


	

   

#np.savetxt('amsum.csv',amsum)




















### PLOTTING
#NUM = len(Time)
#conv_step = 50
#conv_pont = NUM/conv_step

#sum_step_300K = []
#for i in xrange(conv_pont):
    
    #sum_step_300K.append((i*conv_step, np.mean(SurfTen_300K[:i*conv_step])/20.))
    

#sum_step_300K = np.array(sum_step_300K)

#plt.plot(sum_step_300K[:, 0], sum_step_300K[:, 1], label='T=300K', color='green', linewidth=1.0)

#plt.legend(loc='lower right', fontsize=14)
#plt.xlabel(r'Time (ps)', fontsize=12)
#plt.ylabel(r'r (mN/m)', fontsize=12)
#plt.ylim(2, 23)
#plt.xlim(230, 350)
#plt.savefig('SurfTens_Converge_Temp300.pdf', bbox_inches='tight', ppi=1200)

"""
print "average value of interfacial tension"
print X_av, Y_av, WAT_av, TRIBP_av, MainWAT_av, ExtWAT_av

#ax = plt.figure().gca() 
#ax.yaxis.set_major_locator(MaxNLocator(integer=True))

fig, left_axis = plt.subplots()
right_axis = left_axis.twinx()

left_axis.errorbar(N, X, yerr=Y, fmt='.-', label='$Interface Tension$', color="red", linewidth=1.)
#left_axis.plot(N, X, '.-', label='Interfacial Tension', color="blue", linewidth=1.)
right_axis.plot(N, TRIBP, '*-', label='$N_{TBP}$', color="black", linewidth=1.)

left_axis.set_xlabel(r'$T{}$ (K)', fontsize=14)
left_axis.set_ylabel(r'$r{} (mN/m)$', fontsize=14)
right_axis.set_ylabel('Interfacial TBP', fontsize=13)

left_axis.set_xlim(230, 350)
left_axis.set_ylim(5, 35)
right_axis.set_ylim(180, 270)

#ax.plot(N, X, '.-', label='Interfacial Tension', color="blue", linewidth=1.)
#ax.errorbar(N, X, yerr=Y, fmt='.-', color="red", linewidth=1.)
#ax.plot(N, WAT, 'v-', label='$N_{water}$', color="blue", linewidth=1.)
#ax.plot(N, MainWAT, '^-', label='$N_{interfacial-water}$', color="lightblue", linewidth=1.)
#ax.plot(N, ExtWAT, '+-', label='$N_{extracted-water}$', color="blue", linewidth=1.)
#ax.plot(N, TRIBP, '*-', label='$N_{TBP}$', color="black", linewidth=1.)
#ax.set_xlabel(r'$T{}$ (K)')
#ax.set_ylabel(r'$r{} (mN/m)$', fontsize=14)
plt.legend(loc="upper right")
#plt.ylim(2, 23)
#plt.xlim(230, 350)
plt.savefig('SurfTen_TBPconcent.pdf', bbox_inches='tight', ppi=1200)
"""
