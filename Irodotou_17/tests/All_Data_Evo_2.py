# Path to the output folder #
OutputPath = '/Volumes/BAM-BLACK/Outputs/output_all/'

# Define the number of tree files, their name and snap number #
firstFile = 0
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
Sfr = np.empty(nGal)
Vmax = np.empty(nGal)
Type = np.empty(nGal)
DiskMass = np.empty(nGal)
ColdGas = np.empty(nGal)
StellarMass = np.empty(nGal)

# Read in the data #
iGal = 0
for iFile in range(firstFile, lastFile + 1):
    # The following line closes the file at the end of the loop
    with h5py.File(OutputPath + filePrefix + '%i' % iFile + filePostfix, 'r') as f:
        nGalFile = len(f[snap])
        # Masses #
        ColdGas[iGal:iGal + nGalFile] = f[snap]['ColdGas']
        DiskMass[iGal:iGal + nGalFile] = f[snap]['DiskMass']
        StellarMass[iGal:iGal + nGalFile] = f[snap]['StellarMass']

        # Other properties #
        Sfr[iGal:iGal + nGalFile] = f[snap]['Sfr']
        Type[iGal:iGal + nGalFile] = f[snap]['Type']
        Vmax[iGal:iGal + nGalFile] = f[snap]['Vmax']

        iGal += nGalFile

# Save the arrays so you can load them multiple times in different scripts #
np.save(SavePath + '/ColdGas', ColdGas)
np.save(SavePath + '/DiskMass', DiskMass)
np.save(SavePath + '/StellarMass', StellarMass)

# Other properties #
np.save(SavePath + '/Sfr', Sfr)
np.save(SavePath + '/Type', Type)
np.save(SavePath + '/Vmax', Vmax)
