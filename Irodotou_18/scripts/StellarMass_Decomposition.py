# Load data arrays #
# PBMass = np.load(SavePath + 'PBMass.npy')
# CBMass = np.load(SavePath + 'CBMass.npy')
DiskMass = np.load(SavePath + 'DiskMass.npy')
BulgeMass = np.load(SavePath + 'BulgeMass.npy')
# CBMassMajor = np.load(SavePath + 'CBMassMajor.npy')
# CBMassMinor = np.load(SavePath + 'CBMassMinor.npy')
StellarMass = np.load(SavePath + 'StellarMass.npy')

# Trim the data #
# PB_Mass = PBMass * MassUnits
# CB_Mass = CBMass * MassUnits
Disk_Mass = DiskMass * MassUnits
Bulge_Mass = BulgeMass * MassUnits
Stellar_Mass = StellarMass * MassUnits
# CB_Mass_Major = CBMassMajor * MassUnits
# CB_Mass_Minor = CBMassMinor * MassUnits

# PB_Ratio = np.divide(PB_Mass, Stellar_Mass)
# CB_Ratio = np.divide(CB_Mass, Stellar_Mass)
Disk_Ratio = np.divide(Disk_Mass, Stellar_Mass)
Bulge_Ratio = np.divide(Bulge_Mass, Stellar_Mass)
# CBMa_Ratio = np.divide(CB_Mass_Major, Stellar_Mass)
# CBMi_Ratio = np.divide(CB_Mass_Minor, Stellar_Mass)

dlog10 = 0.15

########################################################################################################################

# Generate initial figure #
plt.close()
figure, ax = plt.subplots()
figure, ((ax1, ax2, ax3, ax4), (ax5, ax6, ax7, ax8), (ax9, ax10, ax11, ax12)) = plt.subplots(nrows=3, ncols=4,
                                                                                             figsize=(25, 15))
figure.subplots_adjust(hspace=0, wspace=0)

# 2D histogram plot parameters #
ax2.set_xscale('log')
ax4.set_xscale('log')
ax5.set_xscale('log')
ax7.set_xscale('log')
ax10.set_xscale('log')
ax12.set_xscale('log')

ax2.set_xlim(9e8, 5e12)
ax4.set_xlim(9e8, 5e12)
ax5.set_xlim(9e8, 5e12)
ax7.set_xlim(9e8, 5e12)
ax10.set_xlim(9e8, 5e12)
ax12.set_xlim(9e8, 5e12)

ax2.set_ylim(-0.05, 1.05)
ax4.set_ylim(-0.05, 1.05)
ax5.set_ylim(-0.05, 1.05)
ax7.set_ylim(-0.05, 1.05)
ax10.set_ylim(-0.05, 1.05)
ax12.set_ylim(-0.05, 1.05)

ax2.set_xlabel(r'$\mathrm{M_{\bigstar} / M_{\odot}}$')
ax4.set_xlabel(r'$\mathrm{M_{\bigstar} / M_{\odot}}$')
ax5.set_xlabel(r'$\mathrm{M_{\bigstar} / M_{\odot}}$')
ax7.set_xlabel(r'$\mathrm{M_{\bigstar} / M_{\odot}}$')
ax10.set_xlabel(r'$\mathrm{M_{\bigstar} / M_{\odot}}$')
ax12.set_xlabel(r'$\mathrm{M_{\bigstar} / M_{\odot}}$')

ax2.set_ylabel(r'$\mathrm{M_{b} / M_{\bigstar}}$')
ax4.set_ylabel(r'$\mathrm{M_{d,\bigstar} / M_{\bigstar}}$')
ax5.set_ylabel(r'$\mathrm{M_{pb} / M_{\bigstar}}$')
ax7.set_ylabel(r'$\mathrm{M_{cb} / M_{\bigstar}}$')
ax10.set_ylabel(r'$\mathrm{M_{cb(mi)} / M_{\bigstar}}$')
ax12.set_ylabel(r'$\mathrm{M_{cb(ma)} / M_{\bigstar}}$')

# Remove unwanted subplots #
ax1.axis('off')
ax3.axis('off')
ax6.axis('off')
ax8.axis('off')
ax9.axis('off')
ax11.axis('off')

# Change ticks's position #
ax2.tick_params(direction='in', which='both', top='on', right='on')
ax4.tick_params(direction='in', which='both', top='on', right='on')
ax5.tick_params(direction='in', which='both', top='on', right='on')
ax7.tick_params(direction='in', which='both', top='on', right='on')
ax10.tick_params(direction='in', which='both', top='on', right='on')
ax12.tick_params(direction='in', which='both', top='on', right='on')

########################################################################################################################

p2 = ax2.hexbin(Stellar_Mass, Bulge_Ratio, xscale='log', bins='log', cmap=plt.cm.Reds_r, gridsize=gs, mincnt=1)
p4 = ax4.hexbin(Stellar_Mass, Disk_Ratio, xscale='log', bins='log', cmap=plt.cm.Blues_r, gridsize=gs, mincnt=1)
# p5 = ax5.hexbin(Stellar_Mass, PB_Ratio, xscale='log', bins='log', cmap=plt.cm.Greens_r, gridsize=gs, mincnt=1)
# p7 = ax7.hexbin(Stellar_Mass, CB_Ratio, xscale='log', bins='log', cmap=plt.cm.Oranges_r, gridsize=gs, mincnt=1)
# p10 = ax10.hexbin(Stellar_Mass, CBMi_Ratio, xscale='log', bins='log', cmap=plt.cm.RdPu_r, gridsize=gs, mincnt=1)
# p12 = ax12.hexbin(Stellar_Mass, CBMa_Ratio, xscale='log', bins='log', cmap=plt.cm.cool, gridsize=gs, mincnt=1)

# Adjust the color bars #
cbaxes = figure.add_axes([0.5125, 0.6235, 0.015, 0.2568])
cb = plt.colorbar(p2, cax=cbaxes)
cb.set_label(r'$\mathrm{log_{10}(\mathrm{Counts\, per\, hexbin})}$')

cbaxes = figure.add_axes([0.9, 0.6235, 0.015, 0.2568])
cb = plt.colorbar(p4, cax=cbaxes)
cb.set_label(r'$\mathrm{log_{10}(\mathrm{Counts\, per\, hexbin})}$')

# cbaxes = figure.add_axes([0.319, 0.3665, 0.015, 0.2568])
# cb = plt.colorbar(p5, cax=cbaxes)
# cb.set_label(r'$\mathrm{log_{10}(\mathrm{Counts\, per\, hexbin})}$')
#
# cbaxes = figure.add_axes([0.7065, 0.3665, 0.015, 0.2568])
# cb = plt.colorbar(p7, cax=cbaxes)
# cb.set_label(r'$\mathrm{log_{10}(\mathrm{Counts\, per\, hexbin})}$')
#
# cbaxes = figure.add_axes([0.5125, 0.11, 0.015, 0.2568])
# cb = plt.colorbar(p10, cax=cbaxes)
# cb.set_label(r'$\mathrm{log_{10}(\mathrm{Counts\, per\, hexbin})}$')
#
# cbaxes = figure.add_axes([0.9, 0.11, 0.015, 0.2568])
# cb = plt.colorbar(p12, cax=cbaxes)
# cb.set_label(r'$\mathrm{log_{10}(\mathrm{Counts\, per\, hexbin})}$')

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
ax2.plot(X, median, color='black', lw=lw)
ax2.fill_between(X, shigh, slow, color='black', alpha='0.2')

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
ax4.plot(X, median, color='black', lw=lw)
ax4.fill_between(X, shigh, slow, color='black', alpha='0.2')

# # Calculate median and 1-sigma for pseudo-bulges #
# log10X = np.log10(Stellar_Mass)
# log10XMax = np.log10(max(Stellar_Mass))
# log10XMin = np.log10(min(Stellar_Mass))
# nbin = int((log10XMax - log10XMin) / dlog10)
# X = np.empty(nbin)
# median = np.empty(nbin)
# slow = np.empty(nbin)
# shigh = np.empty(nbin)
# log10XLow = log10XMin
# for i in range(nbin):
#     index = np.where((log10X >= log10XLow) & (log10X < log10XLow + dlog10))[0]
#     X[i] = np.mean(Stellar_Mass[index])
#     if len(index) > 0:
#         median[i] = np.median(PB_Ratio[index])
#         slow[i] = np.percentile(PB_Ratio[index], 15.87)
#         shigh[i] = np.percentile(PB_Ratio[index], 84.13)
#     log10XLow += dlog10
#
# # Plot median and 1-sigma lines for pseudo-bulges #
# ax5.plot(X, median, color='black', lw=lw)
# ax5.fill_between(X, shigh, slow, color='black', alpha='0.2')

# # Calculate median and 1-sigma for classical bulges #
# log10X = np.log10(Stellar_Mass)
# log10XMax = np.log10(max(Stellar_Mass))
# log10XMin = np.log10(min(Stellar_Mass))
# nbin = int((log10XMax - log10XMin) / dlog10)
# X = np.empty(nbin)
# median = np.empty(nbin)
# slow = np.empty(nbin)
# shigh = np.empty(nbin)
# log10XLow = log10XMin
# for i in range(nbin):
#     index = np.where((log10X >= log10XLow) & (log10X < log10XLow + dlog10))[0]
#     X[i] = np.mean(Stellar_Mass[index])
#     if len(index) > 0:
#         median[i] = np.median(CB_Ratio[index])
#         slow[i] = np.percentile(CB_Ratio[index], 15.87)
#         shigh[i] = np.percentile(CB_Ratio[index], 84.13)
#     log10XLow += dlog10
#
# # Plot median and 1-sigma lines for classical bulges #
# ax7.plot(X, median, color='black', lw=lw)
# ax7.fill_between(X, shigh, slow, color='black', alpha='0.2')

# # Calculate median and 1-sigma for classical bulges (Mi) #
# log10X = np.log10(Stellar_Mass)
# log10XMax = np.log10(max(Stellar_Mass))
# log10XMin = np.log10(min(Stellar_Mass))
# nbin = int((log10XMax - log10XMin) / dlog10)
# X = np.empty(nbin)
# median = np.empty(nbin)
# slow = np.empty(nbin)
# shigh = np.empty(nbin)
# log10XLow = log10XMin
# for i in range(nbin):
#     index = np.where((log10X >= log10XLow) & (log10X < log10XLow + dlog10))[0]
#     X[i] = np.mean(Stellar_Mass[index])
#     if len(index) > 0:
#         median[i] = np.median(CBMi_Ratio[index])
#         slow[i] = np.percentile(CBMi_Ratio[index], 15.87)
#         shigh[i] = np.percentile(CBMi_Ratio[index], 84.13)
#     log10XLow += dlog10
#
# # Plot median and 1-sigma lines for classical bulges (Mi) #
# ax10.plot(X, median, color='black', lw=lw)
# ax10.fill_between(X, shigh, slow, color='black', alpha='0.2')
#
# # Calculate median and 1-sigma for classical bulges (Ma) #
# log10X = np.log10(Stellar_Mass)
# log10XMax = np.log10(max(Stellar_Mass))
# log10XMin = np.log10(min(Stellar_Mass))
# nbin = int((log10XMax - log10XMin) / dlog10)
# X = np.empty(nbin)
# median = np.empty(nbin)
# slow = np.empty(nbin)
# shigh = np.empty(nbin)
# log10XLow = log10XMin
# for i in range(nbin):
#     index = np.where((log10X >= log10XLow) & (log10X < log10XLow + dlog10))[0]
#     X[i] = np.mean(Stellar_Mass[index])
#     if len(index) > 0:
#         median[i] = np.median(CBMa_Ratio[index])
#         slow[i] = np.percentile(CBMa_Ratio[index], 15.87)
#         shigh[i] = np.percentile(CBMa_Ratio[index], 84.13)
#     log10XLow += dlog10
#
# # Plot median and 1-sigma lines for classical bulges (Ma) #
# ax12.plot(X, median, color='black', lw=lw)
# ax12.fill_between(X, shigh, slow, color='black', alpha='0.2')

# Create arrows to show how we split each component #
ax1.annotate("", xy=(0.5, 0.07), xycoords='axes fraction', xytext=(0.8, 0.5),
             arrowprops=dict(arrowstyle="-", color='black', connectionstyle="arc3,rad=0"))

ax3.annotate(r'$\mathrm{Stars}$', xy=(-0.5, 1.07), xycoords='axes fraction', xytext=(0.427, 1.4),
             textcoords='axes fraction', arrowprops=dict(arrowstyle="-", color='black', connectionstyle="arc3,rad=0"))

ax3.annotate(r'$\mathrm{Stars}$', xy=(1.5, 1.07), xycoords='axes fraction', xytext=(0.427, 1.4),
             textcoords='axes fraction', arrowprops=dict(arrowstyle="-", color='black', connectionstyle="arc3,rad=0"))

ax3.annotate("", xy=(0.6, 0.07), xycoords='axes fraction', xytext=(0.25, 0.5),
             arrowprops=dict(arrowstyle="-", color='black', connectionstyle="arc3,rad=0"))

ax8.annotate("", xy=(0.6, 0.07), xycoords='axes fraction', xytext=(0.25, 0.5),
              arrowprops=dict(arrowstyle="-", color='black', connectionstyle="arc3,rad=0"))

ax6.annotate("", xy=(0.5, 0.07), xycoords='axes fraction', xytext=(0.8, 0.5), textcoords='axes fraction',
             arrowprops=dict(arrowstyle="-", color='black', connectionstyle="arc3,rad=0"))

ax2.annotate(r'$\mathrm{(1,2)}$', xy=(0.83, 0.78), xycoords='axes fraction', size=17)
ax2.annotate(r'$\mathrm{Bulge}$', xy=(0.431, 1.01), xycoords='axes fraction', color='red', size=17)

ax4.annotate(r'$\mathrm{(1,4)}$', xy=(0.83, 0.78), xycoords='axes fraction', size=17)
ax4.annotate(r'$\mathrm{Disk}$', xy=(0.444, 1.01), xycoords='axes fraction', color='blue',size=17)

ax5.annotate(r'$\mathrm{(2,1)}$', xy=(0.83, 0.78), xycoords='axes fraction', size=17)
ax5.annotate(r'$\mathrm{Pseudo}$', xy=(0.417, 1.01), xycoords='axes fraction',color='green', size=17)

ax7.annotate(r'$\mathrm{(2,3)}$', xy=(0.83, 0.78), xycoords='axes fraction', size=17)
ax7.annotate(r'$\mathrm{Classical}$', xy=(0.495, 1.01), xycoords='axes fraction',color='orange', size=17)

ax10.annotate(r'$\mathrm{(3,2)}$', xy=(0.83, 0.78), xycoords='axes fraction', size=17)
ax10.annotate(r'$\mathrm{Minor}$', xy=(0.434, 1.01), xycoords='axes fraction', color='magenta',size=17)

ax12.annotate(r'$\mathrm{(3,4)}$', xy=(0.83, 0.78), xycoords='axes fraction', size=17)
ax12.annotate(r'$\mathrm{Major}$', xy=(0.518, 1.01), xycoords='axes fraction', color='cyan',size=17)

plt.savefig('SM_Decomp_58-' + date + '.png')