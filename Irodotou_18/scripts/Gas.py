# Load data arrays #
ColdGas = np.load(SavePath + 'ColdGas.npy')
H2Fraction = np.load(SavePath + 'H2Fraction.npy')
StellarMass = np.load(SavePath + 'StellarMass.npy')
ColdGasElements = np.load(SavePath + 'ColdGasElements.npy')

# Generate initial figure #
plt.close()
f, ax = plt.subplots()
f, (ax1, ax2, ax3, ax4) = plt.subplots(ncols=4, sharey=True, figsize=(15, 7.5))
f.subplots_adjust(hspace=0, wspace=0)

# 2D histogram and plot parameters #
ax1.set_xlim(9.2, 12)
ax2.set_xlim(9.2, 12)
ax3.set_xlim(9.2, 12)
ax4.set_xlim(9.2, 12)

plt.ylim(-2, 0.5)

ax1.set_ylabel(r'$\mathrm{log10(M_{gas} / M_{\bigstar})}$')
ax1.set_xlabel(r'$\mathrm{log10(M_{\bigstar} / M_{\odot})}$')
ax1.tick_params(direction='in', which='both', top='on', right='on')
ax2.tick_params(direction='in', which='both', top='on', right='on')

ax1.scatter(np.log10(StellarMass * MassUnits), np.log10(np.divide(ColdGas * MassUnits, StellarMass * MassUnits)))
ax2.scatter(np.log10(StellarMass * MassUnits),
            np.log10(np.divide(list(zip(*ColdGasElements))[0], StellarMass * MassUnits)))
ax3.scatter(np.log10(StellarMass * MassUnits), np.log10(np.divide(H2Fraction * MassUnits, StellarMass * MassUnits)))
ax4.scatter(np.log10(StellarMass * MassUnits),
            np.log10(np.divide(H2Fraction * MassUnits, list(zip(*ColdGasElements))[0])))

plt.savefig('Gas-' + date + '.png')