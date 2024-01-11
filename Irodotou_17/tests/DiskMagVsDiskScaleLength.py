# Determine the size of the arrays that we need to hold the data #
nGal = 0
for iFile in range(firstFile, lastFile + 1):
    # The following line closes the file at the end of the loop
    with h5py.File(outputDir + filePrefix + '%i' % iFile + filePostfix, 'r') as f:
        nGal += len(f[snap])

DiskMass = np.empty(nGal)
BulgeMass = np.empty(nGal)
IDBulgeMass = np.empty(nGal)
ScaleLength = np.empty(nGal)
StellarMass = np.empty(nGal)
DiskMag = np.empty([nGal, 5])

# Read in the data #
iGal = 0
for iFile in range(firstFile, lastFile + 1):
    # The following line closes the file at the end of the loop
    with h5py.File(outputDir + filePrefix + '%i' % iFile + filePostfix, 'r') as f:
        nGalFile = len(f[snap])
        DiskMag[iGal:iGal + nGalFile] = f[snap]['Mag']
        DiskMass[iGal:iGal + nGalFile] = f[snap]['DiskMass']
        BulgeMass[iGal:iGal + nGalFile] = f[snap]['BulgeMass']
        ScaleLength[iGal:iGal + nGalFile] = f[snap]['DiskRadius']
        StellarMass[iGal:iGal + nGalFile] = f[snap]['StellarMass']
        IDBulgeMass[iGal:iGal + nGalFile] = f[snap]['InstabilityDrivenBulgeMass']
        iGal += nGalFile

# Trim the data #
indexID = np.where((IDBulgeMass > 0.7 * BulgeMass) & (DiskMass > 0.7 * StellarMass))

Disk_Mag = zip(*DiskMag[indexID])[3]
Disk_Scale_Length = ScaleLength[indexID] * LengthUnits / 3.0

dDiskScaleLength = 0.2

########################################################################################################################

# Generate initial figure #
plt.close()
plt.figure(1, figsize=(18, 10))

# Scatter plot parameters #
plt.xscale('log')
plt.ylim(-15, -23)
plt.xlim(1e-1, 1e2)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.ylabel(r'$\mathrm{M_{K, disk}}$', fontsize=30)
plt.xlabel(r'$\mathrm{R_{disk}\; [Kpc]}$', fontsize=30)
plt.tick_params(direction='in', which='both', top='on', right='on')

# Plot data #
plt.scatter(Disk_Scale_Length, Disk_Mag, c='k', s=40, label="$\mathrm{Pseudo\, bulges}$")

# Plot observational data #
VBM15M = np.genfromtxt('VBM15M.csv', delimiter=',', names=['x', 'y'])
plt.scatter(np.power(10, VBM15M['x']), VBM15M['y'], c='g', marker='s', s=100, label="$\mathrm{Vaghmare+15}$", zorder=2)

# Calculate median and 1-sigma for pseudo bulges #
Disk_Mag = np.absolute(Disk_Mag)
LogDiskScaleLength = np.log10(Disk_Scale_Length)
LogDiskScaleLengthMax = np.log10(max(Disk_Scale_Length))
LogDiskScaleLengthMin = np.log10(min(Disk_Scale_Length))
nbin = int((LogDiskScaleLengthMax - LogDiskScaleLengthMin) / dDiskScaleLength)
length = np.empty(nbin)
median = np.empty(nbin)
slow = np.empty(nbin)
shigh = np.empty(nbin)
MagLow = LogDiskScaleLengthMin
for i in range(nbin):
    index = np.where((LogDiskScaleLength >= MagLow) & (LogDiskScaleLength < MagLow + dDiskScaleLength))[0]
    length[i] = np.mean(Disk_Scale_Length[index])
    if len(index) > 0:
        median[i] = np.median(Disk_Mag[index])
        slow[i] = np.percentile(Disk_Mag[index], 15.87)
        shigh[i] = np.percentile(Disk_Mag[index], 84.13)
    MagLow += dDiskScaleLength

# Plot median and 1-sigma lines for pseudo bulges #
plt.plot(length, -median, 'r-', lw=4, label="$\mathrm{Median}$")
plt.fill_between(length, -shigh, -slow, color='red', alpha='0.5')

plt.legend(ncol=2, loc=4, fontsize='large')
plt.savefig('DiskMagVsDiskScaleLength-' + snap + date + '.png')