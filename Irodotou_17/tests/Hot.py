# Imports #
import h5py
import numpy as np
import matplotlib.pyplot as plt
import time

#date_string = time.strftime("%d\%m\%y\%H%M")

# Read in parameters #
# outputDir = '/Users/Bam/Astronomy PhD/L-Galaxies/outputs/Peter/'
# snap = '58'
# firstFile = 0
# lastFile = 9

# First determine the size of the arrays that we need to hold the data #
nGal = 0
for iFile in range(firstFile, lastFile + 1):
    # The following line closes the file at the end of the loop
    with h5py.File(outputDir + filePrefix + '%i' % iFile + filePostfix, 'r') as f:
        nGal += len(f[snap])

# Declare numpy arrays to hold the data #
Hot = np.empty(nGal)
StellarMass = np.empty(nGal)

# Read in the data #
iGal = 0
for iFile in range(firstFile, lastFile + 1):
    # The following line closes the file at the end of the loop
    with h5py.File(outputDir + filePrefix + '%i' % iFile + filePostfix, 'r') as f:
        nGalFile = len(f[snap])
        StellarMass[iGal:iGal + nGalFile] = f[snap]['StellarMass']
        Hot[iGal:iGal + nGalFile] = f[snap]['HotGas']
        iGal += nGalFile

# Physical units #
hubble = 0.678
VelocityUnits = 1  # [Km/s]
LengthUnits = 1e3 / hubble  # [Kpc]
MassUnits = 1e10 / hubble  # [Msun]
SpinUnits = 1e3 / hubble  # [Km/s * Kpc]

dlog10DiskMass = 0.1


# Data #
Stellar_Mass = StellarMass * MassUnits
Hot = Hot * MassUnits
# Generate initial figure #
plt.close()
fig = plt.figure(1, figsize=(18, 10))

# Scatter plot parameters #
# plt.title(r'$\mathrm{Stellar\; Mass\; versus\; Specific\; angular \;momentum}$', fontsize=30)

plt.xlabel(r'$\mathrm{M_{\star}\; [M_{\odot}]}$', fontsize=30)
plt.ylabel(r'$\mathrm{M_{hot\, gas}\; [M_{\odot}]}$', fontsize=30)

plt.xscale('log')
plt.yscale('log')

plt.xlim(1e8, 1e12)
plt.ylim(1e6, 1e14)

plt.xticks(fontsize=20)
plt.yticks(fontsize=20)

plt.grid(True, which="both", c='k')

# Calculate median and 1-sigma #
log10DiskMass = np.log10(Stellar_Mass)
log10DiskMassMax = np.log10(max(Stellar_Mass))
log10DiskMassMin = np.log10(min(Stellar_Mass))
nbin = int((log10DiskMassMax - log10DiskMassMin) / dlog10DiskMass)
mass = np.empty(nbin)
median = np.empty(nbin)
slow = np.empty(nbin)
shigh = np.empty(nbin)
log10MassLow = log10DiskMassMin
for i in range(nbin):
    index = np.where((log10DiskMass >= log10MassLow) & (log10DiskMass < log10MassLow + dlog10DiskMass))[0]
    mass[i] = np.mean(Stellar_Mass[index])
    if len(index) > 0:
        median[i] = np.median(Hot[index])
        slow[i] = np.percentile(Hot[index], 15.87)
        shigh[i] = np.percentile(Hot[index], 84.13)
    log10MassLow += dlog10DiskMass

# Plot median and 1-sigma lines #
plt.plot(mass, median, 'k-', lw=4, label="$\mathrm{Median Original}$")
# plt.fill_between(mass, shigh, slow, color='black', alpha='0.5')

# Read in parameters #
outputDir = '/Users/Bam/Astronomy PhD/L-Galaxies/outputs/ALL_ON/'
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
Hot = np.empty(nGal)
StellarMass = np.empty(nGal)

# Read in the data #
iGal = 0
for iFile in range(firstFile, lastFile + 1):
    # The following line closes the file at the end of the loop
    with h5py.File(outputDir + filePrefix + '%i' % iFile + filePostfix, 'r') as f:
        nGalFile = len(f[snap])
        StellarMass[iGal:iGal + nGalFile] = f[snap]['StellarMass']
        Hot[iGal:iGal + nGalFile] = f[snap]['HotGas']
        iGal += nGalFile

# Physical units #
hubble = 0.678
VelocityUnits = 1  # [Km/s]
LengthUnits = 1e3 / hubble  # [Kpc]
MassUnits = 1e10 / hubble  # [Msun]
SpinUnits = 1e3 / hubble  # [Km/s * Kpc]

dlog10DiskMass = 0.1


# Data #
Stellar_Mass = StellarMass * MassUnits
Hot = Hot * MassUnits
# Generate initial figure #
# plt.close()
# fig = plt.figure(1, figsize=(18, 10))

# Scatter plot parameters #
# plt.title(r'$\mathrm{Stellar\; Mass\; versus\; Specific\; angular \;momentum}$', fontsize=30)

# plt.xlabel(r'$\mathrm{M_{\star}\; [M_{\odot}]}$', fontsize=30)
# plt.ylabel(r'$\mathrm{M_{hot\, gas}\; [M_{\odot}]}$', fontsize=30)
#
# plt.xscale('log')
# plt.yscale('log')
#
# plt.xlim(1e8, 1e12)
# plt.ylim(1e6, 1e14)
#
# plt.xticks(fontsize=20)
# plt.yticks(fontsize=20)
#
# plt.grid(True, which="both", c='k')

# Calculate median and 1-sigma #
log10DiskMass = np.log10(Stellar_Mass)
log10DiskMassMax = np.log10(max(Stellar_Mass))
log10DiskMassMin = np.log10(min(Stellar_Mass))
nbin = int((log10DiskMassMax - log10DiskMassMin) / dlog10DiskMass)
mass = np.empty(nbin)
median = np.empty(nbin)
slow = np.empty(nbin)
shigh = np.empty(nbin)
log10MassLow = log10DiskMassMin
for i in range(nbin):
    index = np.where((log10DiskMass >= log10MassLow) & (log10DiskMass < log10MassLow + dlog10DiskMass))[0]
    mass[i] = np.mean(Stellar_Mass[index])
    if len(index) > 0:
        median[i] = np.median(Hot[index])
        slow[i] = np.percentile(Hot[index], 15.87)
        shigh[i] = np.percentile(Hot[index], 84.13)
    log10MassLow += dlog10DiskMass

# Plot median and 1-sigma lines #
plt.plot(mass, median, 'r-', lw=4, label="$\mathrm{Median}$")
# plt.fill_between(mass, shigh, slow, color='black', alpha='0.5')

leg = plt.legend(loc=4, fancybox='True', shadow='True', fontsize=20, markerscale=1)
plt.savefig('HotGasVsStellarMass-' + date_string + '.png')
