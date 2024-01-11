# Determine the size and declare arrays to hold the data #
nGal = 0
for iFile in range(firstFile, lastFile + 1):
    # The following line closes the file at the end of the loop
    with h5py.File(outputDir + filePrefix + '%i' % iFile + filePostfix, 'r') as f:
        nGal += len(f[snap])

SFR = np.empty(nGal)
SHLR = np.empty(nGal)
StellarMass = np.empty(nGal)

# Read in the data #
iGal = 0
for iFile in range(firstFile, lastFile + 1):
    # The following line closes the file at the end of the loop
    with h5py.File(outputDir + filePrefix + '%i' % iFile + filePostfix, 'r') as f:
        nGalFile = len(f[snap])
        SFR[iGal:iGal + nGalFile] = f[snap]['Sfr']
        StellarMass[iGal:iGal + nGalFile] = f[snap]['StellarMass']
        SHLR[iGal:iGal + nGalFile] = f[snap]['StellarHalfLightRadius']
        iGal += nGalFile

# Trim the data #
if (snap == '30'):
    index = np.where(SFR / StellarMass > 2.0)
if (snap == '25'):
    index = np.where(SFR / StellarMass > 3.5)
if (snap == '22'):
    index = np.where(SFR / StellarMass > 0.8)

S_F_R = SFR[index]
S_H_L_R = SHLR[index] * LengthUnits
Stellar_Mass = StellarMass[index] * MassUnits

dStellarMass = 0.3

########################################################################################################################

# Generate initial figure #
plt.close()
plt.figure(0, figsize=(8, 6))

# Scatter plot parameters #
plt.xscale('log')
plt.yscale('log')
plt.xlim(1e9, 1e12)
plt.ylim(1e-2, 1e2)
plt.ylabel(r'$\mathrm{SFR/M_{\odot}yr^{-1}}$')
plt.xlabel(r'$\mathrm{M_{\bigstar}/M_{\odot}}$')
plt.tick_params(direction='in', which='both', top='on', right='on')

# Plot L-galaxies data #
if (snap == '30'):
    plt.scatter(Stellar_Mass, S_F_R, c='k', s=10, label="$\mathrm{sSFR > 1.5\, [yr^{-1}]}$")
if (snap == '25'):
    plt.scatter(Stellar_Mass, S_F_R, c='k', s=10, label="$\mathrm{sSFR > 3.5\, [yr^{-1}]}$")
if (snap == '22'):
    plt.scatter(Stellar_Mass, S_F_R, c='k', s=10, label="$\mathrm{sSFR > 0.8\, [yr^{-1}]}$")

# Plot observational data #
if (snap == '30'):
    OSK17_SFR2 = np.genfromtxt('OSK17_SFR2.csv', delimiter=',', names=['x', 'y'])
    plt.plot(np.power(10, OSK17_SFR2['x']), np.power(10, OSK17_SFR2['y']), color='m', linestyle='dashed', lw=3,
             label="Okamura+17")
if (snap == '25'):
    OSK17_SFR3 = np.genfromtxt('OSK17_SFR3.csv', delimiter=',', names=['x', 'y'])
    plt.plot(np.power(10, OSK17_SFR3['x']), np.power(10, OSK17_SFR3['y']), color='b', linestyle='dashed', lw=3,
             label="Okamura+17")
if (snap == '22'):
    OSK17_SFR4 = np.genfromtxt('OSK17_SFR4.csv', delimiter=',', names=['x', 'y'])
    plt.plot(np.power(10, OSK17_SFR4['x']), np.power(10, OSK17_SFR4['y']), color='r', linestyle='dashed', lw=3,
             label="Okamura+17")

plt.legend(ncol=1, loc=4)
plt.annotate("$\mathrm{z \sim }$" + z, xy=(0.1, 0.9), xycoords='axes fraction', fontsize=20)
plt.savefig('StellarMass_Vs_SFR-' + snap + date + '.png')

########################################################################################################################

# Generate initial figure #
plt.close()
plt.figure(0, figsize=(8, 6))

# Scatter plot parameters #
plt.xscale('log')
plt.yscale('log')
plt.xlim(1e9, 1e12)
plt.ylim(1e-2, 1e2)
plt.ylabel(r'$\mathrm{R_{HL}/Kpc}$')
plt.xlabel(r'$\mathrm{M_{\bigstar}/M_{\odot}}$')
plt.tick_params(direction='in', which='both', top='on', right='on')

# Plot L-galaxies data #
if (snap == '30'):
    plt.scatter(Stellar_Mass, S_H_L_R, c='k', s=10, label="$\mathrm{sSFR > 1.5\, [yr^{-1}]}$")
if (snap == '25'):
    plt.scatter(Stellar_Mass, S_H_L_R, c='k', s=10, label="$\mathrm{sSFR > 3.5\, [yr^{-1}]}$")
if (snap == '22'):
    plt.scatter(Stellar_Mass, S_H_L_R, c='k', s=10, label="$\mathrm{sSFR > 0.8\, [yr^{-1}]}$")

if (snap == '30'):
    OSK17_MS2 = np.genfromtxt('OSK17_MS2.csv', delimiter=',', names=['x', 'y'])
    plt.plot(np.power(10, OSK17_MS2['x']), OSK17_MS2['y'], color='m', linestyle='dashed', lw=3, label="Okamura+17")
if (snap == '25'):
    OSK17_MS3 = np.genfromtxt('OSK17_MS3.csv', delimiter=',', names=['x', 'y'])
    plt.plot(np.power(10, OSK17_MS3['x']), OSK17_MS3['y'], color='b', linestyle='dashed', lw=3, label="Okamura+17")
if (snap == '22'):
    OSK17_MS4 = np.genfromtxt('OSK17_MS4.csv', delimiter=',', names=['x', 'y'])
    plt.plot(np.power(10, OSK17_MS4['x']), OSK17_MS4['y'], color='r', linestyle='dashed', lw=3, label="Okamura+17")

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
        median[i] = np.median(S_H_L_R[index])
        slow[i] = np.percentile(S_H_L_R[index], 15.87)
        shigh[i] = np.percentile(S_H_L_R[index], 84.13)
    logMassLow += dStellarMass

# Plot median and 1-sigma lines #
plt.plot(mass, median, 'r-', lw=3, label="$\mathrm{Median}$")
plt.fill_between(mass, shigh, slow, color='red', alpha='0.5')

plt.legend(ncol=1, loc=4)
plt.annotate("$\mathrm{z \sim }$" + z, xy=(0.1, 0.9), xycoords='axes fraction', fontsize=20)
plt.savefig('StellarMass_Vs_HalfLightRadius-' + snap + date + '.png')