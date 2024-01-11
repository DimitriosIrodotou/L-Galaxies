# Trim data #
index1 = np.where((Ninety >= 2.85 * Fifty) & (Ninety < 6 * Fifty))
index2 = np.where((Ninety < 2.85 * Fifty) & (Ninety > Fifty))

Mag1 = list(zip(*Mag[index1]))[2]
Mag2 = list(zip(*Mag[index2]))[2]

S_H_M_R1 = SHMR[index1] * LengthUnits
S_H_M_R2 = SHMR[index2] * LengthUnits

dDiskMag = 0.2

########################################################################################################################

# Generate initial figure #
plt.close()
fig = plt.figure(0, figsize=(10, 7.5))

# Scatter plot parameters #
plt.yscale('log')
plt.xlim(-19.5, -24)
plt.ylim(1e-2, 1e2)
plt.xlabel(r'$\mathrm{M_{r}}$')
plt.ylabel(r'$\mathrm{R_{HM}/Kpc}$')
plt.tick_params(direction='in', which='both', top='on', right='on')

# Plot L-Galaxies data #
plt.scatter(Mag1, S_H_M_R1, marker='o', s=10, c='k', label="$\mathrm{R_{90} / R_{50} >= 2.85}$")

# Plot observational data #
ZY17_Red = np.genfromtxt('./Data/ZY17_Red.csv', delimiter=',', names=['x', 'y'])
plt.scatter(ZY17_Red['x'], ZY17_Red['y'], color='g', marker='^', edgecolor='k', s=50,
            label=r'$\mathrm{Zhang+17(c>=2.85)}$', zorder=4)

ZY17_Red_Top = np.genfromtxt('./Data/ZY17_Red_Top.csv', delimiter=',', names=['x', 'y'])
plt.plot(ZY17_Red_Top['x'], ZY17_Red_Top['y'], color='g', linestyle='dashed', zorder=4)

ZY17_Red_Bottom = np.genfromtxt('./Data/ZY17_Red_Bottom.csv', delimiter=',', names=['x', 'y'])
plt.plot(ZY17_Red_Bottom['x'], ZY17_Red_Bottom['y'], color='g', linestyle='dashed', zorder=4)

# Calculate median and 1-sigma #
AbsDiskMag = np.absolute(Mag1)
AbsDiskMagMax = max(np.absolute(Mag1))
AbsDiskMagMin = min(np.absolute(Mag1))
nbin = int((AbsDiskMagMax - AbsDiskMagMin) / dDiskMag)
mag = np.empty(nbin)
median = np.empty(nbin)
slow = np.empty(nbin)
shigh = np.empty(nbin)
MagLow = AbsDiskMagMin
for i in range(nbin):
    index = np.where((AbsDiskMag >= MagLow) & (AbsDiskMag < MagLow + dDiskMag))[0]
    mag[i] = np.mean(np.absolute(Mag1)[index])
    if len(index) > 0:
        median[i] = np.median(S_H_M_R1[index])
        slow[i] = np.percentile(S_H_M_R1[index], 15.87)
        shigh[i] = np.percentile(S_H_M_R1[index], 84.13)
    MagLow += dDiskMag

# Plot median and 1-sigma line for classical bulges #
plt.plot(-mag, median, 'r-', lw=3, label="$\mathrm{Median}$")
plt.fill_between(-mag, shigh, slow, color='red', alpha='0.5')

# Plot L-galaxies data #
# h = plt.hexbin(Mag1, S_H_M_R1, yscale='log', bins='log', cmap=plt.cm.Greys_r, mincnt=1,
#                label=r'$\mathrm{R_{90} / R_{50} >= 2.85}$')
#
# Adjust the color bar #
# cbaxes = fig.add_axes([0.9, 0.11, 0.02, 0.77])
# cb = plt.colorbar(h, cax=cbaxes)
# cb.set_label('$\mathrm{log(Counts)}$')

plt.legend(ncol=1, loc=4)
plt.savefig('Mag_Vs_HalfMassRadius_ETGs-' + snap + date + '.png')

########################################################################################################################

# Generate initial figure #
plt.close()
fig = plt.figure(0, figsize=(10, 7.5))

# Scatter plot parameters #
plt.yscale('log')
plt.xlim(-19.5, -24)
plt.ylim(1e-2, 1e2)
plt.xlabel(r'$\mathrm{M_{r}}$')
plt.ylabel(r'$\mathrm{R_{HM}/Kpc}$')
plt.tick_params(direction='in', which='both', top='on', right='on')

# Plot L-Galaxies data #
plt.scatter(Mag2, S_H_M_R2, marker='o', s=10, c='k', label="$\mathrm{R_{90} / R_{50} < 2.85}$")

# Plot observational data #
ZY17_Blue = np.genfromtxt('./Data/ZY17_Blue.csv', delimiter=',', names=['x', 'y'])
plt.scatter(ZY17_Blue['x'], ZY17_Blue['y'], color='m', marker='^', edgecolor='k', s=50,
            label=r'$\mathrm{Zhang+17(c<2.85)}$', zorder=4)

ZY17_Blue_Top = np.genfromtxt('./Data/ZY17_Blue_Top.csv', delimiter=',', names=['x', 'y'])
plt.plot(ZY17_Blue_Top['x'], ZY17_Blue_Top['y'], color='m', linestyle='dashed', zorder=4)

ZY17_Blue_Bottom = np.genfromtxt('./Data/ZY17_Blue_Bottom.csv', delimiter=',', names=['x', 'y'])
plt.plot(ZY17_Blue_Bottom['x'], ZY17_Blue_Bottom['y'], color='m', linestyle='dashed', zorder=4)

# Calculate median and 1-sigma #
AbsDiskMag = np.absolute(Mag2)
AbsDiskMagMax = max(np.absolute(Mag2))
AbsDiskMagMin = min(np.absolute(Mag2))
nbin = int((AbsDiskMagMax - AbsDiskMagMin) / dDiskMag)
mag = np.empty(nbin)
median = np.empty(nbin)
slow = np.empty(nbin)
shigh = np.empty(nbin)
MagLow = AbsDiskMagMin
for i in range(nbin):
    index = np.where((AbsDiskMag >= MagLow) & (AbsDiskMag < MagLow + dDiskMag))[0]
    mag[i] = np.mean(np.absolute(Mag2)[index])
    if len(index) > 0:
        median[i] = np.median(S_H_M_R2[index])
        slow[i] = np.percentile(S_H_M_R2[index], 15.87)
        shigh[i] = np.percentile(S_H_M_R2[index], 84.13)
    MagLow += dDiskMag

# Plot median and 1-sigma line for classical bulges #
plt.plot(-mag, median, 'r-', lw=3, label="$\mathrm{Median}$")
plt.fill_between(-mag, shigh, slow, color='red', alpha='0.5')

# Plot 2D histogram #
# h = plt.hexbin(Mag2, S_H_M_R2, yscale='log', bins='log', cmap=plt.cm.Greys_r, mincnt=1,
#                label=r'$\mathrm{R_{90} / R_{50} < 2.85}$')
#
# Adjust the color bar #
# cbaxes = fig.add_axes([0.9, 0.11, 0.02, 0.77])
# cb = plt.colorbar(h, cax=cbaxes)
# cb.set_label('$\mathrm{log(Counts)}$')

plt.legend(ncol=1, loc=4)
plt.savefig('Mag_Vs_HalfMassRadius_LTGs-' + snap + date + '.png')