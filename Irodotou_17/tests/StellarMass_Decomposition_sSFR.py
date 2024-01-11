# Load data arrays #
Sfr = np.load(SavePath + 'Sfr.npy')
PBMass = np.load(SavePath + 'PBMass.npy')
CBMass = np.load(SavePath + 'CBMass.npy')
StellarMass = np.load(SavePath + 'StellarMass.npy')

# Trim the data #
PB_Mass = PBMass * MassUnits
CB_Mass = CBMass * MassUnits
Stellar_Mass = StellarMass * MassUnits
sS_F_R = np.log10((Sfr / StellarMass) * hubble)

PB_Ratio = np.divide(PB_Mass, Stellar_Mass)
CB_Ratio = np.divide(CB_Mass, Stellar_Mass)

########################################################################################################################

# Generate initial figure #
plt.close()
f, ax = plt.subplots()
f, ((ax2, ax3)) = plt.subplots(2, sharex=True, sharey=True, figsize=(10, 7.5))
f.subplots_adjust(hspace=0, wspace=0)

# Scatter plot parameters #
plt.xscale('log')
plt.xlim(1e9, 5e12)
plt.ylim(-0.05, 1.05)
plt.xlabel(r'$\mathrm{M_{\bigstar} / M_{\odot}}$')
ax2.set_ylabel(r'$\mathrm{M_{pb} / M_{\bigstar}}$')
ax3.set_ylabel(r'$\mathrm{M_{cb} / M_{\bigstar}}$')

ax2.tick_params(direction='in', which='both', top='on', right='on')
ax3.tick_params(direction='in', which='both', top='on', right='on')

# Plot L-Galaxies data - color coded #
p2 = ax2.scatter(Stellar_Mass, PB_Ratio, c=sS_F_R, edgecolor='black', s=10, cmap='RdYlBu')
cbaxes = f.add_axes([0.9, 0.495, 0.022, 0.385])
cbaxes.tick_params(labelsize=10)
cb = plt.colorbar(p2, cax=cbaxes, ticks=[-15, -10, -5, 0])
cb.set_label(r'$\mathrm{log_{10}(\mathrm{sSFR}[yr^{-1}])}$', fontsize=10)

p3 = ax3.scatter(Stellar_Mass, CB_Ratio, c=sS_F_R, edgecolor='black', s=10, cmap='RdYlBu')
cbaxes = f.add_axes([0.9, 0.11, 0.022, 0.385])
cbaxes.tick_params(labelsize=10)
cb = plt.colorbar(p3, cax=cbaxes, ticks=[-15, -10, -5, 0])
cb.set_label(r'$\mathrm{log_{10}(\mathrm{sSFR}[yr^{-1}])}$', fontsize=10)

# Save the figure #
plt.savefig('SM_Decomp_sSFR_58-' + date + '.png')