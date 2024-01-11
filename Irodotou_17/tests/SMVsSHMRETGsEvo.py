# Imports #
import h5py
import numpy as np
import matplotlib.pyplot as plt
import time

# date_string = time.strftime("%d\%m\%y\%H%M")

# Read in parameters #
# outputDir = '/Users/Bam/output/'
# snap = '58'
# firstFile = 0
# lastFile = 9

# First determine the size of the arrays that we need to hold the data #
nGal = 0
for iFile in range(firstFile, lastFile + 1):
    # The following line closes the file at the end of the loop
    with h5py.File(outputDir + filePrefix + '%i' % iFile + filePostfix, 'r') as f:
        nGal += len(f[snap])

# Declare numpy arrays to hold the data #
SHMR = np.empty(nGal)
StellarMass = np.empty(nGal)
Ninety = np.empty(nGal)
Fifty = np.empty(nGal)
Sfr = np.empty(nGal)

# Read in the data #
iGal = 0
for iFile in range(firstFile, lastFile + 1):
    # The following line closes the file at the end of the loop
    with h5py.File(outputDir + filePrefix + '%i' % iFile + filePostfix, 'r') as f:
        nGalFile = len(f[snap])
        SHMR[iGal:iGal + nGalFile] = f[snap]['StellarHalfMassRadius']
        StellarMass[iGal:iGal + nGalFile] = f[snap]['StellarMass']
        Sfr[iGal:iGal + nGalFile] = f[snap]['Sfr']
        Ninety[iGal:iGal + nGalFile] = f[snap]['StellarNinetyLightRadius']
        Fifty[iGal:iGal + nGalFile] = f[snap]['StellarHalfLightRadius']
        iGal += nGalFile

# Physical units #
hubble = 0.678
VelocityUnits = 1  # [Km/s]
LengthUnits = 1e3 / hubble  # [Kpc]
MassUnits = 1e10 / hubble  # [Msun]
SpinUnits = 1e3 / hubble  # [Km/s * Kpc]

dBulgeMass = 0.3

# Bulge dominated #
index = np.where(Sfr / StellarMass < 0.02)

# Data #
Stellar_Mass = StellarMass[index] * MassUnits
S_H_M_R = SHMR[index] * LengthUnits

# Generate initial figure #
plt.close()
fig = plt.figure(1, figsize=(18, 10))

# Scatter plot parameters #
plt.xlabel(r'$\mathrm{M_{\star}\; [M_{\odot}]}$', fontsize=30)
plt.ylabel(r'$\mathrm{R_{50}\; [Kpc]}$', fontsize=30)

plt.xscale('log')
plt.yscale('log')

plt.xlim(4e10, 1e12)
plt.ylim(1e-2, 1e2)

plt.xticks(fontsize=20)
plt.yticks(fontsize=20)

plt.grid(True, which="both", c='k')

# Plot data #
plt.scatter(Stellar_Mass, S_H_M_R, c='k', s=40, label="$\mathrm{R_{90} / R_{50} > 2.86}$")

# Observational data #
if (snap == '47' or snap == '43' or snap == '41'):
    plt.title(r'$\mathrm{Stellar\; Mass\; versus\; Stellar\; Half-Mass\; Radius\; for\; ETGs\, (snap =}$' + snap + ')',
              fontsize=30)

    xt = [10 ** 10.6, 10 ** 11.82985782]
    yt = [2.723419256, 14.21254182]
    x1 = [10 ** 10.6, 10 ** 12.1]
    y1 = [1.694367582, 12.78999071]
    x2 = [10 ** 10.61421801, 10 ** 12.092891]
    y2 = [1.754990659, 12.13303543]
    xl = [10 ** 10.6, 10 ** 12.092891]
    yl = [1.054145996, 7.957256521]

    plt.plot(xt, yt, c='b', linestyle='-.', lw=4, label="$\mathrm{Newman+12\, 1-\sigma}$")

    plt.plot(x1, y1, c='b', lw=4, label="$\mathrm{Newman+12 (fr.par.\, slope)}$")
    plt.plot(x2, y2, c='b', lw=4, linestyle='--', label="$\mathrm{Newman+12 (fixed\, slope)}$")

    plt.plot(xl, yl, c='b', lw=4, linestyle='-.')

if (snap == '38' or snap == '36' or snap == '34'):
    plt.title(r'$\mathrm{Stellar\; Mass\; versus\; Stellar\; Half-Mass\; Radius\; for\; ETGs\, (snap =}$' + snap + ')',
              fontsize=30)

    xt = [10 ** 10.607109, 10 ** 12.02890995]
    yt = [1.948948729, 14.46663914]
    x1 = [10 ** 10.607109, 10 ** 12.1]
    y1 = [1.150015712, 9.486157607]
    x2 = [10 ** 10.607109, 10 ** 12.1]
    y2 = [1.191178602, 8.38753708]
    xl = [10 ** 10.6, 10 ** 12.1]
    yl = [0.666761598, 5.499929729]

    plt.plot(xt, yt, c='b', linestyle='-.', lw=4, label="$\mathrm{Newman+12\, 1-\sigma}$")

    plt.plot(x1, y1, c='b', lw=4, label="$\mathrm{Newman+12 (fr.par.\, slope)}$")
    plt.plot(x2, y2, c='b', lw=4, linestyle='--', label="$\mathrm{Newman+12 (fixed\, slope)}$")

    plt.plot(xl, yl, c='b', lw=4, linestyle='-.')

if (snap == '32'):
    plt.title(r'$\mathrm{Stellar\; Mass\; versus\; Stellar\; Half-Mass\; Radius\; for\; ETGs\, (snap =}$' + snap + ')',
              fontsize=30)

    xt = [10 ** 10.6, 10 ** 12.07867299]
    yt = [1.628279237, 13.97684776]
    x1 = [10 ** 10.6, 10 ** 12.1]
    y1 = [0.926465222, 8.237884643]
    x2 = [10 ** 10.592891, 10 ** 12.092891]
    y2 = [0.994126365, 7.029713858]
    xl = [10 ** 10.6, 10 ** 12.1]
    yl = [0.536515749, 4.687226521]

    plt.plot(xt, yt, c='b', linestyle='-.', lw=4, label="$\mathrm{Newman+12\, 1-\sigma}$")

    plt.plot(x1, y1, c='b', lw=4, label="$\mathrm{Newman+12 (fr.par.\, slope)}$")
    plt.plot(x2, y2, c='b', lw=4, linestyle='--', label="$\mathrm{Newman+12 (fixed\, slope)}$")

    plt.plot(xl, yl, c='b', lw=4, linestyle='-.')

    if (snap == '30' or snap == '29' or snap == '28'):
        plt.title(
            r'$\mathrm{Stellar\; Mass\; versus\; Stellar\; Half-Mass\; Radius\; for\; ETGs\, (snap =}$' + snap + ')',
            fontsize=30)

        xt = [10 ** 10.607109, 10 ** 12.02890995]
        yt = [1.948948729, 14.46663914]
        x1 = [10 ** 10.607109, 10 ** 12.1]
        y1 = [1.150015712, 9.486157607]
        x2 = [10 ** 10.607109, 10 ** 12.1]
        y2 = [1.191178602, 8.38753708]
        xl = [10 ** 10.6, 10 ** 12.1]
        yl = [0.666761598, 5.499929729]

        plt.plot(xt, yt, c='b', linestyle='-.', lw=4, label="$\mathrm{Newman+12\, 1-\sigma}$")

        plt.plot(x1, y1, c='b', lw=4, label="$\mathrm{Newman+12 (fr.par.\, slope)}$")
        plt.plot(x2, y2, c='b', lw=4, linestyle='--', label="$\mathrm{Newman+12 (fixed\, slope)}$")

        plt.plot(xl, yl, c='b', lw=4, linestyle='-.')

if (snap == '47'):
    plt.title(r'$\mathrm{Stellar\; Mass\; versus\; Stellar\; Half-Mass\; Radius\; for\; ETGs\, (snap =}$' + snap + ')',
              fontsize=30)

    xt = [10 ** 10.50227101, 10 ** 11.99545799]
    yt = [10 ** 0.742283951, 10 ** 1.49845679]
    x = [10 ** 10.51930356, 10 ** 11.97956094]
    y = [10 ** 0.37191358, 10 ** 0.989197531]
    xl = [10 ** 10.50227101, 10 ** 11.99545799]
    yl = [10 ** -0.060185185, 10 ** 0.703703704]

    plt.plot(xt, yt, c='b', linestyle='--', lw=4, label="$\mathrm{Bernardi+10\, 1-\sigma}$")

    plt.plot(x, y, c='b', lw=4, label="$\mathrm{Bernardi+10}$")
    plt.plot(xl, yl, c='b', lw=4, linestyle='--')

    x1 = [10 ** 10.50227101, 10 ** 11.99432248]
    y1 = [10 ** 0.356481481, 10 ** 1.097222222]
    x2 = [10 ** 11.97615443, 10 ** 10.5011355]
    y2 = [10 ** 0.950617284, 10 ** 0.395061728]

    plt.plot(x1, y1, c='r', lw=4, label="$\mathrm{Huertas-Company+13}$")
    plt.plot(x2, y2, c='r', lw=4, linestyle='--', label="$\mathrm{Huertas-Company+13}$")

if (snap == '43'):
    plt.title(r'$\mathrm{Stellar\; Mass\; versus\; Stellar\; Half-Mass\; Radius\; for\; ETGs\, (snap =}$' + snap + ')',
              fontsize=30)

    xt = [10 ** 10.50328887, 10 ** 11.99929682]
    yt = [10 ** 0.643695015, 10 ** 1.362170088]
    x = [10 ** 10.50526598, 10 ** 11.98942074]
    y = [10 ** 0.240469208, 10 ** 0.900293255]
    xl = [10 ** 10.5018699, 10 ** 12.00002838]
    yl = [10 ** -0.15542522, 10 ** 0.563049853]

    plt.plot(xt, yt, c='b', linestyle='--', lw=4, label="$\mathrm{Bernardi+10}$")
    plt.plot(x, y, c='b', lw=4, label="$\mathrm{Bernardi+10}$")
    plt.plot(xl, yl, c='b', lw=4, linestyle='--', label="$\mathrm{Bernardi+10}$")

    x1 = [10 ** 10.50419386, 10 ** 11.99912339]
    y1 = [10 ** 0.247800587, 10 ** 0.958944282]
    x2 = [10 ** 10.50529121, 10 ** 11.99477186]
    y2 = [10 ** 0.299120235, 10 ** 0.841642229]

    plt.plot(x1, y1, c='r', lw=4, label="$\mathrm{Huertas-Company+13}$")
    plt.plot(x2, y2, c='r', lw=4, linestyle='--', label="$\mathrm{Huertas-Company+13}$")

plt.legend(loc=4, fancybox='True', shadow='True', fontsize=20, markerscale=1)
plt.savefig('StellarMassVsSHMR-' + snap + '.png')
