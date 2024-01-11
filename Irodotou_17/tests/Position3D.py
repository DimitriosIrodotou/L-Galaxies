# Imports #
import h5py
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import time

# date_string = time.strftime("%d\%m\%y\%H%M")

# Read in parameters #
# outputDir = '/Users/Bam/output/'
# filePrefix = 'SA_output_'
# filePostfix = '.h5'
snap = '58'  # z = 1.48
# firstFile = 0
# lastFile = 19

# First determine the size of the arrays that we need to hold the data #
nGal = 0
for iFile in range(firstFile, lastFile + 1):
    # The following line closes the file at the end of the loop
    with h5py.File(outputDir + filePrefix + '%i' % iFile + filePostfix, 'r') as f:
        nGal += len(f[snap])

# Declare numpy arrays to hold the data #
PositionComps = np.empty(shape=(nGal, 3))

# Read in the data #
iGal = 0
for iFile in range(firstFile, lastFile + 1):
    # The following line closes the file at the end of the loop
    with h5py.File(outputDir + filePrefix + '%i' % iFile + filePostfix, 'r') as f:
        nGalFile = len(f[snap])
        PositionComps[iGal:iGal + nGalFile] = f[snap]['Pos']
        iGal += nGalFile

# Physical units #
hubble = 0.678
VelocityUnits = 1  # [Km/s]
LengthUnits = 1e3 / hubble  # [Kpc]
MassUnits = 1e10 / hubble  # [Msun]
SpinUnits = 1e3 / hubble  # [Km/s * Kpc]

dBulgeMass = 0.3

# Data #
## Generate initial figure.
plt.close()
fig = plt.figure(1, figsize=(18, 10))
ax = fig.add_subplot(111, projection='3d')

## 3D plotting.
PositionComps = zip(*PositionComps)
x = PositionComps[0]
y = PositionComps[1]
z = PositionComps[2]

# ax.view_init(elev=15, azim=40)
ax.set_xlabel('X Component')
ax.set_ylabel('Y Component')
ax.set_zlabel('Z Component')
ax.text2D(0.05, 0.95, "Position Vector", transform=ax.transAxes)

ax.set_xlim([-10, 600])
ax.set_ylim([-10, 600])
ax.set_zlim([-10, 600])

ax.scatter(x, y, z, c='r', marker='o')

## Plane Projection.
# ax.plot(x, z, 'r+', zdir='y', zs=1500)
# ax.plot(y, z, 'g+', zdir='x', zs=-800)
# ax.plot(x, y, 'k+', zdir='z', zs=-800)

plt.savefig('Pos-' + date_string + '.png')

