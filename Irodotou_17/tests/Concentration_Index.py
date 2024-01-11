# Load data arrays #
DiskMass = np.load(SavePath + 'DiskMass.npy')
BulgeMass = np.load(SavePath + 'BulgeMass.npy')
StellarMass = np.load(SavePath + 'StellarMass.npy')
Fifty = np.load(SavePath + 'StellarHalfLightRadius.npy')
Ninety = np.load(SavePath + 'StellarNinetyLightRadius.npy')

# Trim the data #
indexLTGs = np.where(DiskMass > 0.7 * StellarMass)
indexETGs = np.where(BulgeMass > 0.7 * StellarMass)
indexInts = np.where((BulgeMass > 0.3 * StellarMass) & (BulgeMass < 0.7 * StellarMass))

concentrationETGs = np.divide(Ninety[indexETGs], Fifty[indexETGs])
concentrationETGs = concentrationETGs[np.where((concentrationETGs <= 4) & (concentrationETGs > 1.0))]
concentrationLTGs = np.divide(Ninety[indexLTGs], Fifty[indexLTGs])
concentrationLTGs = concentrationLTGs[np.where((concentrationLTGs <= 4) & (concentrationLTGs > 1.0))]
concentrationInts = np.divide(Ninety[indexInts], Fifty[indexInts])
concentrationInts = concentrationInts[np.where((concentrationInts <= 4) & (concentrationInts > 1.0))]

########################################################################################################################

# Generate initial figure #
plt.close()
plt.figure(0, figsize=(10, 7.5))

# Hist plot parameters #
plt.xlim(2, 4)
plt.ylim(0, 1.0)
plt.ylabel(r'$\mathrm{Fraction}$')
plt.xlabel(r'$\mathrm{R_{90}/R_{50}}$')
plt.xticks(np.arange(2, 4.1, 0.1))

########################################################################################################################

# Plot L-Galaxies data - histogram #
Elwei = np.full((1, len(concentrationETGs)), np.divide(1., len(concentrationETGs)))
LTGswei = np.full((1, len(concentrationLTGs)), np.divide(1., len(concentrationLTGs)))
LIntswei = np.full((1, len(concentrationInts)), np.divide(1., len(concentrationInts)))

plt.hist(concentrationETGs, label=r'$\mathrm{M_{b}/M_{\bigstar} > 0.7}$', weights=Elwei[0], bins=30, histtype='step',
         color='red', lw=lw)
plt.hist(concentrationInts, label=r'$\mathrm{0.3 < M_{b}/M_{\bigstar} < 0.7}$', weights=LIntswei[0], bins=30,
         histtype='step', color='green', lw=lw)
plt.hist(concentrationLTGs, label=r'$\mathrm{M_{b}/M_{\bigstar} < 0.3}$', weights=LTGswei[0], bins=30, histtype='step',
         color='blue', lw=lw)

# Create the legend #
plt.legend(ncol=1, loc=1)

# Save the figure #
plt.savefig('Con_Index_58-' + date + '.png')