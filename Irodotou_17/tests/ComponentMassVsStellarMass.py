# Imports #
import h5py
import numpy as np
import matplotlib.pyplot as plt
import time

#date_string = time.strftime("%d\%m\%y\%H%M")

# Read in parameters #
#outputDir = '/Users/Bam/Astronomy Phd/L-Galaxies/outputs/DI_Feedback/'
snap = '58'
#firstFile = 0
#lastFile = 9


# First determine the size of the arrays that we need to hold the data #
nGal = 0
for iFile in range(firstFile, lastFile + 1):
    # The following line closes the file at the end of the loop
    with h5py.File(outputDir + filePrefix + '%i' % iFile + filePostfix, 'r') as f:
        nGal += len(f[snap])

# Declare numpy arrays to hold the data #
MDBulgeMass = np.empty(nGal)
IDBulgeMass = np.empty(nGal)
BulgeMass = np.empty(nGal)
DiskMass = np.empty(nGal)
StellarMass = np.empty(nGal)

# Read in the data #
iGal = 0
for iFile in range(firstFile, lastFile + 1):
    # The following line closes the file at the end of the loop
    with h5py.File(outputDir + filePrefix + '%i' % iFile + filePostfix, 'r') as f:
        nGalFile = len(f[snap])
        IDBulgeMass[iGal:iGal + nGalFile] = f[snap]['InstabilityDrivenBulgeMass']
        MDBulgeMass[iGal:iGal + nGalFile] = f[snap]['MergerDrivenBulgeMass']
        BulgeMass[iGal:iGal + nGalFile] = f[snap]['BulgeMass']
        DiskMass[iGal:iGal + nGalFile] = f[snap]['DiskMass']
        StellarMass[iGal:iGal + nGalFile] = f[snap]['StellarMass']
        iGal += nGalFile

# Physical units #
hubble = 0.678
VelocityUnits = 1  # [Km/s]
LengthUnits = 1e3 / hubble  # [Kpc]
MassUnits = 1e10 / hubble  # [Msun]
SpinUnits = 1e3 / hubble  # [Km/s * Kpc]

dlog10BulgeMass = 0.3

# Non-zero id bulge
indexID = np.where(IDBulgeMass > 0.0)

# Non-zero md bulge
MD = MDBulgeMass
indexMD = np.where(MD > 0.0)

# Non-zero disk
indexD = np.where(DiskMass > 0.0)

# Data #
Disk_Mass = DiskMass[indexD] * MassUnits
Bulge_Mass2 = MDBulgeMass[indexMD] * MassUnits
Stellar_Mass = StellarMass[indexD] * MassUnits
Stellar_Mass1 = StellarMass[indexID] * MassUnits
Stellar_Mass2 = StellarMass[indexMD] * MassUnits
Bulge_Mass1 = IDBulgeMass[indexID] * MassUnits

# Generate initial figure #
plt.close()
plt.figure(1, figsize=(18, 10))

# Scatter plot parameters #
plt.title(r'$\mathrm{Component\; mass\; versus\; Stellar\; mass}$', fontsize=30)

plt.xlabel(r'$\mathrm{log(M_{\star}\; [M_{\odot}])}$', fontsize=30)
plt.ylabel(r'$\mathrm{log(M_{\star}\; [M_{\odot}])}$', fontsize=30)

plt.xscale('log')
plt.yscale('log')

plt.xlim(1e9, 1e12)
plt.ylim(1e6, 1e13)

plt.xticks(fontsize=20)
plt.yticks(fontsize=20)

plt.grid(True, which="both", c='k')

# Plot data #
plt.scatter(Stellar_Mass, Disk_Mass, c='b', s=10, alpha=1, label="$\mathrm{Disk}$")
plt.scatter(Stellar_Mass1, Bulge_Mass1, c='g', s=10, alpha=1, label="$\mathrm{Pseudo\, bulges}$")
plt.scatter(Stellar_Mass2, Bulge_Mass2, c='r', s=10, alpha=1, label="$\mathrm{Classical\, bulges}$")
plt.legend(loc=2, fancybox='True', shadow='True', fontsize=20, markerscale=1)
plt.savefig('ComponentMassVsStellarMass-' + date_string + '.png')

########################################################################################################################

# Generate initial figure #
plt.close()
plt.figure(1, figsize=(18, 10))

# Median and 1-sigma plot parameters #
plt.title(r'$\mathrm{Component\; mass\; versus\; Stellar\; mass}$', fontsize=30)

plt.xlabel(r'$\mathrm{log(M_{\star}\; [M_{\odot}])}$', fontsize=30)
plt.ylabel(r'$\mathrm{log(M_{\star}\; [M_{\odot}])}$', fontsize=30)

plt.xscale('log')
plt.yscale('log')

plt.xlim(1e9, 1e12)
plt.ylim(1e6, 1e13)

plt.xticks(fontsize=20)
plt.yticks(fontsize=20)

plt.grid(True, which="both", c='k')

# Calculate median and 1-sigma for disks #
log10StellarMass = np.log10(Stellar_Mass)
log10StellarMassMax = np.log10(max(Stellar_Mass))
log10StellarMassMin = np.log10(min(Stellar_Mass))
nbin = int((log10StellarMassMax - log10StellarMassMin) / dlog10BulgeMass)
mass = np.empty(nbin)
median = np.empty(nbin)
slow = np.empty(nbin)
shigh = np.empty(nbin)
log10MassLow = log10StellarMassMin
for i in range(nbin):
    index = np.where((log10StellarMass >= log10MassLow) & (log10StellarMass < log10MassLow + dlog10BulgeMass))[0]
    mass[i] = np.mean(Stellar_Mass[index])
    if len(index) > 0:
        median[i] = np.median(Disk_Mass[index])
        slow[i] = np.percentile(Disk_Mass[index], 15.87)
        shigh[i] = np.percentile(Disk_Mass[index], 84.13)
    log10MassLow += dlog10BulgeMass

# Plot median and 1-sigma lines for disks #
plt.plot(mass, median, 'b-', lw=4, label="$\mathrm{Disk\, median}$")
plt.fill_between(mass, shigh, slow, color='blue', alpha='0.5')

# Calculate median and 1-sigma for pseudo bulges #
log10StellarMass = np.log10(Stellar_Mass1)
log10StellarMassMax = np.log10(max(Stellar_Mass1))
log10StellarMassMin = np.log10(min(Stellar_Mass1))
nbin = int((log10StellarMassMax - log10StellarMassMin) / dlog10BulgeMass)
mass = np.empty(nbin)
median = np.empty(nbin)
slow = np.empty(nbin)
shigh = np.empty(nbin)
log10MassLow = log10StellarMassMin
for i in range(nbin):
    index = np.where((log10StellarMass >= log10MassLow) & (log10StellarMass < log10MassLow + dlog10BulgeMass))[0]
    mass[i] = np.mean(Stellar_Mass1[index])
    if len(index) > 0:
        median[i] = np.median(Bulge_Mass1[index])
        slow[i] = np.percentile(Bulge_Mass1[index], 15.87)
        shigh[i] = np.percentile(Bulge_Mass1[index], 84.13)
    log10MassLow += dlog10BulgeMass

# Plot median and 1-sigma lines for pseudo bulges #
plt.plot(mass, median, 'g-', lw=4, label="$\mathrm{Pseudo\, median}$")
plt.fill_between(mass, shigh, slow, color='green', alpha='0.5')

# Calculate median and 1-sigma for classical bulges #
log10StellarMass1 = np.log10(Stellar_Mass2)
log10StellarMassMax1 = np.log10(max(Stellar_Mass2))
log10StellarMassMin1 = np.log10(min(Stellar_Mass2))
nbin = int((log10StellarMassMax1 - log10StellarMassMin1) / dlog10BulgeMass)
mass = np.empty(nbin)
median = np.empty(nbin)
slow = np.empty(nbin)
shigh = np.empty(nbin)
log10MassLow1 = log10StellarMassMin1
for i in range(nbin):
    index = np.where((log10StellarMass1 >= log10MassLow1) & (log10StellarMass1 < log10MassLow1 + dlog10BulgeMass))[0]
    mass[i] = np.mean(Stellar_Mass2[index])
    if len(index) > 0:
        median[i] = np.median(Bulge_Mass2[index])
        slow[i] = np.percentile(Bulge_Mass2[index], 15.87)
        shigh[i] = np.percentile(Bulge_Mass2[index], 84.13)
    log10MassLow1 += dlog10BulgeMass

# Plot median and 1-sigma lines for classical bulges  #
plt.plot(mass, median, 'r-', lw=4, label="$\mathrm{Classical\, median}$")
plt.fill_between(mass, shigh, slow, color='red', alpha='0.5')
plt.legend(loc=2, fancybox='True', shadow='True', fontsize=20, markerscale=1)
plt.savefig('ComponentMassVsStellarMass1-' + date_string + '.png')
