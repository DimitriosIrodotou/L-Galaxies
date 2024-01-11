# Imports #
import h5py
import numpy as np
import matplotlib.pyplot as plt
import time
date_string = time.strftime("%d\%m\%y\%H%M")

# Read in parameters #
outputDir = '/Users/Bam/Astronomy PhD/L-Galaxies/outputs/ALL_ON/output/'

filePrefix = 'SA_output_'
filePostfix = '.h5'
snap = '58'
firstFile = 0
lastFile = 19
maxFile = 512

# First determine the size of the arrays that we need to hold the data #
nGal = 0
for iFile in range(firstFile, lastFile + 1):
    # The following line closes the file at the end of the loop
    with h5py.File(outputDir + filePrefix + '%i' % iFile + filePostfix, 'r') as f:
        nGal += len(f[snap])

# Declare numpy arrays to hold the data #
MDBulgeMass = np.empty(nGal)
MiMDBulgeMass = np.empty(nGal)
MaMDBulgeMass = np.empty(nGal)
IDBulgeMass = np.empty(nGal)
DiskMass = np.empty(nGal)
Type = np.empty(nGal)
StellarMass = np.empty(nGal)

# Read in the data #
iGal = 0
for iFile in range(firstFile, lastFile + 1):
    # The following line closes the file at the end of the loop
    with h5py.File(outputDir + filePrefix + '%i' % iFile + filePostfix, 'r') as f:
        nGalFile = len(f[snap])
        IDBulgeMass[iGal:iGal + nGalFile] = f[snap]['InstabilityDrivenBulgeMass']
        MaMDBulgeMass[iGal:iGal + nGalFile] = f[snap]['MaMergerDrivenBulgeMass']
        MiMDBulgeMass[iGal:iGal + nGalFile] = f[snap]['MiMergerDrivenBulgeMass']
        MDBulgeMass[iGal:iGal + nGalFile] = f[snap]['MergerDrivenBulgeMass']
        DiskMass[iGal:iGal + nGalFile] = f[snap]['DiskMass']
        StellarMass[iGal:iGal + nGalFile] = f[snap]['StellarMass']
        Type[iGal:iGal + nGalFile] = f[snap]['Type']
        iGal += nGalFile

# Physical units #
hubble = 0.678
VelocityUnits = 1  # [Km/s]
LengthUnits = 1e3 / hubble  # [Kpc]
MassUnits = 1e10 / hubble  # [Msun]
SpinUnits = 1e3 / hubble  # [Km/s * Kpc]

dlog10MDBulgeMass = 0.2
dlog10IDBulgeMass = 0.2
dlog10DiskMass = 0.2

# Data #
Disk_Mass = DiskMass * MassUnits
ID_Bulge_Mass = IDBulgeMass * MassUnits
MD_Bulge_Mass = (MaMDBulgeMass + MiMDBulgeMass + MDBulgeMass) * MassUnits
Stellar_Mass = StellarMass * MassUnits

index0 = np.where(Type == 0)
index1 = np.where(Type == 1)
index2 = np.where(Type == 2)

Disk_Mass0 = Disk_Mass[index0]
Disk_Mass1 = Disk_Mass[index1]
Disk_Mass2 = Disk_Mass[index2]

Stellar_Mass0 = Stellar_Mass[index0]
Stellar_Mass1 = Stellar_Mass[index1]
Stellar_Mass2 = Stellar_Mass[index2]

ID_Bulge_Mass0 = ID_Bulge_Mass[index0]
ID_Bulge_Mass1 = ID_Bulge_Mass[index1]
ID_Bulge_Mass2 = ID_Bulge_Mass[index2]

MD_Bulge_Mass0 = MD_Bulge_Mass[index0]
MD_Bulge_Mass1 = MD_Bulge_Mass[index1]
MD_Bulge_Mass2 = MD_Bulge_Mass[index2]

Disk_Ratio0 = np.divide(Disk_Mass0, Stellar_Mass0)
Disk_Ratio1 = np.divide(Disk_Mass1, Stellar_Mass1)
Disk_Ratio2 = np.divide(Disk_Mass2, Stellar_Mass2)

ID_Ratio0 = np.divide(ID_Bulge_Mass0, Stellar_Mass0)
ID_Ratio1 = np.divide(ID_Bulge_Mass1, Stellar_Mass1)
ID_Ratio2 = np.divide(ID_Bulge_Mass2, Stellar_Mass2)

MD_Ratio0 = np.divide(MD_Bulge_Mass0, Stellar_Mass0)
MD_Ratio1 = np.divide(MD_Bulge_Mass1, Stellar_Mass1)
MD_Ratio2 = np.divide(MD_Bulge_Mass2, Stellar_Mass2)

# Generate initial figure #
plt.close()
fig = plt.figure(1, figsize=(30, 15))

# Adjust subplots #
left = 0.055
width = 0.43
bottom = 0.07
height = 0.43
bottom_h = left_h = left + width + 0.062

bl_plot = [left, bottom, width, height]
tl_plot = [left, bottom_h, width, 0.43]
br_plot = [left_h, bottom, 0.43, height]
tr_plot = [left_h, bottom_h, width, height]

# Scatter plot parameters #
fig.add_subplot(223, position=bl_plot)

plt.xlabel(r'$\mathrm{log(M_{\star}\; [M_{\odot}])}$', fontsize=20)
plt.ylabel(r'$\mathrm{Disk\, mass\, /\, Total\, Stellar\, Mass}$', fontsize=20)
plt.xscale('log')

plt.xlim(1e8, 1e12)
plt.ylim(-0.2, 1.2)

plt.xticks(fontsize=15)
plt.yticks(fontsize=15)

plt.grid(True, which="both", c='k')

# Plot data for disks #
# plt.scatter(Stellar_Mass0, Disk_Ratio0, c='Navy', s=20, label="$\mathrm{Disk}$")
# plt.scatter(Stellar_Mass1, Disk_Ratio1, c='RoyalBlue', s=20, label="$\mathrm{Disk}$")
plt.scatter(Stellar_Mass2, Disk_Ratio2, c='PowderBlue', s=20, label="$\mathrm{Disk}$")

# Scatter plot parameters #
fig.add_subplot(221, position=tl_plot)

plt.xlabel(r'$\mathrm{log(M_{\star}\; [M_{\odot}])}$', fontsize=20)
plt.ylabel(r'$\mathrm{Instability-driven\, bulge\, mass\, /\, Total\, Stellar\, Mass}$', fontsize=20)
plt.xscale('log')

plt.xlim(1e8, 1e12)
plt.ylim(-0.2, 1.2)

plt.xticks(fontsize=15)
plt.yticks(fontsize=15)

plt.grid(True, which="both", c='k')

# Plot data for pseudo bulges #
# plt.scatter(Stellar_Mass0, ID_Ratio0, c='DarkGreen', s=20, label="$\mathrm{Pseudo\, bulges}$")
# plt.scatter(Stellar_Mass1, ID_Ratio1, c='MediumSeaGreen', s=20, label="$\mathrm{Pseudo\, bulges}$")
plt.scatter(Stellar_Mass2, ID_Ratio2, c='LightGreen', s=20, label="$\mathrm{Pseudo\, bulges}$")

# Scatter plot parameters #
fig.add_subplot(224, position=br_plot)

plt.xlabel(r'$\mathrm{log(M_{\star}\; [M_{\odot}])}$', fontsize=20)
plt.ylabel(r'$\mathrm{Merger-driven\, bulge\, mass\, /\,  Total\, Stellar\, Mass}$', fontsize=20)

plt.xscale('log')

plt.xlim(1e8, 1e12)
plt.ylim(-0.2, 1.2)

plt.xticks(fontsize=15)
plt.yticks(fontsize=15)

plt.grid(True, which="both", c='k')

# Plot data for classical bulges #
# plt.scatter(Stellar_Mass0, MD_Ratio0, c='DarkRed', s=20, label="$\mathrm{Classical\, bulges}$")
# plt.scatter(Stellar_Mass1, MD_Ratio1, c='Red', s=20, label="$\mathrm{Classical\, bulges}$")
plt.scatter(Stellar_Mass2, MD_Ratio2, c='Salmon', s=20, label="$\mathrm{Classical\, bulges}$")
# plt.legend(loc=4, fancybox='True', shadow='True', fontsize=15, markerscale=1)

# Median and 1-sigma lines plot parameters #
fig.add_subplot(222, position=tr_plot)

plt.xlabel(r'$\mathrm{log(M_{\star}\; [M_{\odot}])}$', fontsize=20)
plt.ylabel(r'$\mathrm{Component\, Mass\, /\, Total\, Stellar\, Mass}$', fontsize=20)

plt.xscale('log')

plt.xlim(1e8, 1e12)
plt.ylim(-0.2, 1.2)

plt.xticks(fontsize=15)
plt.yticks(fontsize=15)

plt.grid(True, which="both", c='k')

# # Calculate median and 1-sigma for disks #
# log10StellarMass = np.log10(Stellar_Mass)
# log10StellarMassMax = np.log10(max(Stellar_Mass))
# log10StellarMassMin = np.log10(min(Stellar_Mass))
# nbin = int((log10StellarMassMax - log10StellarMassMin) / dlog10DiskMass)
# mass = np.empty(nbin)
# median = np.empty(nbin)
# slow = np.empty(nbin)
# shigh = np.empty(nbin)
# log10MassLow = log10StellarMassMin
# for i in range(nbin):
#     index = np.where((log10StellarMass >= log10MassLow) & (log10StellarMass < log10MassLow + dlog10DiskMass))[0]
#     mass[i] = np.mean(Stellar_Mass[index])
#     if len(index) > 0:
#         median[i] = np.median(Disk_Ratio[index])
#         slow[i] = np.percentile(Disk_Ratio[index], 15.87)
#         shigh[i] = np.percentile(Disk_Ratio[index], 84.13)
#     log10MassLow += dlog10DiskMass
#
# # Plot median and 1-sigma lines for disks #
# plt.plot(mass, median, 'b-', lw=4, label="$\mathrm{Disk\, median}$")
# plt.fill_between(mass, shigh, slow, color='blue', alpha='0.5')
#
# # Calculate median and 1-sigma for pseudo bulges #
# log10StellarMass = np.log10(Stellar_Mass)
# log10StellarMassMax = np.log10(max(Stellar_Mass))
# log10StellarMassMin = np.log10(min(Stellar_Mass))
# nbin = int((log10StellarMassMax - log10StellarMassMin) / dlog10IDBulgeMass)
# mass = np.empty(nbin)
# median = np.empty(nbin)
# slow = np.empty(nbin)
# shigh = np.empty(nbin)
# log10MassLow = log10StellarMassMin
# for i in range(nbin):
#     index = np.where((log10StellarMass >= log10MassLow) & (log10StellarMass < log10MassLow + dlog10IDBulgeMass))[0]
#     mass[i] = np.mean(Stellar_Mass[index])
#     if len(index) > 0:
#         median[i] = np.median(ID_Ratio[index])
#         slow[i] = np.percentile(ID_Ratio[index], 15.87)
#         shigh[i] = np.percentile(ID_Ratio[index], 84.13)
#     log10MassLow += dlog10IDBulgeMass
#
# # Plot median and 1-sigma lines for pseudo bulges #
# plt.plot(mass, median, 'g-', lw=4, label="$\mathrm{Pseudo\, median}$")
# plt.fill_between(mass, shigh, slow, color='green', alpha='0.5')
#
# # Calculate median and 1-sigma for classical bulges #
# log10StellarMass1 = np.log10(Stellar_Mass)
# log10StellarMassMax1 = np.log10(max(Stellar_Mass))
# log10StellarMassMin1 = np.log10(min(Stellar_Mass))
# nbin = int((log10StellarMassMax1 - log10StellarMassMin1) / dlog10MDBulgeMass)
# mass = np.empty(nbin)
# median = np.empty(nbin)
# slow = np.empty(nbin)
# shigh = np.empty(nbin)
# log10MassLow1 = log10StellarMassMin1
# for i in range(nbin):
#     index = np.where((log10StellarMass1 >= log10MassLow1) & (log10StellarMass1 < log10MassLow1 + dlog10MDBulgeMass))[0]
#     mass[i] = np.mean(Stellar_Mass[index])
#     if len(index) > 0:
#         median[i] = np.median(MD_Ratio[index])
#         slow[i] = np.percentile(MD_Ratio[index], 15.87)
#         shigh[i] = np.percentile(MD_Ratio[index], 84.13)
#     log10MassLow1 += dlog10MDBulgeMass
#
# # Plot median and 1-sigma lines for classical bulges #
# plt.plot(mass, median, 'r-', lw=4, label="$\mathrm{Classical\, median}$")
# plt.fill_between(mass, shigh, slow, color='red', alpha='0.5')

plt.savefig('ComponentRatioVsStellarMassAllinOneType-' + date_string + '.png')