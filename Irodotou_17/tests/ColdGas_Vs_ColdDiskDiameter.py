# Load data arrays #
Type = np.load('./L-Galaxies58/Type.npy')
ColdGas = np.load('./L-Galaxies58/ColdGas.npy')
DiskMass = np.load('./L-Galaxies58/DiskMass.npy')
StellarMass = np.load('./L-Galaxies58/StellarMass.npy')
ColdGasRadius = np.load('./L-Galaxies58/ColdGasRadius.npy')

# Trim the data #
index = np.where((DiskMass > 0.7 * StellarMass) & (ColdGas > 0.0) & (Type == 0))

Disk_Mass = DiskMass[index] * MassUnits
Cold_Gas_Mass = ColdGas[index] * MassUnits * 0.54
Cold_Gas_Scale_Length = ColdGasRadius[index] * LengthUnits / 3.
Cold_Gas_Diameter = 2 * ColdGasRadius[index] * LengthUnits

dlog10 = 0.25
P0 = 2.34 * 1.0e-13
G = 6.67408 * 1.0e-11
Msun_conv = 2.0 * 1.0e40
Mpc_conv = 3.086 * 1.0e22

########################################################################################################################

# Generate initial figure #
plt.close()
f = plt.figure(1, figsize=(10, 7.5))

# 2D histogram plot parameters #
plt.xscale('log')
plt.yscale('log')
plt.xlim(1e8, 1e12)
plt.ylim(1e-1, 1e3)
plt.ylabel(r'$\mathrm{D_{d,gas}\; /kpc}$')
plt.xlabel(r'$\mathrm{M_{HI} / M_{\odot}}$')
plt.tick_params(direction='in', which='both', top='on', right='on')

K = (G / (8. * np.pi * P0)) * (np.power(Msun_conv, 2.0) / np.power(Mpc_conv, 4.0))
R_int = K * Cold_Gas_Mass * (Cold_Gas_Mass + 0.4 * Disk_Mass) / np.power(Cold_Gas_Scale_Length, 4.0)
R_cmol = np.power(R_int, 0.8)

Ratio = 1.0 / (3.44 * np.power(R_cmol, -0.506) + 4.82 * np.power(R_cmol, -1.054))
HI = np.log10((0.74 / (1.0 + Ratio)) * Cold_Gas_Mass) * MassUnits

x = [10 ** 6.3505404138315535, 10 ** 11.273580542567885]
y = [10 ** -0.0801687763713077, 10 ** 2.421940928270042]

plt.plot(x, y)

# Calculate median and 1-sigma #
log10X = np.log10(Cold_Gas_Mass)
log10XMax = np.log10(max(Cold_Gas_Mass))
log10XMin = np.log10(min(Cold_Gas_Mass))
nbin = int((log10XMax - log10XMin) / dlog10)
X = np.empty(nbin)
median = np.empty(nbin)
slow = np.empty(nbin)
shigh = np.empty(nbin)
log10XLow = log10XMin
for i in range(nbin):
    index = np.where((log10X >= log10XLow) & (log10X < log10XLow + dlog10))[0]
    X[i] = np.mean(Cold_Gas_Mass[index])
    if len(index) > 0:
        median[i] = np.median(Cold_Gas_Diameter[index])
        slow[i] = np.percentile(Cold_Gas_Diameter[index], 15.87)
        shigh[i] = np.percentile(Cold_Gas_Diameter[index], 84.13)
    log10XLow += dlog10
# Plot median and 1-sigma lines #
median, = plt.plot(X, median, 'r-', lw=3)
plt.fill_between(X, shigh, slow, color='red', alpha='0.5', zorder=2)
fill, = plt.fill(np.NaN, np.NaN, c='red', alpha=0.5)

# Read observational data from WFA14 #
WFA14 = np.genfromtxt('./Data/WFA14.csv', delimiter=',', names=['x', 'y'])

# Plot observational data from WFA14 #
plt.scatter(np.power(10, WFA14['x']), np.power(10, WFA14['y']), c='m', marker='*', s=150, zorder=2,
            label=r'$\mathrm{Wang+14}$')

x2 = [10 ** 1.2, 10 ** 2.2]
y2 = [10 ** 8.879296346, 10 ** 10.82138024]

# Plot observational data from Wang14 #
plt.plot(x2, y2, c='g', linestyle='-.', lw=4, label="$\mathrm{Broeils&Rhee97}$")

plt.legend(loc=2, fancybox='True', shadow='True', fontsize="20")

# Plot 2D histogram #
h = plt.hexbin(Cold_Gas_Mass, Cold_Gas_Diameter, xscale='log', yscale='log', bins='log', cmap="Greys",
               mincnt=3, label="$\mathrm{M_{\star,d} / M_{\star,total}> 0.7}$")

# Adjust the color bar #
cbaxes = f.add_axes([0.9, 0.11, 0.02, 0.77])
cb = plt.colorbar(h, cax=cbaxes)
cb.set_label('$\mathrm{log(Counts)}$', fontsize=20)

plt.savefig('ColdGas_Vs_ColdDiskDiameter-' + snap + date + '.png')