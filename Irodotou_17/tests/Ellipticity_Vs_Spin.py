# Imports #
import time
import h5py
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

start_time = time.time()
date = time.strftime("%d\%m\%y\%H%M")

outputDir = '/Users/Bam/Astronomy PhD/L-Galaxies/outputs/ALL_ON/output/'
snap = '58'

# Define the number of trees #
firstFile = 0
lastFile = 19
maxFile = 512
filePostfix = '.h5'
filePrefix = 'SA_output_'

# Physical units and simulation parameters #
hubble = 0.678  # [dimensionless]
boxside = 480.28  # Units Mpc/h
VelocityUnits = 1  # [Km/s]
LengthUnits = 1e3 / hubble  # [Kpc]
MassUnits = 1e10 / hubble  # [Msun]
SpinUnits = 1e3 / hubble  # [Km/s * Kpc]

# Determine the size and declare arrays to hold the data #
nGal = 0
for iFile in range(firstFile, lastFile + 1):
    # The following line closes the file at the end of the loop
    with h5py.File(outputDir + filePrefix + '%i' % iFile + filePostfix, 'r') as f:
        nGal += len(f[snap])
    print('nGal=', nGal)

Vmax = np.empty(nGal)
DiskMass = np.empty(nGal)
CosTheta = np.empty(nGal)
DiskRadius = np.empty(nGal)
StellarMass = np.empty(nGal)
DiskSpin = np.empty(shape=(nGal, 3))

# Read in the data #
iGal = 0
for iFile in range(firstFile, lastFile + 1):
    # The following line closes the file at the end of the loop
    with h5py.File(outputDir + filePrefix + '%i' % iFile + filePostfix, 'r') as f:
        nGalFile = len(f[snap])
        DiskSpin[iGal:iGal + nGalFile] = f[snap]['DiskSpin']
        DiskMass[iGal:iGal + nGalFile] = f[snap]['DiskMass']
        Vmax[iGal:iGal + nGalFile] = f[snap]['InfallVmax']
        DiskRadius[iGal:iGal + nGalFile] = f[snap]['DiskRadius']
        CosTheta[iGal:iGal + nGalFile] = f[snap]['CosInclination']
        StellarMass[iGal:iGal + nGalFile] = f[snap]['StellarMass']
        iGal += nGalFile

Disk_Spin = np.linalg.norm(DiskSpin, axis=1)

# costheta = np.abs(np.divide(zip(*DiskSpin)[2], Disk_Spin))

ellipticity = 1 - CosTheta
Jproxy = np.divide(DiskMass * DiskRadius * Vmax, DiskMass * DiskRadius * Vmax * 1.22)

# Generate initial figure #
plt.close()
plt.figure(1, figsize=(18, 10))

# Scatter plot parameters #
# plt.xscale('log')
# plt.yscale('log')
# plt.ylim(1e1, 1e4)
# plt.xlim(1e9, 1e12)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.tick_params(direction='in', which='both', top='on', right='on')
plt.xlabel(r'$\mathrm{M_{\star,D.}\; [M_{\odot}]}$', fontsize=30)
plt.ylabel(r'$\mathrm{|J_{\star,D.}|\; [Km*s^{-1}*Kpc]}$', fontsize=30)

# Plot L-Galaxies data #
plt.scatter(ellipticity, Jproxy, c='k', s=10, label="$\mathrm{M_{\star,d} / M_{\star,total}> 0.5}$")
plt.savefig('1-' + snap + date + '.png')