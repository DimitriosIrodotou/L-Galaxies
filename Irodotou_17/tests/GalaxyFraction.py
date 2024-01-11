# Imports
import h5py
import numpy as np
import matplotlib.pyplot as plt
import time
date_string = time.strftime("%d\%m\%y\%H%M")

# Read in parameters #
outputDir = '/Users/Bam/Astronomy Phd/L-Galaxies/outputs/'
obsDir = '/Users/Bam/PycharmProjects2/Fraction/'
filePrefix = 'SA_output_'
filePostfix = '.h5'
snap = '58'
redshift = 0
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
Type = np.empty(nGal)
BulgeMass = np.empty(nGal)
DiskMass = np.empty(nGal)
StellarMass = np.empty(nGal)

# Read in the data #
iGal = 0
for iFile in range(firstFile, lastFile + 1):
    # The following line closes the file at the end of the loop #
    with h5py.File(outputDir + filePrefix + '%i' % iFile + filePostfix, 'r') as f:
        nGalFile = len(f[snap])
        Type[iGal:iGal + nGalFile] = f[snap]['Type']
        BulgeMass[iGal:iGal + nGalFile] = f[snap]['BulgeMass']
        DiskMass[iGal:iGal + nGalFile] = f[snap]['DiskMass']
        StellarMass[iGal:iGal + nGalFile] = f[snap]['StellarMass']
        iGal += nGalFile
assert np.all(abs(StellarMass - BulgeMass - DiskMass) < 1e-5 * StellarMass)

# Simulation parameters (read from file!) #
hubble = 0.673
boxside = 480.28  # Units Mpc/h

# Divisions between bulge classes #
logRatio1 = -0.154902
logRatio2 = -2

# Bins for histogram and plotting #
binwidth = 0.25
xrange = np.array([7.8, 11.6])
bins = np.arange(xrange[0], xrange[1] + 0.001, binwidth)

# Put into observer units and add scatter to stellar mass estimate #
offset = 10 + np.log10(hubble)
logBulge = np.log10(BulgeMass) + offset
logDisk = np.log10(DiskMass) + offset
logStellarMass = np.log10(StellarMass) + offset
logStellarMassObs = logStellarMass + np.random.randn(nGal) * 0.08 * (1 + redshift)

# Put galaxies into bins #
indBin = np.digitize(logStellarMassObs, bins)
nBin = len(bins) - 1
x = np.empty(nBin)
yBulge = np.empty(nBin)
yDisk = np.empty(nBin)

yIrr = np.empty(nBin)

# Loop over bins, counting fractions in each class #
for iBin in range(nBin):
    x[iBin] = 0.5 * (bins[iBin] + bins[iBin + 1])
    indThisBin = np.where(indBin == iBin + 1)[0]
    allBin = len(indThisBin)

    # Bulges
    yBulge[iBin] = len(np.where((logBulge[indThisBin] - logStellarMass[indThisBin]) > logRatio1)[0]) / float(allBin)
    # Disks
    yIrr[iBin] = len(np.where((logBulge[indThisBin] - logStellarMass[indThisBin]) < logRatio2)[0]) / float(allBin)
    # Intermediates
    yDisk[iBin] = 1. - yBulge[iBin] - yIrr[iBin]

# Generate initial figure #
plt.close()
plt.figure(1, figsize=(18, 10))

# Plot parameters #
plt.title(r'$\mathrm{Fraction\, of\, different\, morphological\, types\, as\, a\, function\, of\, stellar\, mass}$',
          fontsize=30)

plt.xlabel(r'$\mathrm{log(M_{\star} [M_\odot])}$', fontsize=30)
plt.ylabel(r'$\mathrm{Fraction}$', fontsize=30)

plt.xlim(7, 12)
plt.ylim(0, 1.2)

plt.xticks(fontsize=20)
plt.yticks(fontsize=20)

plt.grid(True, which="both", c='k')

# Plot data #
plt.plot(x, yBulge, c='r', label='$\mathrm{Bulge}$', lw=4)
plt.plot(x, yDisk, c='b', label='$\mathrm{Disk}$', lw=4)
plt.plot(x, yIrr, c='g', label='$\mathrm{Irregular}$', lw=4)

# Observational data #
obsBulgeFile = 'conselice2006_bulge_fract.txt'
obsDiskFile = 'conselice2006_disk_fract.txt'
obsIrrFile = 'conselice2006_irr_fract.txt'
obsHubble = 0.70

# Plot observations #
plt.gca().set_prop_cycle(None)

obsBulge = np.loadtxt(obsDir + obsBulgeFile)
obsMass = obsBulge[:, 0] + 2 * np.log10(obsHubble)
plt.errorbar(obsMass, obsBulge[:, 1], yerr=obsBulge[:, 2], marker='o', linestyle='None', c='r',
             label="$\mathrm{Conselice\, 2006}$")

obsDisk = np.loadtxt(obsDir + obsDiskFile)
obsMass = obsDisk[:, 0] + 2 * np.log10(obsHubble)
plt.errorbar(obsMass, obsDisk[:, 1], yerr=obsDisk[:, 2], marker='o', linestyle='None', c='b')

obsIrr = np.loadtxt(obsDir + obsIrrFile)
obsMass = obsIrr[:, 0] + 2 * np.log10(obsHubble)
plt.errorbar(obsMass, obsIrr[:, 1], yerr=obsIrr[:, 2], marker='o', linestyle='None', c='g')

plt.legend(loc=2, fancybox='True', shadow='True', fontsize=20, markerscale=1)
plt.savefig('GalaxyFraction-' + date_string + '.png')
