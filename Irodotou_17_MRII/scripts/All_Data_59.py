# Path to the output folder #
OutputPath = '/Volumes/BAM-BLACK/output/'

# Define the number of tree files, their name and snap number #
firstFile = 1
lastFile = 511
maxFile = 512
filePostfix = '.h5'
filePrefix = 'SA_output_'

# Determine the size and declare arrays to hold the data #
nGal = 0
for iFile in range(firstFile, lastFile + 1):
    # The following line closes the file at the end of the loop
    with h5py.File(OutputPath + filePrefix + '%i' % iFile + filePostfix, 'r') as f:
        nGal += len(f[snap])
    print('nGal =', nGal)

# Declare numpy arrays to hold the data #
SHMR = np.empty(nGal)
CBMass = np.empty(nGal)
DiskMass = np.empty(nGal)
StellarMass = np.empty(nGal)

# Read in the data #
iGal = 0
for iFile in range(firstFile, lastFile + 1):
    # The following line closes the file at the end of the loop
    with h5py.File(OutputPath + filePrefix + '%i' % iFile + filePostfix, 'r') as f:
        nGalFile = len(f[snap])
        # Masses #
        CBMass[iGal:iGal + nGalFile] = f[snap]['CBMass']
        DiskMass[iGal:iGal + nGalFile] = f[snap]['DiskMass']
        StellarMass[iGal:iGal + nGalFile] = f[snap]['StellarMass']

        # Sizes #
        SHMR[iGal:iGal + nGalFile] = f[snap]['StellarHalfMassRadius']

        iGal += nGalFile

# Save the arrays so you can load them multiple times in different scripts #
np.save(SavePath + 'CBMass', CBMass)
np.save(SavePath + 'DiskMass', DiskMass)
np.save(SavePath + 'StellarMass', StellarMass)

np.save(SavePath + 'StellarHalfMassRadius', SHMR)