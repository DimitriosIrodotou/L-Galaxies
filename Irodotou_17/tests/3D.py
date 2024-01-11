# Imports #
import h5py
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import time
from random import randint

date_string = time.strftime("%d\%m\%y\%H%M")

# Read in parameters #
outputDir = '/Users/Bam/Astronomy PhD/L-Galaxies/outputs/NO_BHG/output/'
filePrefix = 'SA_output_'
filePostfix = '.h5'
snap = '58'
firstFile = 0
lastFile = 19

# First determine the size of the arrays that we need to hold the data #
nGal = 0
for iFile in range(firstFile, lastFile + 1):
    # The following line closes the file at the end of the loop
    with h5py.File(outputDir + filePrefix + '%i' % iFile + filePostfix, 'r') as f:
        nGal += len(f[snap])

# Declare numpy arrays to hold the data #
MDBulgeMass = np.empty(nGal)
MiMDBulgeMass = np.empty(nGal)
MaMDBulgeMass = np.empty(nGal)
IDBulgeMass = np.empty(nGal)
DiskMass = np.empty(nGal)
StellarMass = np.empty(nGal)
NMajor = np.empty(nGal)
NMinor = np.empty(nGal)

# Read in the data #
iGal = 0
for iFile in range(firstFile, lastFile + 1):
    # The following line closes the file at the end of the loop
    with h5py.File(outputDir + filePrefix + '%i' % iFile + filePostfix, 'r') as f:
        nGalFile = len(f[snap])
        IDBulgeMass[iGal:iGal + nGalFile] = f[snap]['InstabilityDrivenBulgeMass']
        MaMDBulgeMass[iGal:iGal + nGalFile] = f[snap]['MaMergerDrivenBulgeMass']
        MiMDBulgeMass[iGal:iGal + nGalFile] = f[snap]['MiMergerDrivenBulgeMass']
        MDBulgeMass[iGal:iGal + nGalFile] = f[snap]['MergerDrivenBulgeMass']
        DiskMass[iGal:iGal + nGalFile] = f[snap]['DiskMass']
        StellarMass[iGal:iGal + nGalFile] = f[snap]['StellarMass']
        NMajor[iGal:iGal + nGalFile] = f[snap]['NMajorMergers']
        NMinor[iGal:iGal + nGalFile] = f[snap]['NMinorMergers']
        iGal += nGalFile

# Physical units #
hubble = 0.678
VelocityUnits = 1  # [Km/s]
LengthUnits = 1e3 / hubble  # [Kpc]
MassUnits = 1e10 / hubble  # [Msun]
SpinUnits = 1e3 / hubble  # [Km/s * Kpc]

# Data #
Disk_Mass = DiskMass * MassUnits
ID_Bulge_Mass = IDBulgeMass * MassUnits
MD_Bulge_Mass = (MaMDBulgeMass + MiMDBulgeMass + MDBulgeMass) * MassUnits
Stellar_Mass = StellarMass * MassUnits

Disk_Ratio = np.divide(Disk_Mass, Stellar_Mass)
ID_Ratio = np.divide(ID_Bulge_Mass, Stellar_Mass)
MD_Ratio = np.divide(MD_Bulge_Mass, Stellar_Mass)

# Bins for histogram and plotting
binperdex = 5
xrange = np.array([7, 12])
nbin = (xrange[1] - xrange[0]) * binperdex

Stellar_Mass = np.log10(Stellar_Mass)

colors = []

for i in range(int(max(NMajor)) + 1):
    colors.append('#%06X' % randint(0, 0xFFFFFF))

plt.close()
fig = plt.figure(1, figsize=(18, 10))
ax = fig.add_subplot(111, projection='3d')

ax.set_xlim(0, 13)
ax.set_ylim(8, 12)
ax.set_zlim(0, 1.2)

ax.set_xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])

ax.set_xlabel(r'$\mathrm{Number\, of\ major\, mergers}$', fontsize=15)
ax.set_ylabel(r'$\mathrm{log_{10}(M_{\star}\; [M_{\odot}])}$', fontsize=15)
ax.set_zlabel(r'$\mathrm{ID\, bulge\, mass\, /\, Total\, Stellar\, Mass}$', fontsize=15)

# ax.view_init(azim=-90)

for i in range(int(max(NMajor)) + 1):
    index = np.where(NMajor == i)
    ax.scatter(NMajor[index], Stellar_Mass[index], ID_Ratio[index], c=colors[i], depthshade=False, edgecolor='k', s=40,
               zorder=i)

for ii in range(90, -40, 5):
    ax.view_init(azim = ii)
    plt.savefig("movie%d.png" % ii)
