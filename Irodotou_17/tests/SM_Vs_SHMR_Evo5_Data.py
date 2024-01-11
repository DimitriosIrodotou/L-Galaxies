# Determine the size and declare arrays to hold the data #
nGal = 0
for iFile in range(firstFile, lastFile + 1):
    # The following line closes the file at the end of the loop
    with h5py.File(outputDir + filePrefix + '%i' % iFile + filePostfix, 'r') as f:
        nGal += len(f[snap])

if snap == '51':
    SHMR = np.empty(nGal)
    BulgeMass = np.empty(nGal)
    StellarMass = np.empty(nGal)

# Store data from previous snap #
PreviousSHMR = SHMR
PreviousBulgeMass = BulgeMass
PreviousStellarMass = StellarMass

# Read in the data #
iGal = 0
for iFile in range(firstFile, lastFile + 1):
    # The following line closes the file at the end of the loop
    with h5py.File(outputDir + filePrefix + '%i' % iFile + filePostfix, 'r') as f:
        nGalFile = len(f[snap])
        BulgeMass[iGal:iGal + nGalFile] = f[snap]['BulgeMass']
        StellarMass[iGal:iGal + nGalFile] = f[snap]['StellarMass']
        SHMR[iGal:iGal + nGalFile] = f[snap]['StellarHalfMassRadius']
        iGal += nGalFile

SHMR = np.hstack((PreviousSHMR, SHMR))
BulgeMass = np.hstack((PreviousBulgeMass, BulgeMass))
StellarMass = np.hstack((PreviousStellarMass, StellarMass))