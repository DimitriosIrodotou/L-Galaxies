# Trim the data #
index = np.where(SFR / StellarMass < 0.02)

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
plt.xlim(4e10, 1e12)
plt.ylabel(r'$\mathrm{R_{HM}/Kpc}$')
plt.xlabel(r'$\mathrm{M_{\bigstar}/M_{\odot}}$')
plt.tick_params(direction='in', which='both', top='on', right='on')

# Plot L-Galaxies data #
plt.scatter(Stellar_Mass, S_H_M_R, c='k', s=10)

# Plot Observational data #
NRE12_15_2 = np.genfromtxt('NRE12_15_2.csv', delimiter=',', names=['x', 'y'])
plt.plot(np.power(10, NRE12_15_2['x'][0:2]), NRE12_15_2['y'][0:2], color='b', linestyle='dashed', lw=3,
         label=r'$\mathrm{Newman+12\, 1-\sigma}$')
plt.plot(np.power(10, NRE12_15_2['x'][2:4]), NRE12_15_2['y'][2:4], color='b', linestyle='solid', lw=3,
         label=r'$\mathrm{Newman+12 (fr.par.\, slope)}$')
plt.plot(np.power(10, NRE12_15_2['x'][4:6]), NRE12_15_2['y'][4:6], color='g', linestyle='dotted', lw=3,
         label=r'$\mathrm{Newman+12 (fixed\, slope)}$')
plt.plot(np.power(10, NRE12_15_2['x'][6:8]), NRE12_15_2['y'][6:8], color='b', linestyle='dashed', lw=3)

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
plt.plot(mass, median, 'r-', lw=3, label=r'$\mathrm{Median}$')
plt.fill_between(mass, shigh, slow, color='red', alpha='0.5')

plt.legend(ncol=1, loc=4)
plt.annotate("$\mathrm{1.5 < z < 2.0}$", xy=(0.1, 0.9), xycoords='axes fraction', fontsize=20)
plt.savefig('SM_Vs_SHMR_Evo1-' + snap + date + '.png')