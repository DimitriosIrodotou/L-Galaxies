# Load data arrays #
Vmax = np.load(SavePath + 'Vmax.npy')
ColdGas = np.load(SavePath + 'ColdGas.npy')
DiskMass = np.load(SavePath + 'DiskMass.npy')
StellarMass = np.load(SavePath + 'StellarMass.npy')

# Trim the data #
index = np.where(ColdGas > StellarMass)

V_max = Vmax[index] * VelocityUnits
Baryons = (ColdGas[index] + StellarMass[index]) * MassUnits

dlog10 = 0.02
########################################################################################################################

# Generate initial figure #
plt.close()
figure, ax = plt.subplots()
figure, (ax1, ax2) = plt.subplots(ncols=2, sharex=True, figsize=(20, 7.5))
figure.subplots_adjust(hspace=0, wspace=0.3)

# 2D histogram plot parameters #
ax1.set_ylim(8.6, 12.1)
ax2.set_ylim(8.6, 12.1)
ax1.set_xlim(1.6, 2.8)
ax2.set_xlim(1.6, 2.8)

ax1.set_xlabel(r'$\mathrm{log_{10}(V_{c} / (km \cdot s^{-1}))}$')
ax2.set_xlabel(r'$\mathrm{log_{10}(V_{c} / (km \cdot s^{-1}))}$')
ax1.set_ylabel(r'$\mathrm{log_{10}((M_{\bigstar} + M_{d,gas}) / M_{\odot})}$')
ax2.set_ylabel(r'$\mathrm{log_{10}((M_{\bigstar} + M_{d,gas}) / M_{\odot})}$')

ax1.tick_params(direction='in', which='both', top='on', right='on')
ax2.tick_params(direction='in', which='both', top='on', right='on')

########################################################################################################################

# Read observational data from McGaugh12 #
McGaugh12 = np.genfromtxt('./Obs_Data/McGaugh12.csv', delimiter=',', names=['x', 's', 'g'])

# Plot observational data from McGaugh12 #
ax1.scatter(np.log10(McGaugh12['x']), np.log10(np.power(10, McGaugh12['s']) + np.power(10, McGaugh12['g'])),
            color='green', s=size, marker='^', label=r'$\mathrm{McGaugh12}$', zorder=2)

# Plot L-Galaxies data - 2D histogram #
h = ax1.hexbin(np.log10(V_max), np.log10(Baryons), bins='log', cmap='Greys', gridsize=gs, mincnt=1)

# Adjust the color bar #
cbaxes = figure.add_axes([0.462, 0.11, 0.01, 0.77])
cb = plt.colorbar(h, cax=cbaxes)
cb.set_label('$\mathrm{log_{10}(Counts\; per\; hexbin)}$')

# Calculate median and 1-sigma #
# log10X = np.log10(V_max)
# log10XMax = np.log10(max(V_max))
# log10XMin = np.log10(min(V_max))
# nbin = int((log10XMax - log10XMin) / dlog10)
# X = np.empty(nbin)
# median = np.empty(nbin)
# slow = np.empty(nbin)
# shigh = np.empty(nbin)
# log10XLow = log10XMin
# for i in range(nbin):
#     index = np.where((log10X >= log10XLow) & (log10X < log10XLow + dlog10))[0]
#     X[i] = np.mean(V_max[index])
#     if len(index) > 0:
#         median[i] = np.median(Baryons[index])
#         slow[i] = np.percentile(Baryons[index], 15.87)
#         shigh[i] = np.percentile(Baryons[index], 84.13)
#     log10XLow += dlog10

# Create a zoomed-up inset plot #
# axins = zoomed_inset_axes(ax1, 1.5, loc=7)
# axins.set_xlim(2., 2.21)
# axins.set_ylim(9.7, 10.7)
# mark_inset(ax1, axins, loc1=2, loc2=4, fc="none", ec="0.1")

# Plot median, 1-sigma, McGaugh12 and L-Galaxies data in the inset #
# median, = axins.plot(np.log10(X), np.log10(median), color='red', lw=lw)
# axins.fill_between(np.log10(X), np.log10(shigh), np.log10(slow), color='red', alpha=0.5, zorder=3)
# fill, = plt.fill(np.NaN, np.NaN, color='red', alpha=0.5)

# axins.hexbin(np.log10(V_max), np.log10(Baryons), bins='log', cmap='Greys', gridsize=gs, mincnt=1)
# axins.scatter(np.log10(McGaugh12['x']), np.log10(np.power(10, McGaugh12['s']) + np.power(10, McGaugh12['g'])),
#               color='green', marker='^', zorder=4)

# Create the legends #
colors = ['black', 'grey', 'lightgrey']
squares = collections.RegularPolyCollection(numsides=6, sizes=(20,), facecolors=colors)
legend1 = ax1.legend([squares], [r'$\mathrm{This\; work:M_{d,gas} > M_{\bigstar}}$'], scatterpoints=len(colors),
                     scatteryoffsets=[.5], handlelength=len(colors), markerscale=2, frameon=False, loc=2)

# legend2 = ax1.legend([median, fill],
#                      [r'$\mathrm{This\; work: Median}$', r'$\mathrm{This\; work:16^{th}-84^{th}\,\%ile}$'], loc=1)

ax1.add_artist(legend1)
# ax1.add_artist(legend2)
ax1.legend(frameon=False, scatterpoints=sp, loc=4)

########################################################################################################################

# Trim the data #
index = np.where(DiskMass > 0.7 * StellarMass)

V_max = Vmax[index] * VelocityUnits
Baryons = (ColdGas[index] + StellarMass[index]) * MassUnits

# Read observational data from AZF08 and HDC12 #
AZF08 = np.genfromtxt('./Obs_Data/AZF08.csv', delimiter=',', names=['x', 'y'])
TEA11 = np.genfromtxt('./Obs_Data/TEA11.csv', delimiter=',', names=['x', 'y'])
AVS18 = np.genfromtxt('./Obs_Data/AVS18.csv', delimiter=',', names=['x', 'y'])

# Plot observational data from AZF08, AVS18 #
ax2.scatter(np.log10(AZF08['x']), AZF08['y'], color='green', s=size, zorder=2, label=r'$\mathrm{Avila-Reese+08}$')
ax2.scatter(np.log10(AVS18['x']), AVS18['y'], color='red', s=size, marker='*', zorder=2,
            label=r'$\mathrm{Aquino-Ortiz+18}$')
ax2.scatter(TEA11['x'], TEA11['y'], color='blue', s=size, marker='s', zorder=2, label=r'$\mathrm{Torres-Flores+11}$')

# Plot L-Galaxies data - 2D histogram #
hexbin = ax2.hexbin(np.log10(V_max), np.log10(Baryons), bins='log', cmap='Greys', gridsize=gs, mincnt=1)
# Adjust the color bar #
cbaxes = figure.add_axes([0.9, 0.11, 0.01, 0.77])
cb = plt.colorbar(hexbin, cax=cbaxes)
cb.set_label('$\mathrm{log_{10}(Counts\; per\; hexbin)}$')

# Create the legends #
colors = ['black', 'grey', 'lightgrey']
squares = collections.RegularPolyCollection(numsides=6, sizes=(20,), facecolors=colors)
legend3 = ax2.legend([squares], [r'$\mathrm{This\; work:M_{d,\bigstar}/M_{\bigstar}>0.7}$'], scatterpoints=len(colors),
                     scatteryoffsets=[.5], handlelength=len(colors), markerscale=2, frameon=False, loc=2)

ax2.add_artist(legend3)
ax2.legend(frameon=False, scatterpoints=sp, loc=4)

# Save the figure #
plt.savefig('TF_58-' + date + '.png')