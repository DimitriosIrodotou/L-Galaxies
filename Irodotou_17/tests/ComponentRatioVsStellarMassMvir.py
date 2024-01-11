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
lastFile = 9
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
StellarMass = np.empty(nGal)
Mvir = np.empty(nGal)

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
        Mvir[iGal:iGal + nGalFile] = f[snap]['Mvir']
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
MD_Bulge_Mass = (MaMDBulgeMass + MiMDBulgeMass) * MassUnits
Stellar_Mass = StellarMass * MassUnits
M_vir = Mvir * MassUnits

Disk_Ratio = np.divide(Disk_Mass, Stellar_Mass)
ID_Ratio = np.divide(ID_Bulge_Mass, Stellar_Mass)
MD_Ratio = np.divide(MD_Bulge_Mass, Stellar_Mass)

# Generate initial figure #
# plt.close()
# fig = plt.figure(1, figsize=(25, 15))
#
# Scatter plot parameters #
# plt.title(r'$\mathrm{Component\; to\; total\; mass\; ratio\; versus\; Stellar\; mass}$', fontsize=30)
#
# plt.xlabel(r'$\mathrm{log(M_{\star}\; [M_{\odot}])}$', fontsize=30)
# plt.ylabel(r'$\mathrm{Component/Total}$', fontsize=30)
#
# plt.xscale('log')
#
# plt.xlim(1e9, 1e12)
# plt.ylim(-0.3, 1.2)
#
# plt.xticks(fontsize=20)
# plt.yticks(fontsize=20)
#
# plt.grid(True, which="both", c='k')
#
# Plot data #
# plt.scatter(Stellar_Mass, Disk_Ratio, c='b', s=10, alpha=1, label="$\mathrm{Disk}$", zorder=1)
# plt.scatter(Stellar_Mass, ID_Ratio, c='g', s=10, alpha=1, label="$\mathrm{Pseudo\, bulges}$", zorder=4)
# plt.scatter(Stellar_Mass, MD_Ratio, c='r', s=10, alpha=1, label="$\mathrm{Classical\, bulges}$", zorder=3)
# plt.legend(loc=2, fancybox='True', shadow='True', fontsize=20, markerscale=1)
# plt.savefig('ComponentRatioVsStellarMass-' + date_string + '.png')

########################################################################################################################
#
# # Generate initial figure #
# plt.close()
# fig = plt.figure(1, figsize=(20, 15))
#
# # Median and 1-sigma plot parameters #
# plt.title(r'$\mathrm{Component\; to\; total\; mass\; ratio\; versus\; Stellar\; mass}$', fontsize=30)
#
# plt.xlabel(r'$\mathrm{log(M_{\star}\; [M_{\odot}])}$', fontsize=30)
# plt.ylabel(r'$\mathrm{Component/Total}$', fontsize=30)
#
# plt.xscale('log')
#
# plt.xlim(1e9, 1e12)
# plt.ylim(-0.3, 1.2)
#
# plt.xticks(fontsize=20)
# plt.yticks(fontsize=20)
#
# plt.grid(True, which="both", c='k')
#
# Calculate median and 1-sigma for disks #
# log10StellarMass = np.log10(Stellar_Mass)
# log10StellarMassMax = np.log10(max(Stellar_Mass))
# log10StellarMassMin = np.log10(min(Stellar_Mass))
# nbin = int((log10StellarMassMax - log10StellarMassMin) / dlog10BulgeMass)
# mass = np.empty(nbin)
# median = np.empty(nbin)
# slow = np.empty(nbin)
# shigh = np.empty(nbin)
# log10MassLow = log10StellarMassMin
# for i in range(nbin):
#     index = np.where((log10StellarMass >= log10MassLow) & (log10StellarMass < log10MassLow + dlog10BulgeMass))[0]
#     mass[i] = np.mean(Stellar_Mass[index])
#     if len(index) > 0:
#         median[i] = np.median(Disk_Ratio[index])
#         slow[i] = np.percentile(Disk_Ratio[index], 15.87)
#         shigh[i] = np.percentile(Disk_Ratio[index], 84.13)
#     log10MassLow += dlog10BulgeMass
#
# Plot median and 1-sigma lines for disks #
# plt.plot(mass, median, 'b-', label="$\mathrm{Disk\, median}$", lw=4)
# plt.fill_between(mass, shigh, slow, color='blue', alpha='0.5', zorder=2)
#
# Calculate median and 1-sigma for pseudo bulges #
# log10StellarMass = np.log10(Stellar_Mass)
# log10StellarMassMax = np.log10(max(Stellar_Mass))
# log10StellarMassMin = np.log10(min(Stellar_Mass))
# nbin = int((log10StellarMassMax - log10StellarMassMin) / dlog10BulgeMass)
# mass = np.empty(nbin)
# median = np.empty(nbin)
# slow = np.empty(nbin)
# shigh = np.empty(nbin)
# log10MassLow = log10StellarMassMin
# for i in range(nbin):
#     index = np.where((log10StellarMass >= log10MassLow) & (log10StellarMass < log10MassLow + dlog10BulgeMass))[0]
#     mass[i] = np.mean(Stellar_Mass[index])
#     if len(index) > 0:
#         median[i] = np.median(ID_Ratio[index])
#         slow[i] = np.percentile(ID_Ratio[index], 15.87)
#         shigh[i] = np.percentile(ID_Ratio[index], 84.13)
#     log10MassLow += dlog10BulgeMass
#
# Plot median and 1-sigma lines for pseudo bulges #
# plt.plot(mass, median, 'g-', label="$\mathrm{Pseudo\, median}$", lw=4)
# plt.fill_between(mass, shigh, slow, color='green', alpha='0.5', zorder=2)
#
# Calculate median and 1-sigma for classical bulges #
# log10StellarMass1 = np.log10(Stellar_Mass)
# log10StellarMassMax1 = np.log10(max(Stellar_Mass))
# log10StellarMassMin1 = np.log10(min(Stellar_Mass))
# nbin = int((log10StellarMassMax1 - log10StellarMassMin1) / dlog10BulgeMass)
# mass = np.empty(nbin)
# median = np.empty(nbin)
# slow = np.empty(nbin)
# shigh = np.empty(nbin)
# log10MassLow1 = log10StellarMassMin1
# for i in range(nbin):
#     index = np.where((log10StellarMass1 >= log10MassLow1) & (log10StellarMass1 < log10MassLow1 + dlog10BulgeMass))[0]
#     mass[i] = np.mean(Stellar_Mass[index])
#     if len(index) > 0:
#         median[i] = np.median(MD_Ratio[index])
#         slow[i] = np.percentile(MD_Ratio[index], 15.87)
#         shigh[i] = np.percentile(MD_Ratio[index], 84.13)
#     log10MassLow1 += dlog10BulgeMass
#
# Plot median and 1-sigma lines for classical bulges #
# plt.plot(mass, median, 'r-', label="$\mathrm{Classical\, median}$", lw=4)
# plt.fill_between(mass, shigh, slow, color='red', alpha='0.5', zorder=1)
# plt.legend(loc=2, fancybox='True', shadow='True', fontsize=20, markerscale=1)
# plt.savefig('ComponentRatioVsStellarMass1-' + date_string + '.png')

########################################################################################################################

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

# plt.xlim(1e8, 1e12)
plt.ylim(-0.2, 1.2)

plt.xticks(fontsize=15)
plt.yticks(fontsize=15)

plt.grid(True, which="both", c='k')

# Plot data for disks #
plt.scatter(M_vir, Disk_Ratio, c='b', s=10, label="$\mathrm{Disk}$")
# plt.legend(loc=4, fancybox='True', shadow='True', fontsize=15, markerscale=1)

# Scatter plot parameters #
fig.add_subplot(221, position=tl_plot)

plt.xlabel(r'$\mathrm{log(M_{\star}\; [M_{\odot}])}$', fontsize=20)
plt.ylabel(r'$\mathrm{Instability-driven\, bulge\, mass\, /\, Total\, Stellar\, Mass}$', fontsize=20)
plt.xscale('log')

# plt.xlim(1e8, 1e12)
plt.ylim(-0.2, 1.2)

plt.xticks(fontsize=15)
plt.yticks(fontsize=15)

plt.grid(True, which="both", c='k')

# Plot data for pseudo bulges #
plt.scatter(M_vir, ID_Ratio, c='g', s=10, label="$\mathrm{Pseudo\, bulges}$")
# plt.legend(loc=4, fancybox='True', shadow='True', fontsize=15, markerscale=1)

# Scatter plot parameters #
fig.add_subplot(224, position=br_plot)

plt.xlabel(r'$\mathrm{log(M_{\star}\; [M_{\odot}])}$', fontsize=20)
plt.ylabel(r'$\mathrm{Merger-driven\, bulge\, mass\, /\,  Total\, Stellar\, Mass}$', fontsize=20)

plt.xscale('log')

# plt.xlim(1e8, 1e12)
plt.ylim(-0.2, 1.2)

plt.xticks(fontsize=15)
plt.yticks(fontsize=15)

plt.grid(True, which="both", c='k')

# Plot data for classical bulges #
plt.scatter(M_vir, MD_Ratio, c='r', s=10, label="$\mathrm{Classical\, bulges}$")
# plt.legend(loc=4, fancybox='True', shadow='True', fontsize=15, markerscale=1)

# Median and 1-sigma lines plot parameters #
fig.add_subplot(222, position=tr_plot)

plt.xlabel(r'$\mathrm{log(M_{\star}\; [M_{\odot}])}$', fontsize=20)
plt.ylabel(r'$\mathrm{Component\, Mass\, /\, Total\, Stellar\, Mass}$', fontsize=20)

plt.xscale('log')

# plt.xlim(1e8, 1e12)
plt.ylim(-0.2, 1.2)

plt.xticks(fontsize=15)
plt.yticks(fontsize=15)

plt.grid(True, which="both", c='k')

# Calculate median and 1-sigma for disks #
log10StellarMass = np.log10(M_vir)
log10StellarMassMax = np.log10(max(M_vir))
log10StellarMassMin = np.log10(min(M_vir))
nbin = int((log10StellarMassMax - log10StellarMassMin) / dlog10DiskMass)
mass = np.empty(nbin)
median = np.empty(nbin)
slow = np.empty(nbin)
shigh = np.empty(nbin)
log10MassLow = log10StellarMassMin
for i in range(nbin):
    index = np.where((log10StellarMass >= log10MassLow) & (log10StellarMass < log10MassLow + dlog10DiskMass))[0]
    mass[i] = np.mean(M_vir[index])
    if len(index) > 0:
        median[i] = np.median(Disk_Ratio[index])
        slow[i] = np.percentile(Disk_Ratio[index], 15.87)
        shigh[i] = np.percentile(Disk_Ratio[index], 84.13)
    log10MassLow += dlog10DiskMass

# Plot median and 1-sigma lines for disks #
plt.plot(mass, median, 'b-', lw=4, label="$\mathrm{Disk\, median}$")
plt.fill_between(mass, shigh, slow, color='blue', alpha='0.5')

# Calculate median and 1-sigma for pseudo bulges #
log10StellarMass = np.log10(M_vir)
log10StellarMassMax = np.log10(max(M_vir))
log10StellarMassMin = np.log10(min(M_vir))
nbin = int((log10StellarMassMax - log10StellarMassMin) / dlog10IDBulgeMass)
mass = np.empty(nbin)
median = np.empty(nbin)
slow = np.empty(nbin)
shigh = np.empty(nbin)
log10MassLow = log10StellarMassMin
for i in range(nbin):
    index = np.where((log10StellarMass >= log10MassLow) & (log10StellarMass < log10MassLow + dlog10IDBulgeMass))[0]
    mass[i] = np.mean(M_vir[index])
    if len(index) > 0:
        median[i] = np.median(ID_Ratio[index])
        slow[i] = np.percentile(ID_Ratio[index], 15.87)
        shigh[i] = np.percentile(ID_Ratio[index], 84.13)
    log10MassLow += dlog10IDBulgeMass

# Plot median and 1-sigma lines for pseudo bulges #
plt.plot(mass, median, 'g-', lw=4, label="$\mathrm{Pseudo\, median}$")
plt.fill_between(mass, shigh, slow, color='green', alpha='0.5')

# Calculate median and 1-sigma for classical bulges #
log10StellarMass1 = np.log10(M_vir)
log10StellarMassMax1 = np.log10(max(M_vir))
log10StellarMassMin1 = np.log10(min(M_vir))
nbin = int((log10StellarMassMax1 - log10StellarMassMin1) / dlog10MDBulgeMass)
mass = np.empty(nbin)
median = np.empty(nbin)
slow = np.empty(nbin)
shigh = np.empty(nbin)
log10MassLow1 = log10StellarMassMin1
for i in range(nbin):
    index = np.where((log10StellarMass1 >= log10MassLow1) & (log10StellarMass1 < log10MassLow1 + dlog10MDBulgeMass))[0]
    mass[i] = np.mean(M_vir[index])
    if len(index) > 0:
        median[i] = np.median(MD_Ratio[index])
        slow[i] = np.percentile(MD_Ratio[index], 15.87)
        shigh[i] = np.percentile(MD_Ratio[index], 84.13)
    log10MassLow1 += dlog10MDBulgeMass

# Plot median and 1-sigma lines for classical bulges #
plt.plot(mass, median, 'r-', lw=4, label="$\mathrm{Classical\, median}$")
plt.fill_between(mass, shigh, slow, color='red', alpha='0.5')
plt.savefig('ComponentRatioVsStellarMassAllinOne-' + date_string + '.png')

########################################################################################################################

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
h = plt.hexbin(Stellar_Mass, Disk_Ratio, xscale='log', bins='log', cmap=plt.cm.Blues_r, mincnt=1)

# Adjust the color bar #
cbaxes = fig.add_axes([0.475, 0.131, 0.01, 0.308])
cb = plt.colorbar(h, cax=cbaxes)

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
h = plt.hexbin(Stellar_Mass, ID_Ratio, xscale='log', bins='log', cmap=plt.cm.Greens_r, mincnt=1)

# Adjust the color bar #
cbaxes = fig.add_axes([0.475, 0.608, 0.01, 0.308])
cb = plt.colorbar(h, cax=cbaxes)

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
h = plt.hexbin(Stellar_Mass, MD_Ratio, xscale='log', bins='log', cmap=plt.cm.Reds_r, mincnt=1)

# Adjust the color bar #
cbaxes = fig.add_axes([0.967, 0.131, 0.01, 0.308])
cb = plt.colorbar(h, cax=cbaxes)

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

# Calculate median and 1-sigma for disks #
log10StellarMass = np.log10(Stellar_Mass)
log10StellarMassMax = np.log10(max(Stellar_Mass))
log10StellarMassMin = np.log10(min(Stellar_Mass))
nbin = int((log10StellarMassMax - log10StellarMassMin) / dlog10DiskMass)
mass = np.empty(nbin)
median = np.empty(nbin)
slow = np.empty(nbin)
shigh = np.empty(nbin)
log10MassLow = log10StellarMassMin
for i in range(nbin):
    index = np.where((log10StellarMass >= log10MassLow) & (log10StellarMass < log10MassLow + dlog10DiskMass))[0]
    mass[i] = np.mean(Stellar_Mass[index])
    if len(index) > 0:
        median[i] = np.median(Disk_Ratio[index])
        slow[i] = np.percentile(Disk_Ratio[index], 15.87)
        shigh[i] = np.percentile(Disk_Ratio[index], 84.13)
    log10MassLow += dlog10DiskMass

# Plot median and 1-sigma lines for disks #
plt.plot(mass, median, 'b-', lw=4, label="$\mathrm{Disk\, median}$")
plt.fill_between(mass, shigh, slow, color='blue', alpha='0.5')

# Calculate median and 1-sigma for pseudo bulges #
log10StellarMass = np.log10(Stellar_Mass)
log10StellarMassMax = np.log10(max(Stellar_Mass))
log10StellarMassMin = np.log10(min(Stellar_Mass))
nbin = int((log10StellarMassMax - log10StellarMassMin) / dlog10IDBulgeMass)
mass = np.empty(nbin)
median = np.empty(nbin)
slow = np.empty(nbin)
shigh = np.empty(nbin)
log10MassLow = log10StellarMassMin
for i in range(nbin):
    index = np.where((log10StellarMass >= log10MassLow) & (log10StellarMass < log10MassLow + dlog10IDBulgeMass))[0]
    mass[i] = np.mean(Stellar_Mass[index])
    if len(index) > 0:
        median[i] = np.median(ID_Ratio[index])
        slow[i] = np.percentile(ID_Ratio[index], 15.87)
        shigh[i] = np.percentile(ID_Ratio[index], 84.13)
    log10MassLow += dlog10IDBulgeMass

# Plot median and 1-sigma lines for pseudo bulges #
plt.plot(mass, median, 'g-', lw=4, label="$\mathrm{Pseudo\, median}$")
plt.fill_between(mass, shigh, slow, color='green', alpha='0.5')

# Calculate median and 1-sigma for classical bulges #
log10StellarMass1 = np.log10(Stellar_Mass)
log10StellarMassMax1 = np.log10(max(Stellar_Mass))
log10StellarMassMin1 = np.log10(min(Stellar_Mass))
nbin = int((log10StellarMassMax1 - log10StellarMassMin1) / dlog10MDBulgeMass)
mass = np.empty(nbin)
median = np.empty(nbin)
slow = np.empty(nbin)
shigh = np.empty(nbin)
log10MassLow1 = log10StellarMassMin1
for i in range(nbin):
    index = np.where((log10StellarMass1 >= log10MassLow1) & (log10StellarMass1 < log10MassLow1 + dlog10MDBulgeMass))[0]
    mass[i] = np.mean(Stellar_Mass[index])
    if len(index) > 0:
        median[i] = np.median(MD_Ratio[index])
        slow[i] = np.percentile(MD_Ratio[index], 15.87)
        shigh[i] = np.percentile(MD_Ratio[index], 84.13)
    log10MassLow1 += dlog10MDBulgeMass

# Plot median and 1-sigma lines for classical bulges #
plt.plot(mass, median, 'r-', lw=4, label="$\mathrm{Classical\, median}$")
plt.fill_between(mass, shigh, slow, color='red', alpha='0.5')
plt.savefig('ComponentRatioVsStellarMassHex-' + date_string + '.png')