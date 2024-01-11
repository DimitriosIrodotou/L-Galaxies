# Load data arrays #
DiskMass = np.load(SavePath + 'DiskMass.npy')
BulgeMass = np.load(SavePath + 'BulgeMass.npy')
StellarMass = np.load(SavePath + 'StellarMass.npy')

indexDD = np.where(BulgeMass < 0.01 * StellarMass)
indexBD = np.where(BulgeMass > 0.7 * StellarMass)
indexIrr = np.where((BulgeMass < 0.7 * StellarMass) & (BulgeMass > 0.01 * StellarMass))

# Bins for histogram and plotting
firstFile = 5
lastFile = 5
maxFile = 512
binperdex = 5
xrange = np.array([7.8, 12.0])
nbin = (xrange[1] - xrange[0]) * binperdex

########################################################################################################################

# Put into bins and normalise to number per unit volume (Mpc/h) per dex
nobj, bins, junk = plt.hist(np.log10(StellarMass * 1e10 * hubble), bins=np.int(nbin), range=xrange, log=True)
y = nobj * maxFile / ((lastFile - firstFile + 1) * boxside ** 3) * binperdex

# Plot at centre of bins
x = 0.5 * (bins[:-1] + bins[1:])

########################################################################################################################

# Put into bins and normalise to number per unit volume (Mpc/h) per dex
nobj, bins, junk = plt.hist(np.log10(StellarMass[indexIrr] * 1e10 * hubble), bins=np.int(nbin), range=xrange, log=True)
yIrr = nobj * maxFile / ((lastFile - firstFile + 1) * boxside ** 3) * binperdex
xIrr = 0.5 * (bins[:-1] + bins[1:])

nobj, bins, junk = plt.hist(np.log10(StellarMass[indexDD] * 1e10 * hubble), bins=np.int(nbin), range=xrange, log=True)
yDD = nobj * maxFile / ((lastFile - firstFile + 1) * boxside ** 3) * binperdex
xDD = 0.5 * (bins[:-1] + bins[1:])

nobj, bins, junk = plt.hist(np.log10(StellarMass[indexBD] * 1e10 * hubble), bins=np.int(nbin), range=xrange, log=True)
yBD = nobj * maxFile / ((lastFile - firstFile + 1) * boxside ** 3) * binperdex
xBD = 0.5 * (bins[:-1] + bins[1:])


########################################################################################################################

# Generate initial figure #
plt.close()
figure = plt.figure(0, figsize=(10, 7.5))

# Plot parameters #
plt.ylim(-6, 0)
plt.xlim(8, 12)

plt.ylabel(r'$\mathrm{log_{10}(N / (dex / (h^{-1}Mpc)^{3})}$')
plt.xlabel(r'$\mathrm{log_{10}(M_{\bigstar} / h^{-2}M_\odot)}$')

plt.tick_params(direction='in', which='both', top='on', right='on')

########################################################################################################################

plt.plot(x, np.log10(y), color='black', label=r'$\mathrm{This\; work}$')

# Read MCMC data #
HWT15 = np.genfromtxt('./Obs_Data/Henriques2015a_smf_z0.csv', delimiter=',', names=['x', 'y'])

# Plot MCMC data #
plt.scatter(HWT15['x'], HWT15['y'], color='black', zorder=4)

# Create the legends #
# Create an object to combine the Hen15 lines in the legend #
class AnyObjectHandler(HandlerBase):
    def create_artists(self, legend, orig_handle, x0, y0, width, height, fontsize, trans):
        l1 = plt.Line2D([x0, y0 + width], [0.5 * height, 0.5 * height], color='black')
        return [l1]


legend1 = plt.legend([object], [r'$\mathrm{This\; work}$'], handler_map={object: AnyObjectHandler()}, frameon=False,
                     loc=2)


class AnyObjectHandler(HandlerBase):
    def create_artists(self, legend, orig_handle, x0, y0, width, height, fontsize, trans):
        l1 = plt.Line2D([x0, y0 + width], [0.5 * height, 0.5 * height], linestyle='dotted', color='black')
        return [l1]


legend2 = plt.legend([object], [r'$\mathrm{HWT15}$'], handler_map={object: AnyObjectHandler()}, frameon=False,
                     loc=1)

# Save the figure #
plt.savefig('SMF_58-' + date + '.png')