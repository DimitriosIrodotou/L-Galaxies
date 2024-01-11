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
lastFile = 0

# First determine the size of the arrays that we need to hold the data #
nGal = 0
for iFile in range(firstFile, lastFile + 1):
    # The following line closes the file at the end of the loop
    with h5py.File(outputDir + filePrefix + '%i' % iFile + filePostfix, 'r') as f:
        nGal += len(f[snap])

# Declare numpy arrays to hold the data #
MDBulgeMass = np.empty(nGal)
IDBulgeMass = np.empty(nGal)


# Read in the data #
iGal = 0
for iFile in range(firstFile, lastFile + 1):
    # The following line closes the file at the end of the loop
    with h5py.File(outputDir + filePrefix + '%i' % iFile + filePostfix, 'r') as f:
        nGalFile = len(f[snap])
        IDBulgeMass[iGal:iGal + nGalFile] = f[snap]['InstabilityDrivenBulgeMass']
        MDBulgeMass[iGal:iGal + nGalFile] = f[snap]['MergerDrivenBulgeMass']
        iGal += nGalFile

# Physical units #
hubble = 0.678
VelocityUnits = 1  # [Km/s]
LengthUnits = 1e3 / hubble  # [Kpc]
MassUnits = 1e10 / hubble  # [Msun]
SpinUnits = 1e3 / hubble  # [Km/s * Kpc]

IDBulgeMass = IDBulgeMass[np.where(IDBulgeMass > 1e-4)] * MassUnits
MDBulgeMass = MDBulgeMass[np.where(MDBulgeMass > 1e-4)] * MassUnits

# Generate initial figure #
plt.close()
plt.figure(1, figsize=(18, 10))

plt.xscale('log')
plt.yscale('log')

plt.hist(MDBulgeMass, bins=100)

plt.savefig('Hist-' + date_string + '.png')
