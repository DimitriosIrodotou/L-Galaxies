# Load data arrays #
Type = np.load('./L-Galaxies58/Type.npy')
ColdGas = np.load('./L-Galaxies58/ColdGas.npy')
DiskMass = np.load('./L-Galaxies58/DiskMass.npy')
StellarMass = np.load('./L-Galaxies58/StellarMass.npy')

# Trim the data #
index = np.where((DiskMass > 0.7 * StellarMass) & (ColdGas > 0.0) & (Type == 0))

Cold_Gas_Mass = ColdGas[index] * MassUnits
Stellar_Mass = StellarMass[index] * MassUnits
Ratio = np.divide(Cold_Gas_Mass, Stellar_Mass)

dlog10 = 0.23

########################################################################################################################

# Generate initial figure #
plt.close()
f = plt.figure(1, figsize=(10, 7.5))

# 2D histogram plot parameters #
plt.xscale('log')
plt.yscale('log')
plt.xlim(1e9, 1e12)
plt.ylim(1e-4, 1e2)
plt.xlabel(r'$\mathrm{M_{\bigstar} / M_{\odot}}$')
plt.ylabel(r'$\mathrm{M_{d,gas} / M_{\bigstar}}$')
plt.tick_params(direction='in', which='both', top='on', right='on')

# Calculate median and 1-sigma #
log10X = np.log10(Stellar_Mass)
log10XMax = np.log10(max(Stellar_Mass))
log10XMin = np.log10(min(Stellar_Mass))
nbin = int((log10XMax - log10XMin) / dlog10)
X = np.empty(nbin)
median = np.empty(nbin)
slow = np.empty(nbin)
shigh = np.empty(nbin)
log10XLow = log10XMin
for i in range(nbin):
    index = np.where((log10X >= log10XLow) & (log10X < log10XLow + dlog10))[0]
    X[i] = np.mean(Stellar_Mass[index])
    if len(index) > 0:
        median[i] = np.median(Ratio[index])
        slow[i] = np.percentile(Ratio[index], 15.87)
        shigh[i] = np.percentile(Ratio[index], 84.13)
    log10XLow += dlog10
# Plot median and 1-sigma lines #
median, = plt.plot(X, median, 'r-', lw=3)
plt.fill_between(X, shigh, slow, color='red', alpha='0.5', zorder=2)
fill, = plt.fill(np.NaN, np.NaN, c='red', alpha=0.5)

# Read observational data from WFA14 and CSK10 #
WFA14 = np.genfromtxt('./Data/WFA14Ratio.csv', delimiter=',', names=['x', 'y'])
CSK10 = np.genfromtxt('./Data/CSK10.csv', delimiter=',', names=['x', 'y'])

# Plot observational data from WFA14 and CSK10 #
plt.scatter(np.power(10, WFA14['x']), np.power(10, WFA14['y']), c='b', marker='*', s=150, zorder=2,
            label=r'$\mathrm{Wang+14}$')

plt.plot(np.power(10, CSK10['x'][2:4]), np.power(10, CSK10['y'])[2:4], color='k', lw=3,
         label=r'$\mathrm{Catinella+10}$')
plt.plot(np.power(10, CSK10['x'][0:2]), np.power(10, CSK10['y'][0:2]), color='k', lw=3, linestyle='dashed',
         label=r'$\mathrm{Offset\, by\, +0.6dex}$')

# Create the legends #
colors = ['black', 'grey', 'lightgrey']
squares = collections.RegularPolyCollection(numsides=6, sizes=(20,), facecolors=colors)
legend = plt.legend([squares], [r'$\mathrm{This\; work:M_{d,\bigstar} / M_{\bigstar,total}> 0.7}}$'],
                    scatterpoints=len(colors), scatteryoffsets=[.5], handlelength=len(colors), markerscale=2, loc=2)

plt.gca().add_artist(legend)
plt.legend(loc=4, scatterpoints=3)

# Plot L-Galaxies data - 2D histogram #
h = plt.hexbin(Stellar_Mass, Ratio, xscale='log', yscale='log', bins='log', cmap="Greys", mincnt=3)

# Adjust the color bar #
cbaxes = f.add_axes([0.9, 0.11, 0.02, 0.77])
cb = plt.colorbar(h, cax=cbaxes)
cb.set_label('$\mathrm{log_{10}(Counts\; per\; hexbin)}$')

plt.savefig('MassRatioVsStellarMass-' + snap + date + '.png')