# Imports #
import h5py
import numpy as np
import matplotlib.pyplot as plt
import time

# date_string = time.strftime("%d\%m\%y\%H%M")

# Read in parameters #
# outputDir = '/Users/Bam/output/'
# filePrefix = 'SA_output_'
# filePostfix = '.h5'
snap = '30'  # z = 2.07
# firstFile = 0
# lastFile = 19

# First determine the size of the arrays that we need to hold the data #
nGal = 0
for iFile in range(firstFile, lastFile + 1):
    # The following line closes the file at the end of the loop
    with h5py.File(outputDir + filePrefix + '%i' % iFile + filePostfix, 'r') as f:
        nGal += len(f[snap])

# Declare numpy arrays to hold the data #
SHMR = np.empty(nGal)
StellarMass = np.empty(nGal)
Sfr = np.empty(nGal)

# Read in the data #
iGal = 0
for iFile in range(firstFile, lastFile + 1):
    # The following line closes the file at the end of the loop
    with h5py.File(outputDir + filePrefix + '%i' % iFile + filePostfix, 'r') as f:
        nGalFile = len(f[snap])
        SHMR[iGal:iGal + nGalFile] = f[snap]['StellarHalfMassRadius']
        StellarMass[iGal:iGal + nGalFile] = f[snap]['StellarMass']
        Sfr[iGal:iGal + nGalFile] = f[snap]['Sfr']
        iGal += nGalFile

# Physical units #
hubble = 0.678
VelocityUnits = 1  # [Km/s]
LengthUnits = 1e3 / hubble  # [Kpc]
MassUnits = 1e10 / hubble  # [Msun]
SpinUnits = 1e3 / hubble  # [Km/s * Kpc]

dBulgeMass = 0.3

# Bulge dominated #
index = np.where(Sfr / StellarMass < 0.02)

# Data #
Stellar_Mass = StellarMass[index] * MassUnits
S_H_M_R = SHMR[index] * LengthUnits
x = Stellar_Mass
y = S_H_M_R

# Generate initial figure #
plt.close()
fig = plt.figure(1, figsize=(18, 10))

# Scatter plot parameters #
plt.xlabel(r'$\mathrm{M_{\star}\; [M_{\odot}]}$', fontsize=30)
plt.ylabel(r'$\mathrm{R_{50}\; [Kpc]}$', fontsize=30)

plt.xscale('log')
plt.yscale('log')

plt.xlim(4e10, 1e12)
plt.ylim(1e-2, 1e2)

plt.xticks(fontsize=20)
plt.yticks(fontsize=20)

plt.grid(True, which="both", c='k')

# Plot data #
plt.scatter(Stellar_Mass, S_H_M_R, c='k', s=40)

########################################################################################################################

snap = '29'  # z = 2.25

# First determine the size of the arrays that we need to hold the data #
nGal = 0
for iFile in range(firstFile, lastFile + 1):
    # The following line closes the file at the end of the loop
    with h5py.File(outputDir + filePrefix + '%i' % iFile + filePostfix, 'r') as f:
        nGal += len(f[snap])

# Declare numpy arrays to hold the data #
SHMR = np.empty(nGal)
StellarMass = np.empty(nGal)
Sfr = np.empty(nGal)

# Read in the data #
iGal = 0
for iFile in range(firstFile, lastFile + 1):
    # The following line closes the file at the end of the loop
    with h5py.File(outputDir + filePrefix + '%i' % iFile + filePostfix, 'r') as f:
        nGalFile = len(f[snap])
        SHMR[iGal:iGal + nGalFile] = f[snap]['StellarHalfMassRadius']
        StellarMass[iGal:iGal + nGalFile] = f[snap]['StellarMass']
        Sfr[iGal:iGal + nGalFile] = f[snap]['Sfr']
        iGal += nGalFile

# Bulge dominated #
index = np.where(Sfr / StellarMass < 0.02)

# Data #
Stellar_Mass = StellarMass[index] * MassUnits
S_H_M_R = SHMR[index] * LengthUnits
x = np.hstack((x, Stellar_Mass))
y = np.hstack((y, S_H_M_R))

plt.scatter(Stellar_Mass, S_H_M_R, c='k', s=40)

########################################################################################################################

snap = '28'  # z = 2.44

# First determine the size of the arrays that we need to hold the data #
nGal = 0
for iFile in range(firstFile, lastFile + 1):
    # The following line closes the file at the end of the loop
    with h5py.File(outputDir + filePrefix + '%i' % iFile + filePostfix, 'r') as f:
        nGal += len(f[snap])

# Declare numpy arrays to hold the data #
SHMR = np.empty(nGal)
StellarMass = np.empty(nGal)
Sfr = np.empty(nGal)

# Read in the data #
iGal = 0
for iFile in range(firstFile, lastFile + 1):
    # The following line closes the file at the end of the loop
    with h5py.File(outputDir + filePrefix + '%i' % iFile + filePostfix, 'r') as f:
        nGalFile = len(f[snap])
        SHMR[iGal:iGal + nGalFile] = f[snap]['StellarHalfMassRadius']
        StellarMass[iGal:iGal + nGalFile] = f[snap]['StellarMass']
        Sfr[iGal:iGal + nGalFile] = f[snap]['Sfr']
        iGal += nGalFile

# Bulge dominated #
index = np.where(Sfr / StellarMass < 0.02)

# Data #
Stellar_Mass = StellarMass[index] * MassUnits
S_H_M_R = SHMR[index] * LengthUnits
x = np.hstack((x, Stellar_Mass))
y = np.hstack((y, S_H_M_R))

plt.scatter(Stellar_Mass, S_H_M_R, c='k', s=40, label="$\mathrm{sSFR < 0.02\, [Gyr^{-1}]}$")

########################################################################################################################

# Observational data #
plt.title(r'$\mathrm{Stellar\; Mass\; versus\; Stellar\; Half-Mass\; Radius\; for\; ETGs\, (2.07<z<2.44)}$',
          fontsize=30)

xt = [10 ** 10.60493421, 10 ** 12.08026316]
yt = [1.068838041, 11.30723684]
x1 = [10 ** 10.6, 10 ** 12.1]
y1 = [0.586033201, 6.324568748]
x2 = [10 ** 10.607109, 10 ** 12.06546053]
y2 = [0.662965334, 4.499692358]
xl = [10 ** 10.6, 10 ** 12.1]
yl = [0.316285459, 3.413405802]

plt.plot(xt, yt, c='b', linestyle='-.', lw=4, label="$\mathrm{Newman+12\, 1-\sigma}$")

plt.plot(x1, y1, c='b', lw=4, label="$\mathrm{Newman+12 (fr.par.\, slope)}$")
plt.plot(x2, y2, c='b', lw=4, linestyle='--', label="$\mathrm{Newman+12 (fixed\, slope)}$")

plt.plot(xl, yl, c='b', lw=4, linestyle='-.')

# Calculate median and 1-sigma #
LogBulgeMass = np.log10(x)
LogBulgeMassMax = np.log10(max(x))
LogBulgeMassMin = np.log10(min(x))
nbin = int((LogBulgeMassMax - LogBulgeMassMin) / dBulgeMass)
mass = np.empty(nbin)
median = np.empty(nbin)
slow = np.empty(nbin)
shigh = np.empty(nbin)
logMassLow = LogBulgeMassMin
for i in range(nbin):
    index = np.where((LogBulgeMass >= logMassLow) & (LogBulgeMass < logMassLow + dBulgeMass))[0]
    mass[i] = np.mean(np.absolute(x)[index])
    if len(index) > 0:
        median[i] = np.median(y[index])
        slow[i] = np.percentile(y[index], 15.87)
        shigh[i] = np.percentile(y[index], 84.13)
    logMassLow += dBulgeMass

# Plot median and 1-sigma lines #
plt.plot(mass, median, 'r-', lw=4, label="$\mathrm{Median}$")
plt.fill_between(mass, shigh, slow, color='red', alpha='0.5')

plt.legend(loc=4, fancybox='True', shadow='True', fontsize=20, markerscale=1)
plt.savefig('SMVsSHMREvo4-' + date_string + '.png')
