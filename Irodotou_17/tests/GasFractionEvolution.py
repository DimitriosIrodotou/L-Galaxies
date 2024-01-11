# Imports #
import h5py
import numpy as np
import matplotlib.pyplot as plt
import time

date_string = time.strftime("%d\%m\%y\%H%M")

# Read in parameters #
outputDir = '/Users/Bam/Astronomy Phd/L-Galaxies/outputs/output/'
obsDir = '/Users/Bam/Astronomy PhD/LGalaxies_HWT15_PublicRelease/MCMC/ObsConstraints/'
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
ColdGas = np.empty(nGal)
DiskMass = np.empty(nGal)
StellarMass = np.empty(nGal)

# Read in the data #
iGal = 0
for iFile in range(firstFile, lastFile + 1):
    # The following line closes the file at the end of the loop
    with h5py.File(outputDir + filePrefix + '%i' % iFile + filePostfix, 'r') as f:
        nGalFile = len(f[snap])
        DiskMass[iGal:iGal + nGalFile] = f[snap]['DiskMass']
        ColdGas[iGal:iGal + nGalFile] = f[snap]['ColdGas']
        StellarMass[iGal:iGal + nGalFile] = f[snap]['StellarMass']
        iGal += nGalFile

# Physical units #
hubble = 0.678
VelocityUnits = 1  # [Km/s]
LengthUnits = 1e3 / hubble  # [Kpc]
MassUnits = 1e10 / hubble  # [Msun]
SpinUnits = 1e3 / hubble  # [Km/s * Kpc]

dlog10StellarMass = 0.2

# Disk dominated #
indexDD = np.where((DiskMass > 0.6 * StellarMass) & (ColdGas > 0.0))

# Data #
Cold_Gas_Mass = ColdGas[indexDD] * MassUnits
Stellar_Mass = StellarMass[indexDD] * MassUnits
Ratio = np.divide(Cold_Gas_Mass, Stellar_Mass)

# Generate initial figure #
plt.close()
plt.figure(1, figsize=(18, 10))

# Scatter plot parameters #
plt.title(r'$\mathrm{Stellar\; Mass\; versus\; Cold\; Gas\; to\; Stellar\; Disk\; Mass}$', fontsize=30)

plt.xscale('log')
plt.yscale('log')

plt.xlim(1e9, 1e12)
plt.ylim(1e-2, 1e1)

plt.xticks(fontsize=20)
plt.yticks(fontsize=20)

plt.xlabel('$\mathrm{M_{\star}\; [M_{\odot}]}$', fontsize=30)
plt.ylabel('$\mathrm{M_{gas}\; /\; M_{\star}}$', fontsize=30)

plt.grid(True, which="both", c='k')

# Calculate median and 1-sigma #
log10StellarMass = np.log10(Stellar_Mass)
log10StellarMassMax = np.log10(max(Stellar_Mass))
log10StellarMassMin = np.log10(min(Stellar_Mass))
nbin = int((log10StellarMassMax - log10StellarMassMin) / dlog10StellarMass)
mass = np.empty(nbin)
median = np.empty(nbin)
log10StellarMassLow = log10StellarMassMin
for i in range(nbin):
    index = \
        np.where(
            (log10StellarMass >= log10StellarMassLow) & (log10StellarMass < log10StellarMassLow + dlog10StellarMass))[
            0]
    mass[i] = np.mean(Stellar_Mass[index])
    if len(index) > 0:
        median[i] = np.median(Ratio[index])
    log10StellarMassLow += dlog10StellarMass

# Plot median and 1-sigma lines #
plt.plot(mass, median, 'r-', label="$\mathrm{z=0.00}$", lw=2)
plt.legend(loc=1, fancybox='True', shadow='True', fontsize="20")

#################################################################################################################################################################


# Read in parameters #
# outputDir = '/Users/Bam/Astronomy Phd/L-Galaxies/outputs/'
obsDir = '/Users/Bam/Astronomy PhD/LGalaxies_HWT15_PublicRelease/MCMC/ObsConstraints/'
filePrefix = 'SA_output_'
filePostfix = '.h5'
snap = '54'
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
ColdGas = np.empty(nGal)
DiskMass = np.empty(nGal)
StellarMass = np.empty(nGal)

# Read in the data #
iGal = 0
for iFile in range(firstFile, lastFile + 1):
    # The following line closes the file at the end of the loop
    with h5py.File(outputDir + filePrefix + '%i' % iFile + filePostfix, 'r') as f:
        nGalFile = len(f[snap])
        DiskMass[iGal:iGal + nGalFile] = f[snap]['DiskMass']
        ColdGas[iGal:iGal + nGalFile] = f[snap]['ColdGas']
        StellarMass[iGal:iGal + nGalFile] = f[snap]['StellarMass']
        iGal += nGalFile

# Physical units #
hubble = 0.678
VelocityUnits = 1  # [Km/s]
LengthUnits = 1e3 / hubble  # [Kpc]
MassUnits = 1e10 / hubble  # [Msun]
SpinUnits = 1e3 / hubble  # [Km/s * Kpc]

dlog10StellarMass = 0.2

# Disk dominated #
indexDD = np.where((DiskMass > 0.6 * StellarMass) & (ColdGas > 0.0))

# Data #
Cold_Gas_Mass = ColdGas[indexDD] * MassUnits
Stellar_Mass = StellarMass[indexDD] * MassUnits
Ratio = np.divide(Cold_Gas_Mass, Stellar_Mass)

# Calculate median and 1-sigma #
log10StellarMass = np.log10(Stellar_Mass)
log10StellarMassMax = np.log10(max(Stellar_Mass))
log10StellarMassMin = np.log10(min(Stellar_Mass))
nbin = int((log10StellarMassMax - log10StellarMassMin) / dlog10StellarMass)
mass = np.empty(nbin)
median = np.empty(nbin)
log10StellarMassLow = log10StellarMassMin
for i in range(nbin):
    index = \
        np.where(
            (log10StellarMass >= log10StellarMassLow) & (log10StellarMass < log10StellarMassLow + dlog10StellarMass))[
            0]
    mass[i] = np.mean(Stellar_Mass[index])
    if len(index) > 0:
        median[i] = np.median(Ratio[index])
    log10StellarMassLow += dlog10StellarMass

# Plot median and 1-sigma lines #
plt.plot(mass, median, 'k-', label="$\mathrm{z=0.12}$", lw=2)
plt.legend(loc=1, fancybox='True', shadow='True', fontsize="20")

#################################################################################################################################################################


# Read in parameters #
# outputDir = '/Users/Bam/Astronomy Phd/L-Galaxies/outputs/'
obsDir = '/Users/Bam/Astronomy PhD/LGalaxies_HWT15_PublicRelease/MCMC/ObsConstraints/'
filePrefix = 'SA_output_'
filePostfix = '.h5'
snap = '50'
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
ColdGas = np.empty(nGal)
DiskMass = np.empty(nGal)
StellarMass = np.empty(nGal)

# Read in the data #
iGal = 0
for iFile in range(firstFile, lastFile + 1):
    # The following line closes the file at the end of the loop
    with h5py.File(outputDir + filePrefix + '%i' % iFile + filePostfix, 'r') as f:
        nGalFile = len(f[snap])
        DiskMass[iGal:iGal + nGalFile] = f[snap]['DiskMass']
        ColdGas[iGal:iGal + nGalFile] = f[snap]['ColdGas']
        StellarMass[iGal:iGal + nGalFile] = f[snap]['StellarMass']
        iGal += nGalFile

# Physical units #
hubble = 0.678
VelocityUnits = 1  # [Km/s]
LengthUnits = 1e3 / hubble  # [Kpc]
MassUnits = 1e10 / hubble  # [Msun]
SpinUnits = 1e3 / hubble  # [Km/s * Kpc]

dlog10StellarMass = 0.2

# Disk dominated #
indexDD = np.where((DiskMass > 0.6 * StellarMass) & (ColdGas > 0.0))

# Data #
Cold_Gas_Mass = ColdGas[indexDD] * MassUnits
Stellar_Mass = StellarMass[indexDD] * MassUnits
Ratio = np.divide(Cold_Gas_Mass, Stellar_Mass)

# Generate initial figure #

# Calculate median and 1-sigma #
log10StellarMass = np.log10(Stellar_Mass)
log10StellarMassMax = np.log10(max(Stellar_Mass))
log10StellarMassMin = np.log10(min(Stellar_Mass))
nbin = int((log10StellarMassMax - log10StellarMassMin) / dlog10StellarMass)
mass = np.empty(nbin)
median = np.empty(nbin)
log10StellarMassLow = log10StellarMassMin
for i in range(nbin):
    index = \
        np.where(
            (log10StellarMass >= log10StellarMassLow) & (log10StellarMass < log10StellarMassLow + dlog10StellarMass))[
            0]
    mass[i] = np.mean(Stellar_Mass[index])
    if len(index) > 0:
        median[i] = np.median(Ratio[index])
    log10StellarMassLow += dlog10StellarMass

# Plot median and 1-sigma lines #
plt.plot(mass, median, 'g-', label="$\mathrm{z=0.25}$", lw=2)
plt.legend(loc=1, fancybox='True', shadow='True', fontsize="20")

#################################################################################################################################################################



# Read in parameters #
# outputDir = '/Users/Bam/Astronomy Phd/L-Galaxies/outputs/'
obsDir = '/Users/Bam/Astronomy PhD/LGalaxies_HWT15_PublicRelease/MCMC/ObsConstraints/'
filePrefix = 'SA_output_'
filePostfix = '.h5'
snap = '45'
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
ColdGas = np.empty(nGal)
DiskMass = np.empty(nGal)
StellarMass = np.empty(nGal)

# Read in the data #
iGal = 0
for iFile in range(firstFile, lastFile + 1):
    # The following line closes the file at the end of the loop
    with h5py.File(outputDir + filePrefix + '%i' % iFile + filePostfix, 'r') as f:
        nGalFile = len(f[snap])
        DiskMass[iGal:iGal + nGalFile] = f[snap]['DiskMass']
        ColdGas[iGal:iGal + nGalFile] = f[snap]['ColdGas']
        StellarMass[iGal:iGal + nGalFile] = f[snap]['StellarMass']
        iGal += nGalFile

# Physical units #
hubble = 0.678
VelocityUnits = 1  # [Km/s]
LengthUnits = 1e3 / hubble  # [Kpc]
MassUnits = 1e10 / hubble  # [Msun]
SpinUnits = 1e3 / hubble  # [Km/s * Kpc]

dlog10StellarMass = 0.2

# Disk dominated #
indexDD = np.where((DiskMass > 0.6 * StellarMass) & (ColdGas > 0.0))

# Data #
Cold_Gas_Mass = ColdGas[indexDD] * MassUnits
Stellar_Mass = StellarMass[indexDD] * MassUnits
Ratio = np.divide(Cold_Gas_Mass, Stellar_Mass)

# Generate initial figure #

# Calculate median and 1-sigma #
log10StellarMass = np.log10(Stellar_Mass)
log10StellarMassMax = np.log10(max(Stellar_Mass))
log10StellarMassMin = np.log10(min(Stellar_Mass))
nbin = int((log10StellarMassMax - log10StellarMassMin) / dlog10StellarMass)
mass = np.empty(nbin)
median = np.empty(nbin)
log10StellarMassLow = log10StellarMassMin
for i in range(nbin):
    index = \
        np.where(
            (log10StellarMass >= log10StellarMassLow) & (log10StellarMass < log10StellarMassLow + dlog10StellarMass))[
            0]
    mass[i] = np.mean(Stellar_Mass[index])
    if len(index) > 0:
        median[i] = np.median(Ratio[index])
    log10StellarMassLow += dlog10StellarMass

# Plot median and 1-sigma lines #
plt.plot(mass, median, 'b-', label="$\mathrm{z=0.50}$", lw=2)
plt.legend(loc=1, fancybox='True', shadow='True', fontsize="20")

#################################################################################################################################################################



# Read in parameters #
# outputDir = '/Users/Bam/Astronomy Phd/L-Galaxies/outputs/'
obsDir = '/Users/Bam/Astronomy PhD/LGalaxies_HWT15_PublicRelease/MCMC/ObsConstraints/'
filePrefix = 'SA_output_'
filePostfix = '.h5'
snap = '38'
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
ColdGas = np.empty(nGal)
DiskMass = np.empty(nGal)
StellarMass = np.empty(nGal)

# Read in the data #
iGal = 0
for iFile in range(firstFile, lastFile + 1):
    # The following line closes the file at the end of the loop
    with h5py.File(outputDir + filePrefix + '%i' % iFile + filePostfix, 'r') as f:
        nGalFile = len(f[snap])
        DiskMass[iGal:iGal + nGalFile] = f[snap]['DiskMass']
        ColdGas[iGal:iGal + nGalFile] = f[snap]['ColdGas']
        StellarMass[iGal:iGal + nGalFile] = f[snap]['StellarMass']
        iGal += nGalFile

# Physical units #
hubble = 0.678
VelocityUnits = 1  # [Km/s]
LengthUnits = 1e3 / hubble  # [Kpc]
MassUnits = 1e10 / hubble  # [Msun]
SpinUnits = 1e3 / hubble  # [Km/s * Kpc]

dlog10StellarMass = 0.2

# Disk dominated #
indexDD = np.where((DiskMass > 0.6 * StellarMass) & (ColdGas > 0.0))

# Data #
Cold_Gas_Mass = ColdGas[indexDD] * MassUnits
Stellar_Mass = StellarMass[indexDD] * MassUnits
Ratio = np.divide(Cold_Gas_Mass, Stellar_Mass)


# Calculate median and 1-sigma #
log10StellarMass = np.log10(Stellar_Mass)
log10StellarMassMax = np.log10(max(Stellar_Mass))
log10StellarMassMin = np.log10(min(Stellar_Mass))
nbin = int((log10StellarMassMax - log10StellarMassMin) / dlog10StellarMass)
mass = np.empty(nbin)
median = np.empty(nbin)
log10StellarMassLow = log10StellarMassMin
for i in range(nbin):
    index = \
        np.where(
            (log10StellarMass >= log10StellarMassLow) & (log10StellarMass < log10StellarMassLow + dlog10StellarMass))[
            0]
    mass[i] = np.mean(Stellar_Mass[index])
    if len(index) > 0:
        median[i] = np.median(Ratio[index])
    log10StellarMassLow += dlog10StellarMass

# Plot median and 1-sigma lines #
plt.plot(mass, median, 'r--', label="$\mathrm{z=1.00}$", lw=2)
plt.legend(loc=1, fancybox='True', shadow='True', fontsize="20")

#################################################################################################################################################################



# Read in parameters #
# outputDir = '/Users/Bam/Astronomy Phd/L-Galaxies/outputs/'
obsDir = '/Users/Bam/Astronomy PhD/LGalaxies_HWT15_PublicRelease/MCMC/ObsConstraints/'
filePrefix = 'SA_output_'
filePostfix = '.h5'
snap = '30'
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
ColdGas = np.empty(nGal)
DiskMass = np.empty(nGal)
StellarMass = np.empty(nGal)

# Read in the data #
iGal = 0
for iFile in range(firstFile, lastFile + 1):
    # The following line closes the file at the end of the loop
    with h5py.File(outputDir + filePrefix + '%i' % iFile + filePostfix, 'r') as f:
        nGalFile = len(f[snap])
        DiskMass[iGal:iGal + nGalFile] = f[snap]['DiskMass']
        ColdGas[iGal:iGal + nGalFile] = f[snap]['ColdGas']
        StellarMass[iGal:iGal + nGalFile] = f[snap]['StellarMass']
        iGal += nGalFile

# Physical units #
hubble = 0.678
VelocityUnits = 1  # [Km/s]
LengthUnits = 1e3 / hubble  # [Kpc]
MassUnits = 1e10 / hubble  # [Msun]
SpinUnits = 1e3 / hubble  # [Km/s * Kpc]

dlog10StellarMass = 0.2

# Disk dominated #
indexDD = np.where((DiskMass > 0.6 * StellarMass) & (ColdGas > 0.0))

# Data #
Cold_Gas_Mass = ColdGas[indexDD] * MassUnits
Stellar_Mass = StellarMass[indexDD] * MassUnits
Ratio = np.divide(Cold_Gas_Mass, Stellar_Mass)


# Calculate median and 1-sigma #
log10StellarMass = np.log10(Stellar_Mass)
log10StellarMassMax = np.log10(max(Stellar_Mass))
log10StellarMassMin = np.log10(min(Stellar_Mass))
nbin = int((log10StellarMassMax - log10StellarMassMin) / dlog10StellarMass)
mass = np.empty(nbin)
median = np.empty(nbin)
log10StellarMassLow = log10StellarMassMin
for i in range(nbin):
    index = \
        np.where(
            (log10StellarMass >= log10StellarMassLow) & (log10StellarMass < log10StellarMassLow + dlog10StellarMass))[
            0]
    mass[i] = np.mean(Stellar_Mass[index])
    if len(index) > 0:
        median[i] = np.median(Ratio[index])
    log10StellarMassLow += dlog10StellarMass

# Plot median and 1-sigma lines #
plt.plot(mass, median, 'k.-', label="$\mathrm{z=2.00}$", lw=2)
plt.legend(loc=1, fancybox='True', shadow='True', fontsize="20")
plt.savefig('MassRatioVsStellarMass-' + date_string + '.png')

#################################################################################################################################################################