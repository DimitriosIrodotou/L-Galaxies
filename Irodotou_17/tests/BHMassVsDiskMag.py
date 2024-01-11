# Imports #
import h5py
import numpy as np
import matplotlib.pyplot as plt
import time
date_string = time.strftime("%d\%m\%y\%H%M")

# Read in parameters #
outputDir = '/Users/Bam/Astronomy Phd/L-Galaxies/outputs/DI_Feedback/'

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
N = np.empty(nGal)
MMDBulgeMass = np.empty(nGal)
mMDBulgeMass = np.empty(nGal)
MDBulgeMass = np.empty(nGal)
IDBulgeMass = np.empty(nGal)
BulgeMass = np.empty(nGal)
BlackHoleMass = np.empty(nGal)
StellarMass = np.empty(nGal)
DiskMag = np.empty([nGal, 5])

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
        BlackHoleMass[iGal:iGal + nGalFile] = f[snap]['BlackHoleMass']
        StellarMass[iGal:iGal + nGalFile] = f[snap]['StellarMass']
        DiskMag[iGal:iGal + nGalFile] = f[snap]['Mag']
        N[iGal:iGal + nGalFile] = f[snap]['NMajorMergers']
        iGal += nGalFile

# Physical units #
hubble = 0.678
VelocityUnits = 1  # [Km/s]
LengthUnits = 1e3 / hubble  # [Kpc]
MassUnits = 1e10 / hubble  # [Msun]
SpinUnits = 1e3 / hubble  # [Km/s * Kpc]

dDiskMag = 0.3

# ID bulge dominated #
indexID = np.where((IDBulgeMass > 0.7 * BulgeMass) & (BlackHoleMass > 1e-5))

# MD bulge dominated #
MD = MMDBulgeMass + MDBulgeMass + mMDBulgeMass
indexMD = np.where((MD > 0.7 * BulgeMass) & (BlackHoleMass > 1e-5))

# Data #
Disk_Mag1 = zip(*DiskMag[indexID])[3]
Disk_Mag2 = zip(*DiskMag[indexMD])[3]

BH_Mass1 = BlackHoleMass[indexID] * MassUnits
BH_Mass2 = BlackHoleMass[indexMD] * MassUnits

# Generate initial figure #
plt.close()
plt.figure(1, figsize=(18, 10))

# Scatter plot parameters #
plt.title(r'$\mathrm{BH\; mass\; versus\; K-band\; absolute\; magnitude\; of\; the\; disk}$', fontsize=30)

plt.xlabel(r'$\mathrm{M_{K, disk}}$', fontsize=30)
plt.ylabel(r'$\mathrm{log(M_{\bullet}\; [M_{\odot}])}$', fontsize=30)

plt.yscale('log')

plt.xlim(-20, -24)
plt.ylim(1e5, 1e10)

plt.xticks(fontsize=20)
plt.yticks(fontsize=20)

plt.grid(True, which="both", c='k')

# Plot data #
plt.scatter(Disk_Mag1, BH_Mass1, c='b', s=10, label="$\mathrm{Pseudo\, bulges}$")
plt.scatter(Disk_Mag2, BH_Mass2, c='r', s=10, label="$\mathrm{Classical\, bulges}$")

# Observational data #
xp = [-21.65, -22.55, -22.85, -22.92, -23.01, -23.03, -23.15, -23.31, -23.52, -23.63, -23.68, -23.68, -23.77, -24.02,
      -24.12, -24.12, -24.12, -24.30, -24.33, -24.67, -24.74]
yp = [10 ** 6.905, 10 ** 5.457, 10 ** 6.109, 10 ** 6.167, 10 ** 6.206, 10 ** 6.948, 10 ** 6.324, 10 ** 5.543,
      10 ** 5.958, 10 ** 6.304, 10 ** 6.187, 10 ** 6.265, 10 ** 5.578, 10 ** 7.215, 10 ** 6.629, 10 ** 6.546,
      10 ** 6.546, 10 ** 7.080, 10 ** 6.797, 10 ** 6.245, 10 ** 6.304]
xc = [-20.93, -21.37, -21.55, -21.90, -21.99, -22.01, -22.01, -22.04, -22.15, -22.48, -22.55, -23.26, -23.31, -23.40,
      -23.47, -23.54, -23.72, -23.89]
yc = [10 ** 7.579, 10 ** 8.436, 10 ** 8.436, 10 ** 7.298, 10 ** 7.946, 10 ** 6.274, 10 ** 7.627, 10 ** 8.462,
      10 ** 6.455, 10 ** 7.748, 10 ** 8.304, 10 ** 7.252, 10 ** 7.207, 10 ** 6.962, 10 ** 8.174, 10 ** 7.117,
      10 ** 6.896, 10 ** 7.532]

# Plot observational data #
plt.scatter(xp, yp, c='b', marker='*', edgecolor='k', s=300, label="$\mathrm{Pseudo\, bulges}$")
plt.scatter(xc, yc, c='r', marker='*', edgecolor='k', s=300, label="$\mathrm{Classical\, bulges}$")
plt.legend(loc=1, fancybox='True', shadow='True', fontsize=20, markerscale=1)
plt.savefig('BHMassVsDiskMag-' + date_string + '.png')

########################################################################################################################

# Generate initial figure #
plt.close()
plt.figure(1, figsize=(18, 10))

# Median and 1-sigma plot parameters #
plt.title(r'$\mathrm{BH\; mass\; versus\; K-band\; absolute\; magnitude\; of\; the\; disk}$', fontsize=30)

plt.xlabel(r'$\mathrm{M_{K, disk}}$', fontsize=30)
plt.ylabel(r'$\mathrm{log(M_{\bullet}\; [M_{\odot}])}$', fontsize=30)

plt.yscale('log')

plt.xlim(-20, -24)
plt.ylim(1e5, 1e10)

plt.xticks(fontsize=20)
plt.yticks(fontsize=20)

plt.grid(True, which="both", c='k')

# Plot observational data #
plt.scatter(xp, yp, color='b', marker='*', edgecolor='k', s=300, label="$\mathrm{Pseudo\, bulges}$")
plt.scatter(xc, yc, color='r', marker='*', edgecolor='k', s=300, label="$\mathrm{Classical\, bulges}$")

# Calculate median and 1-sigma for pseudo bulges #
AbsDiskMag = np.absolute(Disk_Mag1)
AbsDiskMagMax = max(np.absolute(Disk_Mag1))
AbsDiskMagMin = min(np.absolute(Disk_Mag1))
nbin = int((AbsDiskMagMax - AbsDiskMagMin) / dDiskMag)
mag = np.empty(nbin)
median = np.empty(nbin)
slow = np.empty(nbin)
shigh = np.empty(nbin)
MagLow = AbsDiskMagMin
for i in range(nbin):
    index = np.where((AbsDiskMag >= MagLow) & (AbsDiskMag < MagLow + dDiskMag))[0]
    mag[i] = np.mean(np.absolute(Disk_Mag1)[index])
    if len(index) > 0:
        median[i] = np.median(BH_Mass1[index])
        slow[i] = np.percentile(BH_Mass1[index], 15.87)
        shigh[i] = np.percentile(BH_Mass1[index], 84.13)
    MagLow += dDiskMag

# Plot median and 1-sigma lines for pseudo bulges #
plt.plot(-mag, median, 'b-', lw=4, label="$\mathrm{Pseudo\, median}$")
plt.fill_between(-mag, shigh, slow, color='blue', alpha='0.5')

# Calculate median and 1-sigma for classical bulges #
AbsDiskMag = np.absolute(Disk_Mag2)
AbsDiskMagMax = max(np.absolute(Disk_Mag2))
AbsDiskMagMin = min(np.absolute(Disk_Mag2))
nbin = int((AbsDiskMagMax - AbsDiskMagMin) / dDiskMag)
mag = np.empty(nbin)
median = np.empty(nbin)
slow = np.empty(nbin)
shigh = np.empty(nbin)
MagLow = AbsDiskMagMin
for i in range(nbin):
    index = np.where((AbsDiskMag >= MagLow) & (AbsDiskMag < MagLow + dDiskMag))[0]
    mag[i] = np.mean(np.absolute(Disk_Mag2)[index])
    if len(index) > 0:
        median[i] = np.median(BH_Mass2[index])
        slow[i] = np.percentile(BH_Mass2[index], 15.87)
        shigh[i] = np.percentile(BH_Mass2[index], 84.13)
    MagLow += dDiskMag

# Plot median and 1-sigma line for classical bulges #
plt.plot(-mag, median, 'r-', lw=4, label="$\mathrm{Classical\, median}$")
plt.fill_between(-mag, shigh, slow, color='red', alpha='0.5')
plt.legend(loc=1, fancybox='True', shadow='True', fontsize=20, markerscale=1)
plt.savefig('BHMassVsDiskMag1-' + date_string + '.png')
