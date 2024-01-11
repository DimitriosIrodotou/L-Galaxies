# Load data arrays #
PBMass = np.load(SavePath + 'PBMass.npy')
DiskMass = np.load(SavePath + 'DiskMass.npy')
BulgeMass = np.load(SavePath + 'BulgeMass.npy')
StellarMass = np.load(SavePath + 'StellarMass.npy')
SHMR = np.load(SavePath + 'StellarHalfMassRadius.npy')

# Trim the data #
index = np.where((PBMass > 0.5 * BulgeMass) & (DiskMass > 0.5 * StellarMass))

S_H_M_R = SHMR[index] * LengthUnits
Stellar_Mass = StellarMass[index] * MassUnits

dlog10 = 0.3

########################################################################################################################

# Generate initial figure #
plt.close()
plt.figure(0, figsize=(10, 7.5))

# Scatter plot parameters #
plt.xscale('log')
plt.yscale('log')
plt.xlim(7e9, 1e12)
plt.ylim(1e-1, 1e2)
plt.ylabel(r'$\mathrm{R_{HM}/Kpc}$')
plt.xlabel(r'$\mathrm{M_{\bigstar}/M_{\odot}}$')
plt.tick_params(direction='in', which='both', top='on', right='on')

# Read observational data from KCR17FL and KCR17RP #
KCR17FL = np.genfromtxt('./Obs_Data/KCR17FL.csv', delimiter=',', names=['x', 'y'])
KCR17RP = np.genfromtxt('./Obs_Data/KCR17RP.csv', delimiter=',', names=['x', 'y'])

# Plot observational data from KCR17FL and KCR17RP #
plt.scatter(np.power(10, KCR17FL['x']), np.power(10, KCR17FL['y']), color='green', s=s, marker='s', edgecolor='black',
            label="$\mathrm{Kalinova+\,17(FL)}$", zorder=2)
plt.scatter(np.power(10, KCR17RP['x']), np.power(10, KCR17RP['y']), color='blue', s=s, marker='d', edgecolor='black',
            label="$\mathrm{Kalinova+\,17(RP)}$", zorder=2)

# Create the legends #
colors = ['black', 'grey', 'lightgrey']
squares = collections.RegularPolyCollection(numsides=6, sizes=(20,), facecolors=colors)
legend = plt.legend([squares], [r'$\mathrm{This\;work:M_{d,\bigstar} / M_{\bigstar}\; &\; M_{pb} / M_{b} > 0.5}$'],
                    scatterpoints=len(colors), scatteryoffsets=[.5], handlelength=len(colors), markerscale=2, loc=2)

plt.gca().add_artist(legend)
plt.legend(loc=4)

# Plot L-Galaxies data - 2D histogram #
h = plt.hexbin(Stellar_Mass, S_H_M_R, xscale='log', yscale='log', bins='log', cmap='Greys', mincnt=3)

plt.savefig('SM_Vs_SHMR_58-' + date + '.png')