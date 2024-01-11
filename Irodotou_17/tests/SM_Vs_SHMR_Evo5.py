# Trim the date #
index = np.where(BulgeMass > 0.6 * StellarMass)

S_H_M_R = SHMR[index] * LengthUnits
Stellar_Mass = StellarMass[index] * MassUnits

dStellarMass = 0.3

########################################################################################################################

# Generate initial figure #
plt.close()
plt.figure(0, figsize=(8, 6))

# Scatter plot parameters #
plt.xscale('log')
plt.yscale('log')
plt.ylim(1e-2, 1e2)
plt.xlim(3.2e10, 1e12)
plt.ylabel(r'$\mathrm{R_{HM}/Kpc}$')
plt.xlabel(r'$\mathrm{M_{\bigstar,total}/M_{\odot}}$')
plt.tick_params(direction='in', which='both', top='on', right='on')

# Plot L-Galaxies data #
plt.scatter(Stellar_Mass, S_H_M_R, c='k', s=10, label=r'$\mathrm{B/T > 0.6}$')

# Plot observational data #
HMS12_n_02_05 = np.genfromtxt('HMS12_n_02_05.csv', delimiter=',', names=['x', 'y'])
plt.plot(np.power(10, HMS12_n_02_05['x']), np.power(10, HMS12_n_02_05['y']), color='b',
         linestyle='dashed', label=r'$\mathrm{Huertas-Company+12(n>2.5)}$', zorder=4)

HMS12_BT_02_05 = np.genfromtxt('HMS12_BT_02_05.csv', delimiter=',', names=['x', 'y'])
plt.plot(np.power(10, HMS12_BT_02_05['x']), np.power(10, HMS12_BT_02_05['y']), color='b',
         linestyle='solid', label=r'$\mathrm{Huertas-Company+12(B/T>0.6)}$', zorder=4)

# Calculate median and 1-sigma #
LogBulgeMass = np.log10(Stellar_Mass)
LogBulgeMassMax = np.log10(max(Stellar_Mass))
LogBulgeMassMin = np.log10(min(Stellar_Mass))
nbin = int((LogBulgeMassMax - LogBulgeMassMin) / dStellarMass)
mass = np.empty(nbin)
median = np.empty(nbin)
slow = np.empty(nbin)
shigh = np.empty(nbin)
logMassLow = LogBulgeMassMin
for i in range(nbin):
    index = np.where((LogBulgeMass >= logMassLow) & (LogBulgeMass < logMassLow + dStellarMass))[0]
    mass[i] = np.mean(np.absolute(Stellar_Mass)[index])
    if len(index) > 0:
        median[i] = np.median(S_H_M_R[index])
        slow[i] = np.percentile(S_H_M_R[index], 15.87)
        shigh[i] = np.percentile(S_H_M_R[index], 84.13)
    logMassLow += dStellarMass

# Plot median and 1-sigma lines #
plt.plot(mass, median, 'r-', lw=3, label="$\mathrm{Median}$")
plt.fill_between(mass, shigh, slow, color='red', alpha='0.5')

plt.legend(ncol=2, loc=4)
plt.annotate(r'$\mathrm{0.22 < z < 0.51 }$', xy=(0.1, 0.9), xycoords='axes fraction')
plt.savefig('SM_Vs_SHMR_Evo5-' + snap + date + '.png')