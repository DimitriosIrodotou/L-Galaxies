# Import required python libraries #
import time
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.ndimage import zoom


# Declare the plotting style #
sns.set()
sns.set_style('ticks', {'axes.grid': True})
sns.set_context('notebook', font_scale=1.6)
lw = 3  # linewidth
mc = 3  # mincnt
sp = 3  # scatterpoints
ms = 5  # markersize
gs = 150  # gridsize
size = 50  # size

# Physical units and simulation parameters #
redshift = 0.0
hubble = 0.673  # [dimensionless]
obsHubble = 0.70  # [dimensionless]
boxside = 480.28  # [Mpc/h]
VelocityUnits = 1  # [Km/s]
LengthUnits = 1e3 / hubble  # [Kpc]
MassUnits = 1e10 / hubble  # [Msun]
SpinUnits = 1e3 / hubble  # [Km/s * Kpc]

# Start the time #
start_time = time.time()
date = time.strftime("%d\%m\%y\%H%M")

SavePath = './L-Galaxies_Data/55/'

# Load data arrays #
DiskMass = np.load(SavePath + 'DiskMass.npy')
StellarMass = np.load(SavePath + 'StellarMass.npy')
SHMR = np.load(SavePath + 'StellarHalfMassRadius.npy')

# Trim the data #
index = np.where(DiskMass < 0.3 * StellarMass)

S_H_M_R = SHMR[index] * LengthUnits
Stellar_Mass = StellarMass[index] * MassUnits

dlog10 = 0.3

########################################################################################################################

# Generate initial figure #
plt.close()
figure = plt.figure(0, figsize=(10, 7.5))

# 2D histogram and plot parameters #
# plt.xscale('log')
# plt.yscale('log')
#
plt.xlim(8.2, 12)
plt.ylim(-0.5, 1.5)

plt.ylabel(r'$\mathrm{R_{HM} / kpc}$')
plt.xlabel(r'$\mathrm{M_{\bigstar} / M_{\odot}}$')

plt.tick_params(direction='in', which='both', top='on', right='on')

########################################################################################################################

# Plot L-Galaxies data - 2D histogram #
hexbin = plt.hexbin(np.log10(Stellar_Mass), np.log10(S_H_M_R), bins='log',cmap='Greys', mincnt=mc)

xlim = [8.5, 12.5]
ylim = [-1, 2]
bin = [0.1, 0.05]
NGals = len(index[0])
Nbins = [int((xlim[1] - xlim[0]) / bin[0]), int((ylim[1] - ylim[0]) / bin[1])]

H, xedges, yedges = np.histogram2d(np.log10(Stellar_Mass), np.log10(S_H_M_R), bins=Nbins)
extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]
mylevels = np.linspace(1., Nbins[1], Nbins[1]) * NGals / (Nbins[1] ** 2 / 0.7)
H = zoom(H, 20)
plt.contour(H.transpose()[::], origin='lower', cmap='inferno', levels=mylevels, extent=extent)
plt.colorbar(format='%d')



# Save the figure #
plt.savefig('SM_Vs_SHMR_LTGs_55-' + date + '.png')

print("--- %s seconds ---" % (time.time() - start_time))