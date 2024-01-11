# Determine the size of the arrays that we need to hold the data #
nGal = 0
for iFile in range(firstFile, lastFile + 1):
    # The following line closes the file at the end of the loop
    with h5py.File(outputDir + filePrefix + '%i' % iFile + filePostfix, 'r') as f:
        nGal += len(f[snap])

DiskMass = np.empty(nGal)
BulgeSize = np.empty(nGal)
StellarMass = np.empty(nGal)
DiskRadius = np.empty(nGal)

# Read in the data #
iGal = 0
for iFile in range(firstFile, lastFile + 1):
    # The following line closes the file at the end of the loop
    with h5py.File(outputDir + filePrefix + '%i' % iFile + filePostfix, 'r') as f:
        nGalFile = len(f[snap])
        DiskMass[iGal:iGal + nGalFile] = f[snap]['DiskMass']
        BulgeSize[iGal:iGal + nGalFile] = f[snap]['StellarHalfLightRadius']
        DiskRadius[iGal:iGal + nGalFile] = f[snap]['DiskRadius']
        StellarMass[iGal:iGal + nGalFile] = f[snap]['StellarMass']
        iGal += nGalFile

# Trim the data #
index = np.where((DiskMass > 0.7 * StellarMass) & (BulgeSize > 0.0) & (DiskRadius > 0.0))

Bulge_Size = BulgeSize[index] * LengthUnits
Disk_Scale_Length = DiskRadius[index] * LengthUnits / 3.

dBulgeMass = 0.3

########################################################################################################################

# Generate initial figure #
plt.close()
plt.figure(0, figsize=(8, 6))

# Scatter plot parameters #
# plt.xscale('log')
# plt.yscale('log')
plt.ylim(0, 4)
plt.xlim(0, 18)
plt.xlabel(r'$\mathrm{R_{disk}/Kpc}$')
plt.ylabel(r'$\mathrm{R_{50,bulge}/Kpc}$')
plt.tick_params(direction='in', which='both', top='on', right='on')

# Plot L-Galaxies data #
plt.scatter(Disk_Scale_Length, Bulge_Size, color='k', s=10, label="$\mathrm{R_{90} / R_{50} > 2.86}$")

# Plot observational data #
MC02 = np.genfromtxt('MC02.csv', delimiter=',', names=['x', 'y'])
plt.scatter(MC02['x'], MC02['y'], c='g', marker='p', s=50, label="$\mathrm{MacArthur+02}$", zorder=2)

MC02 = np.genfromtxt('Default Dataset.csv', delimiter=',', names=['x', 'y'])
plt.plot(MC02['x'], MC02['y'])

# Calculate median and 1-sigma #
LogBulgeMass = np.log10(Disk_Scale_Length)
LogBulgeMassMax = np.log10(max(Disk_Scale_Length))
LogBulgeMassMin = np.log10(min(Disk_Scale_Length))
nbin = int((LogBulgeMassMax - LogBulgeMassMin) / dBulgeMass)
mass = np.empty(nbin)
median = np.empty(nbin)
slow = np.empty(nbin)
shigh = np.empty(nbin)
logMassLow = LogBulgeMassMin
for i in range(nbin):
    index = np.where((LogBulgeMass >= logMassLow) & (LogBulgeMass < logMassLow + dBulgeMass))[0]
    mass[i] = np.mean(np.absolute(Disk_Scale_Length)[index])
    if len(index) > 0:
        median[i] = np.median(Bulge_Size[index])
        slow[i] = np.percentile(Bulge_Size[index], 15.87)
        shigh[i] = np.percentile(Bulge_Size[index], 84.13)
    logMassLow += dBulgeMass

# Plot median and 1-sigma lines #
plt.plot(mass, median, 'r-', lw=3, label="$\mathrm{Median}$")
plt.fill_between(mass, shigh, slow, color='red', alpha='0.5')

plt.legend(ncol=1, loc=2)
plt.savefig('DiskScaleLength_Vs_BulgeSize-' + snap + date + '.png')

########################################################################################################################
#
# # Generate initial figure #
# plt.close()
# plt.figure(0, figsize=(8, 6))
#
# # Scatter plot parameters #
# plt.xscale('log')
# plt.yscale('log')
# plt.xlim(1e9, 1e12)
# plt.ylim(1e-3, 1e3)
# plt.ylabel(r'$\mathrm{R_{HM}/Kpc}$')
# plt.xlabel(r'$\mathrm{M_{\bigstar}/M_{\odot}}$')
# plt.tick_params(direction='in', which='both', top='on', right='on')
#
# # Calculate median and 1-sigma #
# LogBulgeMass = np.log10(Stellar_Mass)
# LogBulgeMassMax = np.log10(max(Stellar_Mass))
# LogBulgeMassMin = np.log10(min(Stellar_Mass))
# nbin = int((LogBulgeMassMax - LogBulgeMassMin) / dBulgeMass)
# mass = np.empty(nbin)
# median = np.empty(nbin)
# slow = np.empty(nbin)
# shigh = np.empty(nbin)
# logMassLow = LogBulgeMassMin
# for i in range(nbin):
#     index = np.where((LogBulgeMass >= logMassLow) & (LogBulgeMass < logMassLow + dBulgeMass))[0]
#     mass[i] = np.mean(np.absolute(Stellar_Mass)[index])
#     if len(index) > 0:
#         median[i] = np.median(S_H_M_R[index])
#         slow[i] = np.percentile(S_H_M_R[index], 15.87)
#         shigh[i] = np.percentile(S_H_M_R[index], 84.13)
#     logMassLow += dBulgeMass
#
# # Plot median and 1-sigma lines #
# plt.plot(mass, median, 'k-', lw=3, label="$\mathrm{Median}$")
# plt.fill_between(mass, shigh, slow, color='black', alpha='0.5')
#
# # Plot observational data #
# G08 = np.genfromtxt('G08.csv', delimiter=',', names=['x', 'y'])
# plt.plot(np.power(10, G08['x'][2:4]), G08['y'][2:4], color='r', lw=3, label="$\mathrm{Gadotti08\,El}$")
#
# LDR15Ea = np.genfromtxt('LDR15Ea.csv', delimiter=',', names=['x', 'y'])
# plt.plot(LDR15Ea['x'], LDR15Ea['y'], color='g', lw=3, label="$\mathrm{Lange+15 (double-power-law)}$")
#
# LDR15Eb = np.genfromtxt('LDR15Eb.csv', delimiter=',', names=['x', 'y'])
# plt.plot(LDR15Eb['x'], LDR15Eb['y'], color='yellow', lw=3, label="$\mathrm{Lange+15 (single-power-law)}$")
#
# BDL11Eb = np.genfromtxt('BDL11Eb.csv', delimiter=',', names=['x', 'y'])
# plt.plot(np.power(10, BDL11Eb['x']), np.power(10, (BDL11Eb['y'] - 3)), color='orange', lw=3, linestyle='dashed',
#          label="$\mathrm{Baldry+12\, 1\sigma}$")
#
# BDL11Em = np.genfromtxt('BDL11Em.csv', delimiter=',', names=['x', 'y'])
# plt.plot(np.power(10, BDL11Em['x']), np.power(10, (BDL11Em['y'] - 3)), color='orange', lw=3,
#          label="$\mathrm{Baldry+12}$")
#
# BDL11Et = np.genfromtxt('BDL11Et.csv', delimiter=',', names=['x', 'y'])
# plt.plot(np.power(10, BDL11Et['x']), np.power(10, (BDL11Et['y'] - 3)), color='orange', lw=3, linestyle='dashed')
#
# plt.legend(ncol=1, loc=4)
# plt.savefig('StellarMass_Vs_HalfMassRadius_ETGs_Median-' + snap + date + '.png')