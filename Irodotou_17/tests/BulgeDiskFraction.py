# Imports #
import h5py
import numpy as np
import matplotlib.pyplot as plt
import time
date_string = time.strftime("%d\%m\%y\%H%M")

# Read in parameters #
outputDir = '/Users/Bam/Astronomy PhD/L-Galaxies/outputs/NO_BHG/'
filePrefix = 'SA_output_'
filePostfix = '.h5'
snap = '58'
firstFile = 0
lastFile = 9

# First determine the size of the arrays that we need to hold the data #
nGal = 0
for iFile in range(firstFile, lastFile + 1):
    # The following line closes the file at the end of the loop
    with h5py.File(outputDir + filePrefix + '%i' % iFile + filePostfix, 'r') as f:
        nGal += len(f[snap])

# Declare numpy arrays to hold the data #
BulgeMass = np.empty(nGal)
DiskMass = np.empty(nGal)
StellarMass = np.empty(nGal)

# Read in the data #
iGal = 0
for iFile in range(firstFile, lastFile + 1):
    # The following line closes the file at the end of the loop
    with h5py.File(outputDir + filePrefix + '%i' % iFile + filePostfix, 'r') as f:
        nGalFile = len(f[snap])
        DiskMass[iGal:iGal + nGalFile] = f[snap]['DiskMass']
        BulgeMass[iGal:iGal + nGalFile] = f[snap]['BulgeMass']
        StellarMass[iGal:iGal + nGalFile] = f[snap]['StellarMass']
        iGal += nGalFile

# Physical units #
hubble = 0.678
VelocityUnits = 1  # [Km/s]
LengthUnits = 1e3 / hubble  # [Kpc]
MassUnits = 1e10 / hubble  # [Msun]
SpinUnits = 1e3 / hubble  # [Km/s * Kpc]

# Disk dominated #
indexDD = np.where(DiskMass > 0.7 * StellarMass)

# Bulge dominated #
indexBD = np.where(BulgeMass > 0.7 * StellarMass)

# Data #
DD = float(len(indexDD[0])) / float(len(StellarMass))
BD = float(len(indexBD[0])) / float(len(StellarMass))
Stellar_Mass = StellarMass * MassUnits
# Generate initial figure #
plt.close()
plt.figure(1, figsize=(18, 10))

# Scatter plot parameters #
plt.title(r'$\mathrm{Stellar\; Mass\; versus\; Cold\; Gas\; to\; Stellar\; Disk\; Mass}$', fontsize=30)

plt.xlim(0, 3)
plt.ylim(0, 1)

plt.xticks(fontsize=20)
plt.yticks(fontsize=20)

plt.xlabel('$\mathrm{M_{\star}\; [M_{\odot}]}$', fontsize=30)
plt.ylabel('$\mathrm{M_{gas}\; /\; M_{\star}}$', fontsize=30)

plt.scatter(0, DD, c='b')
plt.scatter(0, BD, c='r')

plt.grid(True, which="both", c='k')

########################################################################################################################

# Read in parameters #
outputDir = '/Users/Bam/Astronomy Phd/L-Galaxies/outputs/output2/'
filePrefix = 'SA_output_'
filePostfix = '.h5'
snap = '45'
firstFile = 0
lastFile = 9

# First determine the size of the arrays that we need to hold the data #
nGal = 0
for iFile in range(firstFile, lastFile + 1):
    # The following line closes the file at the end of the loop
    with h5py.File(outputDir + filePrefix + '%i' % iFile + filePostfix, 'r') as f:
        nGal += len(f[snap])

# Declare numpy arrays to hold the data #
BulgeMass = np.empty(nGal)
DiskMass = np.empty(nGal)
StellarMass = np.empty(nGal)

# Read in the data #
iGal = 0
for iFile in range(firstFile, lastFile + 1):
    # The following line closes the file at the end of the loop
    with h5py.File(outputDir + filePrefix + '%i' % iFile + filePostfix, 'r') as f:
        nGalFile = len(f[snap])
        DiskMass[iGal:iGal + nGalFile] = f[snap]['DiskMass']
        BulgeMass[iGal:iGal + nGalFile] = f[snap]['BulgeMass']
        StellarMass[iGal:iGal + nGalFile] = f[snap]['StellarMass']
        iGal += nGalFile

# Physical units #
hubble = 0.678
VelocityUnits = 1  # [Km/s]
LengthUnits = 1e3 / hubble  # [Kpc]
MassUnits = 1e10 / hubble  # [Msun]
SpinUnits = 1e3 / hubble  # [Km/s * Kpc]

# Disk dominated #
indexDD = np.where(DiskMass > 0.7 * StellarMass)

# Bulge dominated #
indexBD = np.where(BulgeMass > 0.7 * StellarMass)

# Data #
DD = float(len(indexDD[0])) / float(len(StellarMass))
BD = float(len(indexBD[0])) / float(len(StellarMass))
Stellar_Mass = StellarMass * MassUnits

plt.scatter(0.5, DD, c='b')
plt.scatter(0.5, BD, c='r')
########################################################################################################################


# Read in parameters #
outputDir = '/Users/Bam/Astronomy Phd/L-Galaxies/outputs/output2/'
filePrefix = 'SA_output_'
filePostfix = '.h5'
snap = '38'
firstFile = 0
lastFile = 9

# First determine the size of the arrays that we need to hold the data #
nGal = 0
for iFile in range(firstFile, lastFile + 1):
    # The following line closes the file at the end of the loop
    with h5py.File(outputDir + filePrefix + '%i' % iFile + filePostfix, 'r') as f:
        nGal += len(f[snap])

# Declare numpy arrays to hold the data #
BulgeMass = np.empty(nGal)
DiskMass = np.empty(nGal)
StellarMass = np.empty(nGal)

# Read in the data #
iGal = 0
for iFile in range(firstFile, lastFile + 1):
    # The following line closes the file at the end of the loop
    with h5py.File(outputDir + filePrefix + '%i' % iFile + filePostfix, 'r') as f:
        nGalFile = len(f[snap])
        DiskMass[iGal:iGal + nGalFile] = f[snap]['DiskMass']
        BulgeMass[iGal:iGal + nGalFile] = f[snap]['BulgeMass']
        StellarMass[iGal:iGal + nGalFile] = f[snap]['StellarMass']
        iGal += nGalFile

# Physical units #
hubble = 0.678
VelocityUnits = 1  # [Km/s]
LengthUnits = 1e3 / hubble  # [Kpc]
MassUnits = 1e10 / hubble  # [Msun]
SpinUnits = 1e3 / hubble  # [Km/s * Kpc]

# Disk dominated #
indexDD = np.where(DiskMass > 0.7 * StellarMass)

# Bulge dominated #
indexBD = np.where(BulgeMass > 0.7 * StellarMass)

# Data #
DD = float(len(indexDD[0])) / float(len(StellarMass))
BD = float(len(indexBD[0])) / float(len(StellarMass))
Stellar_Mass = StellarMass * MassUnits

plt.scatter(1, DD, c='b')
plt.scatter(1, BD, c='r')

########################################################################################################################



# Read in parameters #
outputDir = '/Users/Bam/Astronomy Phd/L-Galaxies/outputs/output2/'
filePrefix = 'SA_output_'
filePostfix = '.h5'
snap = '30'
firstFile = 0
lastFile = 9

# First determine the size of the arrays that we need to hold the data #
nGal = 0
for iFile in range(firstFile, lastFile + 1):
    # The following line closes the file at the end of the loop
    with h5py.File(outputDir + filePrefix + '%i' % iFile + filePostfix, 'r') as f:
        nGal += len(f[snap])

# Declare numpy arrays to hold the data #
BulgeMass = np.empty(nGal)
DiskMass = np.empty(nGal)
StellarMass = np.empty(nGal)

# Read in the data #
iGal = 0
for iFile in range(firstFile, lastFile + 1):
    # The following line closes the file at the end of the loop
    with h5py.File(outputDir + filePrefix + '%i' % iFile + filePostfix, 'r') as f:
        nGalFile = len(f[snap])
        DiskMass[iGal:iGal + nGalFile] = f[snap]['DiskMass']
        BulgeMass[iGal:iGal + nGalFile] = f[snap]['BulgeMass']
        StellarMass[iGal:iGal + nGalFile] = f[snap]['StellarMass']
        iGal += nGalFile

# Physical units #
hubble = 0.678
VelocityUnits = 1  # [Km/s]
LengthUnits = 1e3 / hubble  # [Kpc]
MassUnits = 1e10 / hubble  # [Msun]
SpinUnits = 1e3 / hubble  # [Km/s * Kpc]

# Disk dominated #
indexDD = np.where(DiskMass > 0.7 * StellarMass)

# Bulge dominated #
indexBD = np.where(BulgeMass > 0.7 * StellarMass)

# Data #
DD = float(len(indexDD[0])) / float(len(StellarMass))
BD = float(len(indexBD[0])) / float(len(StellarMass))
Stellar_Mass = StellarMass * MassUnits

plt.scatter(2, DD, c='b')
plt.scatter(2, BD, c='r')

########################################################################################################################

plt.savefig('BulgeDiskFraction-' + date_string + '.png')
