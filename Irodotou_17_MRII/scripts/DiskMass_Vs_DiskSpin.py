# Load data arrays #
DiskMass = np.load(SavePath + 'DiskMass.npy')
DiskSpin = np.load(SavePath + 'DiskSpin.npy')
StellarMass = np.load(SavePath + 'StellarMass.npy')

# Trim the data #
index = np.where((DiskMass > 0.7 * StellarMass) & (np.linalg.norm(DiskSpin, axis=1) > 0.0))

Disk_Mass = DiskMass[index] * MassUnits
Disk_Spin = np.linalg.norm(DiskSpin[index], axis=1) * SpinUnits

dlog10 = 0.1

########################################################################################################################

# Generate initial figure #
plt.close()
figure = plt.figure(0, figsize=(10, 7.5))

# Scatter plot parameters #
plt.xscale('log')
plt.yscale('log')
plt.ylim(1e1, 1e5)
plt.xlim(1e6, 1e12)
plt.xlabel(r'$\mathrm{M_{d,\bigstar} / M_{\odot}}$')
plt.ylabel(r'$\mathrm{|j_{d,\bigstar}| / (km \cdot s^{-1} \cdot kpc)}$')
plt.tick_params(direction='in', which='both', top='on', right='on')

########################################################################################################################

# Read observational data from FR13 and OG14 #
FR13 = np.genfromtxt('./Obs_Data/FR13.csv', delimiter=',', names=['Md', 'jd'])
x = [10 ** 8.407256236, 10 ** 12.00269017]
y = [10 ** 1.995464853, 10 ** 3.986394558]
OG14 = np.genfromtxt('./Obs_Data/OG14.csv', delimiter=',', names=['Md', 'jd'])

# Plot observational data from FR13 and OG14 #
plt.scatter(np.power(10, FR13['Md']), np.power(10, FR13['jd']), color='blue', s=size, marker='s',
            label=r'$\mathrm{Fall\; &\; Romanowsky\, 13}$', zorder=4)
plt.scatter(np.power(10, OG14['Md']), np.power(10, OG14['jd']), color='green', s=size, marker='^',
            label=r'$\mathrm{Obreschkow\; &\; Glazebrook\, 14}$', zorder=4)

# Calculate median and 1-sigma #
log10X = np.log10(Disk_Mass)
log10XMax = np.log10(max(Disk_Mass))
log10XMin = np.log10(min(Disk_Mass))
nbin = int((log10XMax - log10XMin) / dlog10)
X = np.empty(nbin)
median = np.empty(nbin)
slow = np.empty(nbin)
shigh = np.empty(nbin)
log10XLow = log10XMin
for i in range(nbin):
    index = np.where((log10X >= log10XLow) & (log10X < log10XLow + dlog10))[0]
    X[i] = np.mean(Disk_Mass[index])
    if len(index) > 0:
        median[i] = np.median(Disk_Spin[index])
        slow[i] = np.percentile(Disk_Spin[index], 15.87)
        shigh[i] = np.percentile(Disk_Spin[index], 84.13)
    log10XLow += dlog10
# Plot median and 1-sigma lines #
median, = plt.plot(X, median, color='red', lw=lw)
plt.fill_between(X, shigh, slow, color='red', alpha='0.5', zorder=2)
fill, = plt.fill(np.NaN, np.NaN, color='red', alpha=0.5)

line1, = plt.plot(x, y, color='b', lw=lw, linestyle='dashed',
                  label=r'$\mathrm{j_{\bigstar} \propto M_{\bigstar}^{0.6}}$')

# Create the legends #
legend1 = plt.legend([median, fill],
                     [r'$\mathrm{This\; work: Median}$', r'$\mathrm{This\; work:16^{th}-84^{th}\,\%ile}$'],
                     frameon=False, loc=2)

colors = ['black', 'grey', 'lightgrey']
squares = collections.RegularPolyCollection(numsides=6, sizes=(20,), facecolors=colors)
legend2 = plt.legend([squares], [r'$\mathrm{This\;work:M_{d,\bigstar} / M_{\bigstar}> 0.7}$'],
                     scatterpoints=len(colors), scatteryoffsets=[.5], handlelength=len(colors), markerscale=2,
                     frameon=False, loc=1)

plt.gca().add_artist(legend1)
plt.gca().add_artist(legend2)
plt.legend(frameon=False, ncol=1, loc=4, scatterpoints=sp)

# Plot L-Galaxies data - 2D histogram #
hexbin = plt.hexbin(Disk_Mass, Disk_Spin, xscale='log', yscale='log', bins='log', cmap='Greys', gridsize=gs, mincnt=mc)

# Adjust the color bar #
cbaxes = figure.add_axes([0.9, 0.11, 0.02, 0.77])
cb = plt.colorbar(hexbin, cax=cbaxes)
cb.set_label('$\mathrm{log_{10}(Counts\; per\; hexbin)}$')

# Save the figure #
plt.savefig('DM_Vs_DS_58-' + date + '.png')