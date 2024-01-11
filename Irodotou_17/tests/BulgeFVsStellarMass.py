# Imports #
import h5py
import numpy as np
import matplotlib.pyplot as plt
import time
from operator import itemgetter
date_string = time.strftime("%d\%m\%y\%H%M")

# Read in parameters #
outputDir = '/Users/Bam/Astronomy PhD/L-Galaxies/outputs/NO_BHG/'
filePrefix = 'SA_output_'
filePostfix = '.h5'
snap = '58'
firstFile = 0
lastFile = 9
maxFile = 512

# First determine the size of the arrays that we need to hold the data #
nGal = 0
for iFile in range(firstFile, lastFile + 1):
    # The following line closes the file at the end of the loop
    with h5py.File(outputDir + filePrefix + '%i' % iFile + filePostfix, 'r') as f:
        nGal += len(f[snap])
# Declare numpy arrays to hold the data #
MMDBulgeMass = np.empty(nGal)
mMDBulgeMass = np.empty(nGal)
MDBulgeMass = np.empty(nGal)
IDBulgeMass = np.empty(nGal)
BulgeMass = np.empty(nGal)
StellarMass = np.empty(nGal)


# Read in the data #
iGal = 0
for iFile in range(firstFile, lastFile + 1):
    # The following line closes the file at the end of the loop
    with h5py.File(outputDir + filePrefix + '%i' % iFile + filePostfix, 'r') as f:
        nGalFile = len(f[snap])
        IDBulgeMass[iGal:iGal + nGalFile] = f[snap]['InstabilityDrivenBulgeMass']
        MMDBulgeMass[iGal:iGal + nGalFile] = f[snap]['MaMergerDrivenBulgeMass']
        mMDBulgeMass[iGal:iGal + nGalFile] = f[snap]['MiMergerDrivenBulgeMass']
        MDBulgeMass[iGal:iGal + nGalFile] = f[snap]['MergerDrivenBulgeMass']
        BulgeMass[iGal:iGal + nGalFile] = f[snap]['BulgeMass']
        StellarMass[iGal:iGal + nGalFile] = f[snap]['StellarMass']
        iGal += nGalFile

# Physical units #
hubble = 0.678
VelocityUnits = 1  # [Km/s]
LengthUnits = 1e3 / hubble  # [Kpc]
MassUnits = 1e10 / hubble  # [Msun]
SpinUnits = 1e3 / hubble  # [Km/s * Kpc]

dDiskMag = 0.3

Gals = zip(IDBulgeMass,MMDBulgeMass,mMDBulgeMass,MDBulgeMass,BulgeMass,StellarMass)
Gals2 = sorted(Gals,key=itemgetter(5))

# MD bulge dominated #
MD = (MMDBulgeMass + MDBulgeMass + mMDBulgeMass)
Stellar_Mass = StellarMass
# Data #
# Split the stellar, bulge, ID and MD masses into bins
for x in range(10, 50):
    if len(StellarMass) % x == 0:
        Stellar_Mass = np.split(StellarMass, x)
        Bulge_Mass = np.split(BulgeMass, x)
        MD = np.split(MD, x)
        ID_Bulge_Mass = np.split(IDBulgeMass, x)
        break

# Create 2d arrays to count the amount of ID and MD bulges
i = np.zeros([x, len(Stellar_Mass[0])])
j = np.zeros([x, len(Stellar_Mass[0])])
mean = np.zeros([x, len(Stellar_Mass[0])])
width = np.zeros(x)

# Store how many ID and MD bulges are in each bin
for y in range(0, x):
    for z in range(0, len(Stellar_Mass[0])):
        if MD[y][z] > 0.7 * Bulge_Mass[y][z]:
            i[y][z] = 1.
        if ID_Bulge_Mass[y][z] > 0.7 * Bulge_Mass[y][z]:
            j[y][z] = 1.

i = np.sum(i, axis=1)
j = np.sum(j, axis=1)

for l in range(0, x):
    width[l] = max(Stellar_Mass[l]) - min(Stellar_Mass[l])

Stellar_Mass = (np.sum(Stellar_Mass, axis=1) / len(Stellar_Mass[0])) * MassUnits
RatioMD = i / (i + j)
RatioID = j / (i + j)

# Generate initial figure #
plt.close()
plt.figure(1, figsize=(18, 10))

# Scatter plot parameters #
plt.title(r'$\mathrm{Dependence\; of\; classical/pseudo\; bulge\; fraction\; on\; host\; galaxy\; stellar\; mass.}$',
          fontsize=30)

plt.xlabel(r'$\mathrm{log(M_{\star}\; [M_{\odot}])}$', fontsize=30)
plt.ylabel(r'$\mathrm{Fraction\; of\; bulge\; type}$', fontsize=30)

# plt.xscale('log')
#
# plt.xlim(1e8, 1e12)
# plt.ylim(0, 1.2)

plt.xticks(fontsize=20)
plt.yticks(fontsize=20)

plt.grid(True, which="both", c='k')

# Plotting data #

plt.bar(Stellar_Mass, RatioMD, align='center')
# plt.scatter(Stellar_Mass1, Stellar_Mass1, c='b', s=10, label="$\mathrm{Pseudo\, bulges}$", zorder=2)
# plt.scatter(Stellar_Mass2, Stellar_Mass2, c='r', s=10, label="$\mathrm{Classical\, bulges}$", zorder=1)

plt.legend(loc=2, fancybox='True', shadow='True', fontsize=20, markerscale=1)
plt.savefig('BHMassVsDiskMag1-' + date_string + '.png')
