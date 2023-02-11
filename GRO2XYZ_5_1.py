import os, sys

print "molecule_name, start_snap, end_snap, deltaT"
print "eg. WATER/OCTA_OH, 0, 10000, 2"

mole_name = sys.argv[1]

time_b = int(sys.argv[2])  #0
time_e = int(sys.argv[3])  #10000
delta_t = int(sys.argv[4]) #1

t= time_b
while t <= time_e:
    with open(mole_name + str(t) + '.gro') as gro:
        with open(mole_name + str(t) + '.xyz','w') as xyz:
            print(t)
            for i, line in enumerate(gro):
                if i ==0:
                    pass
                elif i == 1:
                    num_atoms = int(line.split()[0])
                    xyz.write(str(num_atoms) + '\n')
                    xyz.write('\n')
                elif (i > 1) & (i < num_atoms + 2):
                    if line.split()[1] == 'O' or line.split()[1] == 'H':
                        xyz.write(line.split()[1]+' ')
                    else:
                        xyz.write(line.split()[1][:2]+' ')
                    xyz.write(str(round(1000*float(line.split()[-3]))/100)+' ')
                    xyz.write(str(round(1000*float(line.split()[-2]))/100)+' ')
                    xyz.write(str(round(1000*float(line.split()[-1]))/100)+'\n')
    t += delta_t
