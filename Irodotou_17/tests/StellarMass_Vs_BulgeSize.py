# Load data arrays #
CBMass = np.load(SavePath + 'CBMass.npy')
BulgeMass = np.load(SavePath + 'BulgeMass.npy')
CBMassMinor = np.load(SavePath + 'CBMassMinor.npy')

BulgeSize = np.load(SavePath + 'BulgeSize.npy')

# Trim the data #
indexCBMi = np.where(CBMass > 0.7 * BulgeMass)

CB_Mi_Mass = CBMass[indexCBMi] * MassUnits
Bulge_Size_CBMi = BulgeSize[indexCBMi] * LengthUnits

dlog10 = 0.3

########################################################################################################################

# Generate initial figure #
plt.close()
figure = plt.figure(0, figsize=(10, 7.5))

# Scatter plot parameters #
plt.xscale('log')
plt.yscale('log')
plt.ylim(1e-1, 1e1)
plt.xlim(1e9, 1e12)
plt.ylabel(r'$\mathrm{R_{disk} / kpc}$')
plt.xlabel(r'$\mathrm{M_{cb(mi)} / M_{\odot}}$')
plt.tick_params(direction='in', which='both', top='on', right='on')

# Read observational data from G09 #
G09 = np.genfromtxt('./Obs_Data/G09.txt', delimiter=';', skip_header=1,
                    dtype=[('Type', 'U15'), ('Type2', 'U15'), ('h', 'f8'), ('re', 'f8'), ('BtoT', 'f8'),
                           ('MtoLb', 'f8'), ('MtoLd', 'f8'), ('Mb', 'f8'), ('Md', 'f8')])

# Trim observational data from G09 #
index = np.where((G09['Type'] == 'classical   ') | (G09['Type2'] == 'classical   '))
G09_Stellar_Mass = G09['Mb'][index]

# Plot observational data from G09 #
scatter = plt.scatter(G09_Stellar_Mass, G09['re'][index], c='magenta', edgecolor='black', s=size / 2, zorder=2,
                      label=r'$\mathrm{Gadotti\, 09: CBs}$')

# Calculate median and 1-sigma #
log10X = np.log10(CB_Mi_Mass)
log10XMax = np.log10(max(CB_Mi_Mass))
log10XMin = np.log10(min(CB_Mi_Mass))
nbin = int((log10XMax - log10XMin) / dlog10)
X = np.empty(nbin)
median = np.empty(nbin)
slow = np.empty(nbin)
shigh = np.empty(nbin)
log10XLow = log10XMin
for i in range(nbin):
    index = np.where((log10X >= log10XLow) & (log10X < log10XLow + dlog10))[0]
    X[i] = np.mean(np.absolute(CB_Mi_Mass)[index])
    if len(index) > 0:
        median[i] = np.nanmedian(Bulge_Size_CBMi[index])
        slow[i] = np.nanpercentile(Bulge_Size_CBMi[index], 15.87)
        shigh[i] = np.nanpercentile(Bulge_Size_CBMi[index], 84.13)
    log10XLow += dlog10

# Plot median and 1-sigma lines #
median, = plt.plot(X, median, color='magenta', lw=lw)
plt.fill_between(X, shigh, slow, color='magenta', alpha='0.5')
fill, = plt.fill(np.NaN, np.NaN, color='magenta', alpha=0.5)

# Create the legends #
legend = plt.legend([median, fill], [r'$\mathrm{This\; work: Median - M_{cb(mi)} / M_{b} > 0.7}$',
                                      r'$\mathrm{This\; work:16^{th}-84^{th}\,\%ile}$'], loc=2)

plt.gca().add_artist(legend)
plt.legend(loc=4, scatterpoints=sp)

# Save the figure #
plt.savefig('SM_Vs_SHMR_ETGs_55-' + date + '.png')