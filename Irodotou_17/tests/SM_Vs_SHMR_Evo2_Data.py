# Determine the size and declare arrays to hold the data #
nGal = 0
for iFile in range(firstFile, lastFile + 1):
    # The following line closes the file at the end of the loop
    with h5py.File(outputDir + filePrefix + '%i' % iFile + filePostfix, 'r') as f:
        nGal += len(f[snap])

if snap == '38':
    SFR = np.empty(nGal)
    SHMR = np.empty(nGal)
    StellarMass = np.empty(nGal)

# Store data from previous snap #
PreviousSFR = SFR
PreviousSHMR = SHMR
PreviousStellarMass = StellarMass

# Read in the data #
iGal = 0
for iFile in range(firstFile, lastFile + 1):
    # The following line closes the file at the end of the loop
    with h5py.File(outputDir + filePrefix + '%i' % iFile + filePostfix, 'r') as f:
        nGalFile = len(f[snap])
        SFR[iGal:iGal + nGalFile] = f[snap]['Sfr']
        StellarMass[iGal:iGal + nGalFile] = f[snap]['StellarMass']
        SHMR[iGal:iGal + nGalFile] = f[snap]['StellarHalfMassRadius']
        iGal += nGalFile

SFR = np.hstack((PreviousSFR, SFR))
SHMR = np.hstack((PreviousSHMR, SHMR))
StellarMass = np.hstack((PreviousStellarMass, StellarMass))