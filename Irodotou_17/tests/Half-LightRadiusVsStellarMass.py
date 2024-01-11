# Imports #
import h5py
import numpy as np
import matplotlib.pyplot as plt
import time

# date_string = time.strftime("%d\%m\%y\%H%M")

# Read in parameters #
# outputDir = '/Users/Bam/Astronomy Phd/Development_Branch/outputs/Driven_DI/'
snap = '58'
# firstFile = 0
# lastFile = 9

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
StellarMass = np.empty(nGal)
HMR = np.empty(nGal)
Ninety = np.empty(nGal)
Fifty = np.empty(nGal)

# Read in the data #
iGal = 0
for iFile in range(firstFile, lastFile + 1):
    # The following line closes the file at the end of the loop
    with h5py.File(outputDir + filePrefix + '%i' % iFile + filePostfix, 'r') as f:
        nGalFile = len(f[snap])
        IDBulgeMass[iGal:iGal + nGalFile] = f[snap]['InstabilityDrivenBulgeMass']
        MDBulgeMass[iGal:iGal + nGalFile] = f[snap]['MergerDrivenBulgeMass']
        BulgeMass[iGal:iGal + nGalFile] = f[snap]['BulgeMass']
        StellarMass[iGal:iGal + nGalFile] = f[snap]['StellarMass']
        HMR[iGal:iGal + nGalFile] = f[snap]['StellarHalfMassRadius']
        Ninety[iGal:iGal + nGalFile] = f[snap]['StellarNinetyLightRadius']
        Fifty[iGal:iGal + nGalFile] = f[snap]['StellarHalfLightRadius']
        iGal += nGalFile

# Physical units #
hubble = 0.678
VelocityUnits = 1  # [Km/s]
LengthUnits = 1e3 / hubble  # [Kpc]
MassUnits = 1e10 / hubble  # [Msun]
SpinUnits = 1e3 / hubble  # [Km/s * Kpc]

dlog10StellarMass = 0.25
dlog10StellarMass1 = 0.5

# Ellipticals #
indexEll = np.where((Ninety > 2.5 * Fifty) & (Ninety < 10 * Fifty))

# ID bulge dominated #
indexID = np.where(IDBulgeMass > 0.6 * BulgeMass)

# MD bulge dominated #
indexMD = np.where((Ninety > 2.5 * Fifty) & (Ninety < 6 * Fifty) & (MDBulgeMass > 0.6 * BulgeMass))

# Data #
Bulge_Mass1 = IDBulgeMass[indexID] * MassUnits
Bulge_Mass2 = MDBulgeMass[indexMD] * MassUnits
Bulge_Mass3 = BulgeMass[indexEll] * MassUnits
H_M_R1 = HMR[indexID] * LengthUnits
H_M_R2 = HMR[indexMD] * LengthUnits
H_M_R3 = HMR[indexEll] * LengthUnits

# Generate initial figure #
plt.close()
plt.figure(1, figsize=(18, 10))

# Scatter plot parameters #
plt.title(r'$\mathrm{Half-mass\; \;radius \;versus \;stellar \;mass}$', fontsize=30)

plt.xlabel(r'$\mathrm{M_{\star}\; [M_{\odot}]}$', fontsize=30)
plt.ylabel(r'$\mathrm{R_{50}\; [Kpc]}$', fontsize=30)

plt.xscale('log')
plt.yscale('log')

plt.xlim(1e8, 1e12)
plt.ylim(1e-1, 1e2)

plt.xticks(fontsize=20)
plt.yticks(fontsize=20)

plt.grid(True, which="both", c='k')

# Plotting data #
plt.scatter(Bulge_Mass1, H_M_R1, c='b', s=10, label="$\mathrm{Pseudo\, bulges}$", zorder=3)
plt.scatter(Bulge_Mass2, H_M_R2, c='g', s=10, label="$\mathrm{Classical\, bulges}$", zorder=2)
plt.scatter(Bulge_Mass3, H_M_R3, c='r', s=10, label="$\mathrm{Ellipticals}$", zorder=1)

G08 = np.genfromtxt('G08.csv', delimiter=',', names=['x', 'y'])
plt.plot(np.power(10,G08['x'][0:2]), G08['y'][0:2], color='b', lw=3, label="$\mathrm{Gadotti08\,PB}$")
plt.plot(np.power(10,G08['x'][2:4]), G08['y'][2:4], color='r', lw=3, label="$\mathrm{Gadotti08\,El}$")
plt.plot(np.power(10,G08['x'][4:6]), G08['y'][4:6], color='g', lw=3, label="$\mathrm{Gadotti08\,CB}$")


plt.legend(loc=2, fancybox='True', shadow='True', fontsize=20, markerscale=1)
plt.savefig('Half-LightRadiusVsStellarMass-' + snap + '.png')

########################################################################################################################

# Generate initial figure #
plt.close()
plt.figure(1, figsize=(18, 10))

# Scatter plot parameters #
plt.title(r'$\mathrm{Half-mass\; \;radius \;versus \;stellar \;mass}$', fontsize=30)

plt.xlabel(r'$\mathrm{M_{\star}\; [M_{\odot}]}$', fontsize=30)
plt.ylabel(r'$\mathrm{R_{50}\; [Kpc]}$', fontsize=30)

plt.xscale('log')
plt.yscale('log')

plt.xlim(1e8, 1e12)
plt.ylim(1e-1, 1e2)

plt.xticks(fontsize=20)
plt.yticks(fontsize=20)

plt.grid(True, which="both", c='k')

# Calculating median and 1-sigma for pseudo bulges #
log10StellarMass = np.log10(Bulge_Mass1)
log10StellarMassMax = np.log10(max(Bulge_Mass1))
log10StellarMassMin = np.log10(min(Bulge_Mass1))
nbin = int((log10StellarMassMax - log10StellarMassMin) / dlog10StellarMass)
mass = np.empty(nbin)
median = np.empty(nbin)
slow = np.empty(nbin)
shigh = np.empty(nbin)
log10MassLow = log10StellarMassMin
for i in range(nbin):
    index = np.where((log10StellarMass >= log10MassLow) & (log10StellarMass < log10MassLow + dlog10StellarMass))[0]
    mass[i] = np.mean(Bulge_Mass1[index])
    if len(index) > 0:
        median[i] = np.median(H_M_R1[index])
        slow[i] = np.percentile(H_M_R1[index], 15.87)
        shigh[i] = np.percentile(H_M_R1[index], 84.13)
    log10MassLow += dlog10StellarMass

# Plotting median and 1-sigma lines #
plt.plot(mass, median, 'b-', label="$\mathrm{Pseudo\, median}$", lw=4)
plt.fill_between(mass, shigh, slow, color='blue', alpha='0.5')

# Calculating median and 1-sigma for classical bulge #
log10StellarMass = np.log10(Bulge_Mass2)
log10StellarMassMax = np.log10(max(Bulge_Mass2))
log10StellarMassMin = np.log10(min(Bulge_Mass2))
nbin = int((log10StellarMassMax - log10StellarMassMin) / dlog10StellarMass)
mass = np.empty(nbin)
median = np.empty(nbin)
slow = np.empty(nbin)
shigh = np.empty(nbin)
log10MassLow = log10StellarMassMin
for i in range(nbin):
    index = np.where((log10StellarMass >= log10MassLow) & (log10StellarMass < log10MassLow + dlog10StellarMass))[0]
    mass[i] = np.mean(Bulge_Mass2[index])
    if len(index) > 0:
        median[i] = np.median(H_M_R2[index])
        slow[i] = np.percentile(H_M_R2[index], 15.87)
        shigh[i] = np.percentile(H_M_R2[index], 84.13)
    log10MassLow += dlog10StellarMass

## Plotting median and 1-sigma.
plt.plot(mass, median, 'g-', label="$\mathrm{Classical\, median}$", lw=4)
plt.fill_between(mass, shigh, slow, color='green', alpha='0.5')

# Median and 1-sigma for ellipticals #
log10StellarMass = np.log10(Bulge_Mass3)
log10StellarMassMax = np.log10(max(Bulge_Mass3))
log10StellarMassMin = np.log10(min(Bulge_Mass3))
nbin = int((log10StellarMassMax - log10StellarMassMin) / dlog10StellarMass)
mass = np.empty(nbin)
median = np.empty(nbin)
slow = np.empty(nbin)
shigh = np.empty(nbin)
log10MassLow = log10StellarMassMin
for i in range(nbin):
    index = np.where((log10StellarMass >= log10MassLow) & (log10StellarMass < log10MassLow + dlog10StellarMass))[0]
    mass[i] = np.mean(Bulge_Mass3[index])
    if len(index) > 0:
        median[i] = np.median(H_M_R3[index])
        slow[i] = np.percentile(H_M_R3[index], 15.87)
        shigh[i] = np.percentile(H_M_R3[index], 84.13)
    log10MassLow += dlog10StellarMass

## Plotting median and 1-sigma.
plt.plot(mass, median, 'r-', label="$\mathrm{Ellipticals\, median}$", lw=4)
plt.fill_between(mass, shigh, slow, color='red', alpha='0.5')

plt.plot(np.power(10,G08['x'][0:2]), G08['y'][0:2], color='b', lw=3, label="$\mathrm{Gadotti08\,PB}$")
plt.plot(np.power(10,G08['x'][2:4]), G08['y'][2:4], color='r', lw=3, label="$\mathrm{Gadotti08\,El}$")
plt.plot(np.power(10,G08['x'][4:6]), G08['y'][4:6], color='g', lw=3, label="$\mathrm{Gadotti08\,CB}$")

plt.legend(loc=2, fancybox='True', shadow='True', fontsize=20, markerscale=1)
plt.savefig('Half-LightRadiusVsStellarMass1-' + snap + '.png')
