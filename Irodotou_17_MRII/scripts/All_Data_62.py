# Path to the output folder #
OutputPath = '/Volumes/BAM-BLACK/Output_03_MRII/'

# Define the number of tree files, their name and snap number #
firstFile = 40
lastFile = 79
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
Vmax = np.empty(nGal)
CBMass = np.empty(nGal)
PBMass = np.empty(nGal)
ColdGas = np.empty(nGal)
DiskMass = np.empty(nGal)
BulgeMass = np.empty(nGal)
CBMassMajor = np.empty(nGal)
CBMassMinor = np.empty(nGal)
StellarMass = np.empty(nGal)
BlackHoleMass = np.empty(nGal)
DiskSpin = np.empty([nGal, 3])
BulgeSpin = np.empty([nGal, 3])

# Read in the data #
iGal = 0
for iFile in range(firstFile, lastFile + 1):
    # The following line closes the file at the end of the loop
    with h5py.File(OutputPath + filePrefix + '%i' % iFile + filePostfix, 'r') as f:
        nGalFile = len(f[snap])
        # Masses #
        PBMass[iGal:iGal + nGalFile] = f[snap]['PBMass']
        CBMass[iGal:iGal + nGalFile] = f[snap]['CBMass']
        ColdGas[iGal:iGal + nGalFile] = f[snap]['ColdGas']
        DiskMass[iGal:iGal + nGalFile] = f[snap]['DiskMass']
        BulgeMass[iGal:iGal + nGalFile] = f[snap]['BulgeMass']
        StellarMass[iGal:iGal + nGalFile] = f[snap]['StellarMass']
        CBMassMajor[iGal:iGal + nGalFile] = f[snap]['CBMassMajor']
        CBMassMinor[iGal:iGal + nGalFile] = f[snap]['CBMassMinor']
        BlackHoleMass[iGal:iGal + nGalFile] = f[snap]['BlackHoleMass']

        # Spins #
        try:
            DiskSpin[iGal:iGal + nGalFile] = f[snap]['DiskSpin']
            BulgeSpin[iGal:iGal + nGalFile] = f[snap]['BulgeSpin']
        except ValueError as e:
            print(f[snap]['BulgeSpin'])

        # Other properties #
        Vmax[iGal:iGal + nGalFile] = f[snap]['InfallVmax']

        iGal += nGalFile

# Save the arrays so you can load them multiple times in different scripts #
np.save(SavePath + 'PBMass', PBMass)
np.save(SavePath + 'CBMass', CBMass)
np.save(SavePath + 'ColdGas', ColdGas)
np.save(SavePath + 'DiskMass', DiskMass)
np.save(SavePath + 'BulgeMass', BulgeMass)
np.save(SavePath + 'StellarMass', StellarMass)
np.save(SavePath + 'CBMassMajor', CBMassMajor)
np.save(SavePath + 'CBMassMinor', CBMassMinor)
np.save(SavePath + 'BlackHoleMass', BlackHoleMass)

np.save(SavePath + 'DiskSpin', DiskSpin)
np.save(SavePath + 'BulgeSpin', BulgeSpin)

np.save(SavePath + 'Vmax', Vmax)