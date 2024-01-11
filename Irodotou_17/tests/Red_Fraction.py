# Load data arrays #
MagDust = np.load('./L-Galaxies_Data/58/MagDust.npy')
StellarMass = np.load('./L-Galaxies_Data/58/StellarMass.npy')
MagDustHWT15 = np.load('./L-Galaxies_Data/MagDust.npy')
StellarMassHWT15 = np.load('./L-Galaxies_Data/StellarMass.npy')

# Put into observer units and add scatter to stellar mass estimate #
offset = 10 + np.log10(hubble)
log10StellarMass = np.log10(StellarMass) + offset
log10StellarMassHWT15 = np.log10(StellarMassHWT15) + offset
log10StellarMassObs = log10StellarMass + np.random.randn(len(StellarMass)) * 0.08 * (1 + redshift)
log10StellarMassObsHWT15 = log10StellarMassHWT15 + np.random.randn(len(StellarMassHWT15)) * 0.08 * (1 + redshift)

slope_red_fraction = [0.075, 0.275, 0.3, 0.32, 0.38]
offset_red_fraction = [1.85, 1.213, 1.18, 0.99, 0.79]

########################################################################################################################

# Generate initial figure #
plt.close()
f = plt.figure(0, figsize=(10, 7.5))

# Plot parameters #
plt.xlim(7.5, 11.5)
plt.ylim(0.0, 1.2)
plt.ylabel(r'$\mathrm{f_{Red}}$')
plt.xlabel(r'$\mathrm{log_{10}(M_{\bigstar} / M_{\odot} \cdot h^{-2})}$')
plt.tick_params(direction='in', which='both', top='on', right='on')
plt.tick_params(direction='in', which='both', top='on', right='on')

# Read MCMC observational data #
data = np.loadtxt("./Obs_Data/RedFraction_z0.00.txt")
obs_xbin = data[:, 0] + (data[:, 1] - data[:, 0]) / 2.
xRF = (data[:, 0] + data[:, 1]) / 2.

# Plot MCMC observational data #
# plt.errorbar(obs_xbin, data[:, 2], data[:, 3], c='b', marker='o', linestyle="None", elinewidth=2, capsize=8,
# capthick=2, zorder=3, label="Observations (MCMC)")

plt.errorbar(xRF + np.log10(0.673) + np.log10(0.673), data[:, 2], yerr=data[:, 3], c='b', marker='o', linestyle="None",
             elinewidth=2, capsize=8, capthick=2, zorder=3, label="Observations (MCMC)")

# Setting up to reproduce HWT15's plot
bin = 0.25
xlim = [8.0, 11.5]
ylim = [0., 1.2]
Mass_arr = np.arange(xlim[0], xlim[1], bin)
RedFraction = np.zeros(len(Mass_arr), dtype=np.float32)

# Calculating the RF #
Magr = MagDust[:, 17]
color_ur = MagDust[:, 15] - MagDust[:, 17]

for ll in range(0, len(Mass_arr)):
    index_red = np.where(
            (color_ur > (offset_red_fraction[0] - slope_red_fraction[0] * np.tanh((Magr + 18.07) / 1.09))) & (
                    log10StellarMassObs > Mass_arr[ll] - bin / 2.) & (log10StellarMassObs < Mass_arr[ll] + bin / 2.))
    index_all = np.where(
            (log10StellarMassObs > Mass_arr[ll] - bin / 2.) & (log10StellarMassObs < Mass_arr[ll] + bin / 2.))

    RedFraction[ll] = float(len(index_red[0])) / float(len(index_all[0]))

plt.plot(Mass_arr, RedFraction, '-r', label=r'$\mathrm{This\; work}$')

# Calculating the RF #
Magr = MagDustHWT15[:, 17]
color_ur = MagDustHWT15[:, 15] - MagDustHWT15[:, 17]

for ll in range(0, len(Mass_arr)):
    index_red = np.where(
            (color_ur > (offset_red_fraction[0] - slope_red_fraction[0] * np.tanh((Magr + 18.07) / 1.09))) & (
                    log10StellarMassObsHWT15 > Mass_arr[ll] - bin / 2.) & (
                    log10StellarMassObsHWT15 < Mass_arr[ll] + bin / 2.))
    index_all = np.where(
            (log10StellarMassObsHWT15 > Mass_arr[ll] - bin / 2.) & (log10StellarMassObsHWT15 < Mass_arr[ll] + bin / 2.))

    RedFraction[ll] = float(len(index_red[0])) / float(len(index_all[0]))

plt.plot(Mass_arr, RedFraction, '-b', label=r'$\mathrm{Henriques+15}$')

plt.legend(loc='upper left', numpoints=1, fontsize='x-small')

plt.savefig('RF_58-' + date + '.png')