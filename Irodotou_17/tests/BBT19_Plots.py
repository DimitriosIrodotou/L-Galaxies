# Load data arrays #
BM = np.load(SavePath + 'BulgeMass.npy')
DM = np.load(SavePath + 'DiskMass.npy')
SM = np.load(SavePath + 'StellarMass.npy')
Type = np.load(SavePath + 'Type.npy')
SFR = np.load(SavePath + 'Sfr.npy')

DiskMassHWT15 = np.load(SavePath + 'HWT15/' + 'DiskMass.npy')
BulgeMassHWT15 = np.load(SavePath + 'HWT15/' + 'BulgeMass.npy')
StellarMassHWT15 = np.load(SavePath + 'HWT15/' + 'StellarMass.npy')

########################################################################################################################
# # Generate initial figure #
# plt.close()
# fig = plt.figure(0, figsize=(10, 7.5))
#
# plt.ylim(0.0, 0.6)
# plt.ylabel(r'$\mathrm{f(B/T)_{\star}}$')
# plt.xlabel(r'$\mathrm{(B/T)_{\star}}$')
#
# # Convert masses to solar units #
# MassUnits = 1e10 / hubble
# BM = BM * MassUnits
# SM = SM * MassUnits
#
# # Find galaxies with masses > 10^10 Msun #
# index = np.where(SM > 1e10)
#
# # Calculate the B/T ratio #
# Ratio = np.divide(BM[index], SM[index])
#
# # Plots BBT19 bar's midpoints #
# BBT19 = np.genfromtxt('./Obs_Data/BBT19.csv', delimiter=',', names=['BT', 'f'])
# plt.scatter(BBT19['BT'], BBT19['f'], color='red', s=size, marker='_', zorder=2, label="$\mathrm{Bluck+19}$")
#
# # Weight each bin by the total number of values and make a histogram #
# Weights = np.divide(np.ones_like(Ratio), float(len(Ratio)))
# plt.hist(Ratio, weights=Weights, edgecolor='black', bins=20)  # 20 = len(np.arange(0.0, 1.05, 0.05))
#
# # Save the figure #
# plt.legend(frameon=False, loc=2)
# plt.savefig('XYZ1-' + date + '-' + snap + '.png')

########################################################################################################################

# Generate initial figure #
plt.close()
fig = plt.figure(0, figsize=(10, 7.5))

plt.ylim(0.0, 1.0)
plt.ylabel(r'$\mathrm{f(B/T>0.5)}$')
plt.xlabel(r'$\mathrm{M_{\bigstar} / M_{\odot}}$')

# Convert masses to solar units #
index = np.where((np.divide(SFR,SM) < 1e-2) & (Type != 0))

offset = 10 - np.log10(hubble)

log10Bulge = np.log10(BM[index]) + offset
log10StellarMass = np.log10(SM[index]) + offset
log10StellarMassObs = log10StellarMass + np.random.randn(len(SM[index])) * 0.08 * (1 + redshift)

log10BulgeHWT15 = np.log10(BulgeMassHWT15) + offset
log10StellarMassHWT15 = np.log10(StellarMassHWT15) + offset
log10StellarMassObsHWT15 = log10StellarMassHWT15 + np.random.randn(len(StellarMassHWT15)) * 0.08 * (1 + redshift)

# Divisions between bulge classes #
logRatio1 = -0.301
logRatio2 = -0.301

# Bins for histogram and plotting #
binwidth = 0.25
xrange = np.array([8.8, 11.8])
bins = np.arange(xrange[0], xrange[1] + 0.001, binwidth)

# Put galaxies into bins #
indBin = np.digitize(log10StellarMassObs, bins)
nBin = len(bins) - 1
x = np.empty(nBin)
yBulge = np.empty(nBin)

# Loop over bins, counting fractions in each class #
for iBin in range(nBin):
    x[iBin] = 0.5 * (bins[iBin] + bins[iBin + 1])
    indThisBin = np.where(indBin == iBin + 1)[0]
    allBin = len(indThisBin)

    # Bulges
    yBulge[iBin] = len(np.where((log10Bulge[indThisBin] - log10StellarMass[indThisBin]) > logRatio1)[0]) / float(allBin)

# Plot L-Galaxies data #
plt.plot(x, yBulge, color='red', lw=2)

# Put HWT15 galaxies into bins #
indBin = np.digitize(log10StellarMassObsHWT15, bins)
nBin = len(bins) - 1
x = np.empty(nBin)
yBulge = np.empty(nBin)

# Loop over bins, counting fractions in each class #
for iBin in range(nBin):
    x[iBin] = 0.5 * (bins[iBin] + bins[iBin + 1])
    indThisBin = np.where(indBin == iBin + 1)[0]
    allBin = len(indThisBin)

    # Bulges
    yBulge[iBin] = len(
            np.where((log10BulgeHWT15[indThisBin] - log10StellarMassHWT15[indThisBin]) > logRatio1)[0]) / float(allBin)

# Plot L-Galaxies data #
# plt.plot(x, yBulge, color='red', lw=2, linestyle='dotted')

# Add text annotation #
plt.annotate(r'$\mathrm{sSFR < 1e-2/Gyr}$', xy=(0.01, 0.5), xycoords='axes fraction', color='red', size=15)
plt.annotate(r'$\mathrm{Type != 0}$', xy=(0.01, 0.8), xycoords='axes fraction', color='red', size=15)

# Save the figure #
plt.savefig('Fig8-' + date + '-' + snap + '.png')