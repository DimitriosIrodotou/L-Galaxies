# Path to the output folder #
# outputDir = '/Users/Bam/output/'
outputDir = '/Volumes/BAM-BLACK/output/'


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
    with h5py.File(outputDir + filePrefix + '%i' % iFile + filePostfix, 'r') as f:
        nGal += len(f[snap])
    print('nGal =', nGal)

# Declare numpy arrays to hold the data #
Sfr = np.empty(nGal)
Type = np.empty(nGal)
Vmax = np.empty(nGal)
Vvir = np.empty(nGal)
Rvir = np.empty(nGal)
Mvir = np.empty(nGal)
SHMR = np.empty(nGal)
CBMass = np.empty(nGal)
PBMass = np.empty(nGal)
ColdGas = np.empty(nGal)
DiskMass = np.empty(nGal)
Mag = np.empty([nGal, 40])
BulgeMass = np.empty(nGal)
BulgeSize = np.empty(nGal)
DiskRadius = np.empty(nGal)
H2Fraction = np.empty(nGal)
CBMassMajor = np.empty(nGal)
CBMassMinor = np.empty(nGal)
StellarMass = np.empty(nGal)
MagDust = np.empty([nGal, 40])
ColdGasRadius = np.empty(nGal)
BlackHoleMass = np.empty(nGal)
DiskSpin = np.empty([nGal, 3])
BulgeSpin = np.empty([nGal, 3])
ColdGasSpin = np.empty([nGal, 3])
ColdGasElements = np.empty([nGal, 11])

# Read in the data #
iGal = 0
for iFile in range(firstFile, lastFile + 1):
    # The following line closes the file at the end of the loop
    with h5py.File(outputDir + filePrefix + '%i' % iFile + filePostfix, 'r') as f:
        nGalFile = len(f[snap])
        # Masses #
        # PBMass[iGal:iGal + nGalFile] = f[snap]['PBMass']
        # CBMass[iGal:iGal + nGalFile] = f[snap]['CBMass']
        ColdGas[iGal:iGal + nGalFile] = f[snap]['ColdGas']
        DiskMass[iGal:iGal + nGalFile] = f[snap]['DiskMass']
        BulgeMass[iGal:iGal + nGalFile] = f[snap]['BulgeMass']
        H2Fraction[iGal:iGal + nGalFile] = f[snap]['H2fraction']
        StellarMass[iGal:iGal + nGalFile] = f[snap]['StellarMass']
        # CBMassMajor[iGal:iGal + nGalFile] = f[snap]['CBMassMajor']
        # CBMassMinor[iGal:iGal + nGalFile] = f[snap]['CBMassMinor']
        BlackHoleMass[iGal:iGal + nGalFile] = f[snap]['BlackHoleMass']
        ColdGasElements[iGal:iGal + nGalFile] = f[snap]['ColdGas_elements']


        # Spins #
        DiskSpin[iGal:iGal + nGalFile] = f[snap]['DiskSpin']
        # BulgeSpin[iGal:iGal + nGalFile] = f[snap]['BulgeSpin']
        ColdGasSpin[iGal:iGal + nGalFile] = f[snap]['ColdGasSpin']

        # Sizes #
        BulgeSize[iGal:iGal + nGalFile] = f[snap]['BulgeSize']
        DiskRadius[iGal:iGal + nGalFile] = f[snap]['DiskRadius']
        SHMR[iGal:iGal + nGalFile] = f[snap]['StellarHalfMassRadius']
        ColdGasRadius[iGal:iGal + nGalFile] = f[snap]['ColdGasRadius']

        # Other properties #
        Vmax[iGal:iGal + nGalFile] = f[snap]['InfallVmax']

        iGal += nGalFile

# Save the arrays so you can load them multiple times in different scripts #
np.save('./L-Galaxies_Data/58/PBMass', PBMass)
np.save('./L-Galaxies_Data/58/CBMass', CBMass)
np.save('./L-Galaxies_Data/58/ColdGas', ColdGas)
np.save('./L-Galaxies_Data/58/DiskMass', DiskMass)
np.save('./L-Galaxies_Data/58/BulgeMass', BulgeMass)
np.save('./L-Galaxies_Data/58/H2Fraction', H2Fraction)
np.save('./L-Galaxies_Data/58/StellarMass', StellarMass)
np.save('./L-Galaxies_Data/58/CBMassMajor', CBMassMajor)
np.save('./L-Galaxies_Data/58/CBMassMinor', CBMassMinor)
np.save('./L-Galaxies_Data/58/BlackHoleMass', BlackHoleMass)
np.save('./L-Galaxies_Data/58/ColdGasElements', ColdGasElements)

np.save('./L-Galaxies_Data/58/DiskSpin', DiskSpin)
np.save('./L-Galaxies_Data/58/BulgeSpin', BulgeSpin)
np.save('./L-Galaxies_Data/58/ColdGasSpin', ColdGasSpin)

np.save('./L-Galaxies_Data/58/BulgeSize', BulgeSize)
np.save('./L-Galaxies_Data/58/DiskRadius', DiskRadius)
np.save('./L-Galaxies_Data/58/StellarHalfMassRadius', SHMR)
np.save('./L-Galaxies_Data/58/ColdGasRadius', ColdGasRadius)

np.save(SavePath + 'Vmax', Vmax)
