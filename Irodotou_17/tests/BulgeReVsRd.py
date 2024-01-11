# Imports #
import h5py
import numpy as np
import matplotlib.pyplot as plt
import time

# date_string = time.strftime("%d\%m\%y\%H%M")

# Read in parameters #
# outputDir = '/Users/Bam/Astronomy PhD/L-Galaxies/outputs/ALL_ON/output/'
snap = '58'
# firstFile = 0
# lastFile = 19

# First determine the size of the arrays that we need to hold the data #
nGal = 0
for iFile in range(firstFile, lastFile + 1):
    # The following line closes the file at the end of the loop
    with h5py.File(outputDir + filePrefix + '%i' % iFile + filePostfix, 'r') as f:
        nGal += len(f[snap])

# Declare numpy arrays to hold the data #
IDBulgeMass = np.empty(nGal)
BulgeMass = np.empty(nGal)
StellarMass = np.empty(nGal)
DiskMass = np.empty(nGal)
HalfLightRadius = np.empty(nGal)
DiskRadius = np.empty(nGal)

# Read in the data #
iGal = 0
for iFile in range(firstFile, lastFile + 1):
    # The following line closes the file at the end of the loop
    with h5py.File(outputDir + filePrefix + '%i' % iFile + filePostfix, 'r') as f:
        nGalFile = len(f[snap])
        IDBulgeMass[iGal:iGal + nGalFile] = f[snap]['InstabilityDrivenBulgeMass']
        DiskRadius[iGal:iGal + nGalFile] = f[snap]['DiskRadius']
        BulgeMass[iGal:iGal + nGalFile] = f[snap]['BulgeMass']
        DiskMass[iGal:iGal + nGalFile] = f[snap]['DiskMass']
        StellarMass[iGal:iGal + nGalFile] = f[snap]['StellarMass']
        HalfLightRadius[iGal:iGal + nGalFile] = f[snap]['StellarHalfLightRadius']
        iGal += nGalFile

# Physical units #
hubble = 0.678
VelocityUnits = 1  # [Km/s]
LengthUnits = 1e3 / hubble  # [Kpc]
MassUnits = 1e10 / hubble  # [Msun]
SpinUnits = 1e3 / hubble  # [Km/s * Kpc]

# ID bulge dominated #
indexID = np.where((BulgeMass > 0.5 * StellarMass) & (IDBulgeMass > 0.5 * BulgeMass))

# Data #
Bulge_Mass = BulgeMass[indexID] * MassUnits
Stellar_Mass = StellarMass[indexID] * MassUnits
Half_Light_Radius = HalfLightRadius[indexID] * LengthUnits
Disk_Scale_Length = DiskRadius[indexID] * LengthUnits / 3.

# Generate initial figure #
plt.close()
plt.figure(1, figsize=(18, 10))

# Scatter plot parameters #
plt.xlabel(r'$\mathrm{R_{d}\; [Kpc]}$', fontsize=30)
plt.ylabel(r'$\mathrm{R_{e}\; [Kpc]}$', fontsize=30)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.xlim(1e-1, 1e1)
plt.ylim(6e-2, 1e1)
plt.xscale('log')
plt.yscale('log')

# Plotting L-Galaxies data #
plt.scatter(Disk_Scale_Length, Half_Light_Radius, c='b', s=10, label="$\mathrm{Pseudo}$", zorder=2)

# Plot observational data #
VBM15 = np.genfromtxt('VBM15.csv', delimiter=',', names=['x', 'y'])
plt.scatter(np.power(10, VBM15['x']), np.power(10, VBM15['y']), color='g', marker='p', s=300, label="Vaghmare+15")

plt.legend(loc=2, fancybox='True', shadow='True', fontsize=20, markerscale=1)
plt.savefig('BulgeReVsRd-' + date + '.png')