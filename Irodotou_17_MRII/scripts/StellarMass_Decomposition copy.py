# Load data arrays #
PBMass = np.load(SavePath + 'PBMass.npy')
CBMass = np.load(SavePath + 'CBMass.npy')
DiskMass = np.load(SavePath + 'DiskMass.npy')
BulgeMass = np.load(SavePath + 'BulgeMass.npy')
CBMassMajor = np.load(SavePath + 'CBMassMajor.npy')
CBMassMinor = np.load(SavePath + 'CBMassMinor.npy')
StellarMass = np.load(SavePath + 'StellarMass.npy')

# Trim the data #
PB_Mass = PBMass * MassUnits
CB_Mass = CBMass * MassUnits
Disk_Mass = DiskMass * MassUnits
Bulge_Mass = BulgeMass * MassUnits
Stellar_Mass = StellarMass * MassUnits
CB_Mass_Major = CBMassMajor * MassUnits
CB_Mass_Minor = CBMassMinor * MassUnits

PB_Ratio = np.divide(PB_Mass, Stellar_Mass)
CB_Ratio = np.divide(CB_Mass, Stellar_Mass)
Disk_Ratio = np.divide(Disk_Mass, Stellar_Mass)
Bulge_Ratio = np.divide(Bulge_Mass, Stellar_Mass)
CBMa_Ratio = np.divide(CB_Mass_Major, Stellar_Mass)
CBMi_Ratio = np.divide(CB_Mass_Minor, Stellar_Mass)

dlog10 = 0.15

########################################################################################################################

# Generate initial figure #
plt.close()
figure, ax = plt.subplots()
figure, ((ax1, ax2, ax3, ax4), (ax5, ax6, ax7, ax8), (ax9, ax10, ax11, ax12), (ax13, ax14, ax15, ax16),
    (ax17, ax18, ax19, ax20)) = plt.subplots(nrows=5, ncols=4, figsize=(20, 15))
figure.subplots_adjust(hspace=0, wspace=0)

# 2D histogram plot parameters #
ax1.set_xscale('log')
ax2.set_xscale('log')
ax6.set_xscale('log')
ax7.set_xscale('log')
ax9.set_xscale('log')
ax10.set_xscale('log')
ax11.set_xscale('log')
ax12.set_xscale('log')
ax14.set_xscale('log')
ax15.set_xscale('log')
ax19.set_xscale('log')
ax20.set_xscale('log')

ax1.set_xlim(7e8, 5e12)
ax2.set_xlim(7e8, 5e12)
ax6.set_xlim(7e8, 5e12)
ax7.set_xlim(7e8, 5e12)
ax9.set_xlim(7e8, 5e12)
ax10.set_xlim(7e8, 5e12)
ax11.set_xlim(7e8, 5e12)
ax12.set_xlim(7e8, 5e12)
ax14.set_xlim(7e8, 5e12)
ax15.set_xlim(7e8, 5e12)
ax19.set_xlim(7e8, 5e12)
ax20.set_xlim(7e8, 5e12)

ax1.set_ylim(-0.05, 1.05)
ax2.set_ylim(-0.05, 1.05)
ax6.set_ylim(-0.05, 1.05)
ax7.set_ylim(-0.05, 1.05)
ax9.set_ylim(-0.05, 1.05)
ax10.set_ylim(-0.05, 1.05)
ax11.set_ylim(-0.05, 1.05)
ax12.set_ylim(-0.05, 1.05)
ax14.set_ylim(-0.05, 1.05)
ax15.set_ylim(-0.05, 1.05)
ax19.set_ylim(-0.05, 1.05)
ax20.set_ylim(-0.05, 1.05)

ax1.set_xlabel(r'$\mathrm{M_{\bigstar} / M_{\odot}}$')
ax2.set_xlabel(r'$\mathrm{M_{\bigstar} / M_{\odot}}$')
ax9.set_xlabel(r'$\mathrm{M_{\bigstar} / M_{\odot}}$')
ax14.set_xlabel(r'$\mathrm{M_{\bigstar} / M_{\odot}}$')
ax19.set_xlabel(r'$\mathrm{M_{\bigstar} / M_{\odot}}$')
ax20.set_xlabel(r'$\mathrm{M_{\bigstar} / M_{\odot}}$')

ax1.set_ylabel(r'$\mathrm{M_{d,\bigstar} / M_{\bigstar}}$')
ax2.set_ylabel(r'$\mathrm{M_{d,\bigstar} / M_{\bigstar}}$')
ax6.set_ylabel(r'$\mathrm{M_{pb} / M_{\bigstar}}$')
ax7.set_ylabel(r'$\mathrm{M_{pb} / M_{\bigstar}}$')
ax9.set_ylabel(r'$\mathrm{M_{b} / M_{\bigstar}}$')
ax11.set_ylabel(r'$\mathrm{M_{cb(ma)} / M_{\bigstar}}$')
ax12.set_ylabel(r'$\mathrm{M_{cb(ma)} / M_{\bigstar}}$')
ax14.set_ylabel(r'$\mathrm{M_{cb} / M_{\bigstar}}$')
ax15.set_ylabel(r'$\mathrm{M_{cb} / M_{\bigstar}}$')
ax19.set_ylabel(r'$\mathrm{M_{cb(mi)} / M_{\bigstar}}$')
ax20.set_ylabel(r'$\mathrm{M_{cb(mi)} / M_{\bigstar}}$')

# Remove unwanted subplots #
ax3.axis('off')
ax4.axis('off')
ax5.axis('off')
ax8.axis('off')
ax13.axis('off')
ax16.axis('off')
ax17.axis('off')
ax18.axis('off')

# Remove unwanted ticks/labels from subplots #
ax10.set_yticklabels([])

# Change ticks's position #
ax6.tick_params(which='both', top='on')
ax7.tick_params(which='both', top='on')
ax10.tick_params(which='both', top='on')
ax11.tick_params(which='both', top='on')
ax15.tick_params(which='both', top='on')

# Change labels's position #
ax1.xaxis.set_label_position("top")
ax2.xaxis.set_label_position("top")

ax2.yaxis.set_label_position("right")
ax7.yaxis.set_label_position("right")
ax12.yaxis.set_label_position("right")
ax15.yaxis.set_label_position("right")
ax20.yaxis.set_label_position("right")

# Change ticks's position #
ax1.xaxis.tick_top()
ax2.xaxis.tick_top()

ax2.yaxis.tick_right()
ax7.yaxis.tick_right()
ax12.yaxis.tick_right()
ax15.yaxis.tick_right()
ax20.yaxis.tick_right()

########################################################################################################################

p1 = ax1.hexbin(Stellar_Mass, Disk_Ratio, xscale='log', bins='log', cmap=plt.cm.Blues_r, gridsize=gs, mincnt=1)
p6 = ax6.hexbin(Stellar_Mass, PB_Ratio, xscale='log', bins='log', cmap=plt.cm.Greens_r, gridsize=gs, mincnt=1)
p9 = ax9.hexbin(Stellar_Mass, Bulge_Ratio, xscale='log', bins='log', cmap=plt.cm.Reds_r, gridsize=gs, mincnt=1)
p11 = ax11.hexbin(Stellar_Mass, CBMa_Ratio, xscale='log', bins='log', cmap=plt.cm.cool, gridsize=gs, mincnt=1)
p14 = ax14.hexbin(Stellar_Mass, CB_Ratio, xscale='log', bins='log', cmap=plt.cm.Oranges_r, gridsize=gs, mincnt=1)
p19 = ax19.hexbin(Stellar_Mass, CBMi_Ratio, xscale='log', bins='log', cmap=plt.cm.RdPu_r, gridsize=gs, mincnt=1)

# Adjust the color bars #
cbaxes = figure.add_axes([0.76, 0.726, 0.015, 0.154])
cbaxes.tick_params(labelsize=10)
cb = plt.colorbar(p1, cax=cbaxes)
cbaxes.yaxis.set_ticks_position('left')
cb.set_label(r'$\mathrm{log_{10}(\mathrm{Counts\, per\, hexbin})}$')

cbaxes = figure.add_axes([0.81, 0.726, 0.015, 0.154])
cbaxes.tick_params(labelsize=10)
cb = plt.colorbar(p9, cax=cbaxes)
cbaxes.yaxis.set_ticks_position('left')
cb.set_label(r'$\mathrm{log_{10}(\mathrm{Counts\, per\, hexbin})}$')

cbaxes = figure.add_axes([0.86, 0.726, 0.015, 0.154])
cbaxes.tick_params(labelsize=10)
cb = plt.colorbar(p6, cax=cbaxes)
cbaxes.yaxis.set_ticks_position('left')
cb.set_label(r'$\mathrm{log_{10}(\mathrm{Counts\, per\, hexbin})}$')

cbaxes = figure.add_axes([0.15, 0.11, 0.015, 0.154])
cbaxes.tick_params(labelsize=10)
cb = plt.colorbar(p14, cax=cbaxes)
cbaxes.yaxis.set_ticks_position('left')
cb.set_label(r'$\mathrm{log_{10}(\mathrm{Counts\, per\, hexbin})}$')

cbaxes = figure.add_axes([0.2, 0.11, 0.015, 0.154])
cbaxes.tick_params(labelsize=10)
cb = plt.colorbar(p11, cax=cbaxes)
cbaxes.yaxis.set_ticks_position('left')
cb.set_label(r'$\mathrm{log_{10}(\mathrm{Counts\, per\, hexbin})}$')

cbaxes = figure.add_axes([0.25, 0.11, 0.015, 0.154])
cbaxes.tick_params(labelsize=10)
cb = plt.colorbar(p19, cax=cbaxes)
cbaxes.yaxis.set_ticks_position('left')
cb.set_label(r'$\mathrm{log_{10}(\mathrm{Counts\, per\, hexbin})}$')

# Calculate median and 1-sigma for disks #
log10X = np.log10(Stellar_Mass)
log10XMax = np.log10(max(Stellar_Mass))
log10XMin = np.log10(min(Stellar_Mass))
nbin = int((log10XMax - log10XMin) / dlog10)
X = np.empty(nbin)
median = np.empty(nbin)
slow = np.empty(nbin)
shigh = np.empty(nbin)
log10XLow = log10XMin
for i in range(nbin):
    index = np.where((log10X >= log10XLow) & (log10X < log10XLow + dlog10))[0]
    X[i] = np.mean(Stellar_Mass[index])
    if len(index) > 0:
        median[i] = np.median(Disk_Ratio[index])
        slow[i] = np.percentile(Disk_Ratio[index], 15.87)
        shigh[i] = np.percentile(Disk_Ratio[index], 84.13)
    log10XLow += dlog10

# Plot median and 1-sigma lines for disks #
p2 = ax2.plot(X, median, color='blue', lw=lw)
p2 = ax2.fill_between(X, shigh, slow, color='blue', alpha='0.5')

# Calculate median and 1-sigma for bulges #
log10X = np.log10(Stellar_Mass)
log10XMax = np.log10(max(Stellar_Mass))
log10XMin = np.log10(min(Stellar_Mass))
nbin = int((log10XMax - log10XMin) / dlog10)
X = np.empty(nbin)
median = np.empty(nbin)
slow = np.empty(nbin)
shigh = np.empty(nbin)
log10XLow = log10XMin
for i in range(nbin):
    index = np.where((log10X >= log10XLow) & (log10X < log10XLow + dlog10))[0]
    X[i] = np.mean(Stellar_Mass[index])
    if len(index) > 0:
        median[i] = np.median(Bulge_Ratio[index])
        slow[i] = np.percentile(Bulge_Ratio[index], 15.87)
        shigh[i] = np.percentile(Bulge_Ratio[index], 84.13)
    log10XLow += dlog10

# Plot median and 1-sigma lines for bulges #
p10 = ax10.plot(X, median, color='red', lw=lw)
p10 = ax10.fill_between(X, shigh, slow, color='red', alpha='0.5')

# Calculate median and 1-sigma for pseudo-bulges #
log10X = np.log10(Stellar_Mass)
log10XMax = np.log10(max(Stellar_Mass))
log10XMin = np.log10(min(Stellar_Mass))
nbin = int((log10XMax - log10XMin) / dlog10)
X = np.empty(nbin)
median = np.empty(nbin)
slow = np.empty(nbin)
shigh = np.empty(nbin)
log10XLow = log10XMin
for i in range(nbin):
    index = np.where((log10X >= log10XLow) & (log10X < log10XLow + dlog10))[0]
    X[i] = np.mean(Stellar_Mass[index])
    if len(index) > 0:
        median[i] = np.median(PB_Ratio[index])
        slow[i] = np.percentile(PB_Ratio[index], 15.87)
        shigh[i] = np.percentile(PB_Ratio[index], 84.13)
    log10XLow += dlog10

# Plot median and 1-sigma lines for pseudo-bulges #
p7 = ax7.plot(X, median, color='green', lw=lw)
p7 = ax7.fill_between(X, shigh, slow, color='green', alpha='0.5')

# Calculate median and 1-sigma for classical bulges (Ma) #
log10X = np.log10(Stellar_Mass)
log10XMax = np.log10(max(Stellar_Mass))
log10XMin = np.log10(min(Stellar_Mass))
nbin = int((log10XMax - log10XMin) / dlog10)
X = np.empty(nbin)
median = np.empty(nbin)
slow = np.empty(nbin)
shigh = np.empty(nbin)
log10XLow = log10XMin
for i in range(nbin):
    index = np.where((log10X >= log10XLow) & (log10X < log10XLow + dlog10))[0]
    X[i] = np.mean(Stellar_Mass[index])
    if len(index) > 0:
        median[i] = np.median(CBMa_Ratio[index])
        slow[i] = np.percentile(CBMa_Ratio[index], 15.87)
        shigh[i] = np.percentile(CBMa_Ratio[index], 84.13)
    log10XLow += dlog10

# Plot median and 1-sigma lines for classical bulges (Ma) #
p2 = ax12.plot(X, median, color='cyan', lw=lw)
p12 = ax12.fill_between(X, shigh, slow, color='cyan', alpha='0.5')

# Calculate median and 1-sigma for classical bulges #
log10X = np.log10(Stellar_Mass)
log10XMax = np.log10(max(Stellar_Mass))
log10XMin = np.log10(min(Stellar_Mass))
nbin = int((log10XMax - log10XMin) / dlog10)
X = np.empty(nbin)
median = np.empty(nbin)
slow = np.empty(nbin)
shigh = np.empty(nbin)
log10XLow = log10XMin
for i in range(nbin):
    index = np.where((log10X >= log10XLow) & (log10X < log10XLow + dlog10))[0]
    X[i] = np.mean(Stellar_Mass[index])
    if len(index) > 0:
        median[i] = np.median(CB_Ratio[index])
        slow[i] = np.percentile(CB_Ratio[index], 15.87)
        shigh[i] = np.percentile(CB_Ratio[index], 84.13)
    log10XLow += dlog10

# Plot median and 1-sigma lines for classical bulges #
p15 = ax15.plot(X, median, color='orange', lw=lw)
p15 = ax15.fill_between(X, shigh, slow, color='orange', alpha='0.5')

# Calculate median and 1-sigma for classical bulges (Mi) #
log10X = np.log10(Stellar_Mass)
log10XMax = np.log10(max(Stellar_Mass))
log10XMin = np.log10(min(Stellar_Mass))
nbin = int((log10XMax - log10XMin) / dlog10)
X = np.empty(nbin)
median = np.empty(nbin)
slow = np.empty(nbin)
shigh = np.empty(nbin)
log10XLow = log10XMin
for i in range(nbin):
    index = np.where((log10X >= log10XLow) & (log10X < log10XLow + dlog10))[0]
    X[i] = np.mean(Stellar_Mass[index])
    if len(index) > 0:
        median[i] = np.median(CBMi_Ratio[index])
        slow[i] = np.percentile(CBMi_Ratio[index], 15.87)
        shigh[i] = np.percentile(CBMi_Ratio[index], 84.13)
    log10XLow += dlog10

# Plot median and 1-sigma lines for classical bulges (Mi) #
p20 = ax20.plot(X, median, color='magenta', lw=lw)
p20 = ax20.fill_between(X, shigh, slow, color='magenta', alpha='0.5')

# Create arrows to show how we split each component #
ax9.annotate("", xy=(0.75, 1.5), xycoords='axes fraction', xytext=(-0.2, 0.75), textcoords='axes fraction',
             arrowprops=dict(arrowstyle="-[, widthB=2.5", color='green', connectionstyle="angle"))

ax9.annotate("", xy=(0.75, -0.5), xycoords='axes fraction', xytext=(-0.2, 0.25), textcoords='axes fraction',
             arrowprops=dict(arrowstyle="-[, widthB=2.5", color='orange', connectionstyle="angle"))

ax14.annotate("", xy=(0.75, 1.5), xycoords='axes fraction', xytext=(-0.2, 0.75), textcoords='axes fraction',
              arrowprops=dict(arrowstyle="-[, widthB=2.5", color='black', connectionstyle="angle"))

ax14.annotate("", xy=(0.75, -0.5), xycoords='axes fraction', xytext=(-0.2, 0.25), textcoords='axes fraction',
              arrowprops=dict(arrowstyle="-[, widthB=2.5", color='magenta', connectionstyle="angle"))

ax5.annotate(r'$\mathrm{M_{\bigstar}}$', xy=(-0.25, 1.5), xycoords='axes fraction', xytext=(-0.5, 0.5),
             textcoords='axes fraction',
             arrowprops=dict(arrowstyle="-[, widthB=2.5", color='blue', connectionstyle="angle"))

ax5.annotate("", xy=(-0.25, -0.5), xycoords='axes fraction', xytext=(-0.453, 0.475), textcoords='axes fraction',
             arrowprops=dict(arrowstyle="-[, widthB=2.5", color='red', connectionstyle="angle"))


ax1.annotate(r'$\mathrm{(1,1)}$', xy=(0.83, 0.74), xycoords='axes fraction', size=17)
ax6.annotate(r'$\mathrm{(2,2)}$', xy=(0.83, 0.74), xycoords='axes fraction', size=17)
ax9.annotate(r'$\mathrm{(3,1)}$', xy=(0.83, 0.74), xycoords='axes fraction', size=17)
ax11.annotate(r'$\mathrm{(3,3)}$', xy=(0.83, 0.74), xycoords='axes fraction', size=17)
ax14.annotate(r'$\mathrm{(4,2)}$', xy=(0.83, 0.74), xycoords='axes fraction', size=17)
ax19.annotate(r'$\mathrm{(5,3)}$', xy=(0.83, 0.74), xycoords='axes fraction', size=17)


plt.savefig('SM_Decomp_58-' + date + '.png')