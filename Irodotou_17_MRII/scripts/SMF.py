# Load data arrays #
DiskMass = np.load(SavePath + 'DiskMass.npy')
BulgeMass = np.load(SavePath + 'BulgeMass.npy')
StellarMass = np.load(SavePath + 'StellarMass.npy')

DiskMassHen15 = np.load(SavePath + 'Output_All_Off/' + 'DiskMass.npy')
BulgeMassHen15 = np.load(SavePath + 'Output_All_Off/' + 'BulgeMass.npy')
StellarMassHen15 = np.load(SavePath + 'Output_All_Off/' + 'StellarMass.npy')

indexDD = np.where(BulgeMass < 0.01 * StellarMass)
indexBD = np.where(BulgeMass > 0.7 * StellarMass)
indexIrr = np.where((BulgeMass < 0.7 * StellarMass) & (BulgeMass > 0.01 * StellarMass))

indexDDHen15 = np.where(BulgeMassHen15 < 0.01 * StellarMassHen15)
indexBDHen15 = np.where(BulgeMassHen15 > 0.7 * StellarMassHen15)
indexIrrHen15 = np.where((BulgeMassHen15 < 0.7 * StellarMassHen15) & (BulgeMassHen15 > 0.01 * StellarMassHen15))

# Bins for histogram and plotting
firstFile = 0
lastFile = 511
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

# Do the same for the Hen15 data #
# Put into bins and normalise to number per unit volume (Mpc/h) per dex
nobj, bins, junk = plt.hist(np.log10(StellarMassHen15 * 1e10 * hubble), bins=np.int(nbin), range=xrange, log=True)
yHen = nobj * maxFile / ((lastFile - firstFile + 1) * boxside ** 3) * binperdex

# Plot at centre of bins
xHen = 0.5 * (bins[:-1] + bins[1:])

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

# Do the same for the Hen15 data #
# Put into bins and normalise to number per unit volume (Mpc/h) per dex
nobj, bins, junk = plt.hist(np.log10(StellarMassHen15[indexIrrHen15] * 1e10 * hubble), bins=np.int(nbin), range=xrange,
                            log=True)
yIrrHen15 = nobj * maxFile / ((lastFile - firstFile + 1) * boxside ** 3) * binperdex
xIrrHen15 = 0.5 * (bins[:-1] + bins[1:])

nobj, bins, junk = plt.hist(np.log10(StellarMassHen15[indexDDHen15] * 1e10 * hubble), bins=np.int(nbin), range=xrange,
                            log=True)
yDDHen15 = nobj * maxFile / ((lastFile - firstFile + 1) * boxside ** 3) * binperdex
xDDHen15 = 0.5 * (bins[:-1] + bins[1:])

nobj, bins, junk = plt.hist(np.log10(StellarMassHen15[indexBDHen15] * 1e10 * hubble), bins=np.int(nbin), range=xrange,
                            log=True)
yBDHen15 = nobj * maxFile / ((lastFile - firstFile + 1) * boxside ** 3) * binperdex
xBDHen15 = 0.5 * (bins[:-1] + bins[1:])

########################################################################################################################

# Generate initial figure #
plt.close()
figure, ax = plt.subplots()
figure, (ax1, ax2) = plt.subplots(ncols=2, figsize=(20, 7.5))
figure.subplots_adjust(hspace=0, wspace=0)

# Plot parameters #
ax1.set_ylim(-6, 0)
ax2.set_ylim(-6, 0)
ax1.set_xlim(8, 12)
ax2.set_xlim(8.01, 12)

ax1.set_ylabel(r'$\mathrm{log_{10}(N / (dex / (h^{-1}Mpc)^{3})}$')
ax2.set_ylabel(r'$\mathrm{log_{10}(N / (dex / (h^{-1}Mpc)^{3})}$')
ax1.set_xlabel(r'$\mathrm{log_{10}(M_{\bigstar} / h^{-2}M_\odot)}$')
ax2.set_xlabel(r'$\mathrm{log_{10}(M_{\bigstar} / h^{-2}M_\odot)}$')

ax2.yaxis.set_label_position("right")

ax2.yaxis.tick_right()
ax1.tick_params(direction='in', which='both', top='on', right='on')
ax2.tick_params(direction='in', which='both', top='on', left='on')

########################################################################################################################

ax1.plot(x, np.log10(y), color='black', label=r'$\mathrm{This\; work}$')
ax1.plot(xHen, np.log10(yHen), color='black', linestyle='dotted', label=r'$\mathrm{HWT15}$')

# Read MCMC data #
HWT15 = np.genfromtxt('./Obs_Data/Henriques2015a_smf_z0.csv', delimiter=',', names=['x', 'y'])

# Plot MCMC data #
ax1.scatter(HWT15['x'], HWT15['y'], color='black', zorder=4)

# Create the legends #
# Create an object to combine the Hen15 lines in the legend #
class AnyObjectHandler(HandlerBase):
    def create_artists(self, legend, orig_handle, x0, y0, width, height, fontsize, trans):
        l1 = plt.Line2D([x0, y0 + width], [0.5 * height, 0.5 * height], color='black')
        return [l1]


legend1 = ax1.legend([object], [r'$\mathrm{This\; work}$'], handler_map={object: AnyObjectHandler()}, frameon=False,
                     loc=2)


class AnyObjectHandler(HandlerBase):
    def create_artists(self, legend, orig_handle, x0, y0, width, height, fontsize, trans):
        l1 = plt.Line2D([x0, y0 + width], [0.5 * height, 0.5 * height], linestyle='dotted', color='black')
        return [l1]


legend2 = ax1.legend([object], [r'$\mathrm{HWT15}$'], handler_map={object: AnyObjectHandler()}, frameon=False,
                     loc=1)

ax1.add_artist(legend1)
ax1.add_artist(legend2)

########################################################################################################################

# Plot MCMC data #
ax2.scatter(HWT15['x'], HWT15['y'], color='black', zorder=4)

ax2.plot(xBD, np.log10(yBD), color='red')
ax2.plot(xDD, np.log10(yDD), color='blue')
ax2.plot(xIrr, np.log10(yIrr), color='green')

ax2.plot(xDDHen15, np.log10(yDDHen15), color='blue', linestyle='dotted')
ax2.plot(xBDHen15, np.log10(yBDHen15), color='red', linestyle='dotted')
ax2.plot(xIrrHen15, np.log10(yIrrHen15), color='green', linestyle='dotted')


# Create the legends #
# Create an object to combine the Hen15 lines in the legend #
class AnyObjectHandler(HandlerBase):
    def create_artists(self, legend, orig_handle, x0, y0, width, height, fontsize, trans):
        l1 = plt.Line2D([x0, y0 + width], [1.0 * height, 1.0 * height], color='red')
        l2 = plt.Line2D([x0, y0 + width], [0.5 * height, 0.5 * height], color='green')
        l3 = plt.Line2D([x0, y0 + width], [0.0 * height, 0.0 * height], color='blue')
        return [l1, l2, l3]


legend1 = ax2.legend([object], [r'$\mathrm{This\; work}$'], handler_map={object: AnyObjectHandler()}, frameon=False,
                     loc=2)


class AnyObjectHandler(HandlerBase):
    def create_artists(self, legend, orig_handle, x0, y0, width, height, fontsize, trans):
        l1 = plt.Line2D([x0, y0 + width], [1.0 * height, 1.0 * height], linestyle='dotted', color='red')
        l2 = plt.Line2D([x0, y0 + width], [0.5 * height, 0.5 * height], linestyle='dotted', color='green')
        l3 = plt.Line2D([x0, y0 + width], [0.0 * height, 0.0 * height], linestyle='dotted', color='blue')
        return [l1, l2, l3]


legend2 = ax2.legend([object], [r'$\mathrm{HWT15}$'], handler_map={object: AnyObjectHandler()}, frameon=False,
                     loc=1)

ax2.add_artist(legend1)
ax2.add_artist(legend2)

# Add text annotation #
ax2.annotate(r'$\mathrm{0.01 < M_{b} / M_{\bigstar} < 0.7}$', xy=(0.01, 0.45), xycoords='axes fraction', color='green',
             size=15)
ax2.annotate(r'$\mathrm{M_{b} / M_{\bigstar} > 0.7}$', xy=(0.83, 0.4), xycoords='axes fraction', color='red', size=15)
ax2.annotate(r'$\mathrm{M_{b} / M_{\bigstar} < 0.01}$', xy=(0.45, 0.02), xycoords='axes fraction', color='blue',
             size=15)

# Save the figure #
plt.savefig('SMF_58-' + date + '.png')