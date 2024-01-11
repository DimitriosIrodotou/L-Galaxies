# Load data arrays #
Mvir = np.load(SavePath + 'Mvir.npy')
SM = np.load(SavePath + 'StellarMass.npy')

MvirH = np.load(SavePath + 'HWT15/' + 'Mvir.npy')
SMH = np.load(SavePath + 'HWT15/' + 'StellarMass.npy')

dlog10 = 0.1

########################################################################################################################

# Generate initial figure #
plt.close()
fig = plt.figure(0, figsize=(10, 7.5))

plt.xscale('log')
plt.yscale('log')
plt.xlim(1e9,1e13)
plt.ylim(1e10,1e16)
plt.xlabel(r'$\mathrm{M_{\bigstar} / M_{\odot}}$')
plt.ylabel(r'$\mathrm{M_{vir} / M_{\odot}}$')
plt.tick_params(direction='in', which='both', top='on', right='on')

# Convert masses to solar units #
SM = SM * MassUnits
Mvir = Mvir * MassUnits
SMH = SMH * MassUnits
MvirH = MvirH * MassUnits

# Calculate median and 1-sigma #
log10X = np.log10(SM)
log10XMax = np.log10(max(SM))
log10XMin = np.log10(min(SM))
nbin = int((log10XMax - log10XMin) / dlog10)
X = np.empty(nbin)
median = np.empty(nbin)
slow = np.empty(nbin)
shigh = np.empty(nbin)
log10XLow = log10XMin
for i in range(nbin):
    index = np.where((log10X >= log10XLow) & (log10X < log10XLow + dlog10))[0]
    X[i] = np.mean(np.absolute(SM)[index])
    if len(index) > 0:
        median[i] = np.nanmedian(Mvir[index])
        slow[i] = np.nanpercentile(Mvir[index], 15.87)
        shigh[i] = np.nanpercentile(Mvir[index], 84.13)
    log10XLow += dlog10

# Plot median and 1-sigma lines #
median, = plt.plot(X, median, color='red', lw=lw, label=r'$\mathrm{This\;work}$')
plt.fill_between(X, shigh, slow, color='red', alpha='0.5')
fill, = plt.fill(np.NaN, np.NaN, color='red', alpha=0.5)

# Calculate median and 1-sigma #
log10X = np.log10(SMH)
log10XMax = np.log10(max(SMH))
log10XMin = np.log10(min(SMH))
nbin = int((log10XMax - log10XMin) / dlog10)
X = np.empty(nbin)
median = np.empty(nbin)
slow = np.empty(nbin)
shigh = np.empty(nbin)
log10XLow = log10XMin
for i in range(nbin):
    index = np.where((log10X >= log10XLow) & (log10X < log10XLow + dlog10))[0]
    X[i] = np.mean(np.absolute(SMH)[index])
    if len(index) > 0:
        median[i] = np.nanmedian(MvirH[index])
        slow[i] = np.nanpercentile(MvirH[index], 15.87)
        shigh[i] = np.nanpercentile(MvirH[index], 84.13)
    log10XLow += dlog10

# Plot median and 1-sigma lines #
median, = plt.plot(X, median, color='green', lw=lw, label=r'$\mathrm{HWT15}$')
plt.fill_between(X, shigh, slow, color='green', alpha='0.5')
fill, = plt.fill(np.NaN, np.NaN, color='green', alpha=0.5)

# Save the figure #
plt.legend(frameon=False, loc=2)
plt.savefig('SM_Vs_MVir-' + date + '-' + snap + '.png')

