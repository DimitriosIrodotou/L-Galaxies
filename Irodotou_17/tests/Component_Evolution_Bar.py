# Trim the data #
PB_Mass = PBMass * MassUnits
Disk_Mass = DiskMass * MassUnits
Bulge_Mass = BulgeMass * MassUnits
Stellar_Mass = StellarMass * MassUnits
CB_Mass_Major = CBMassMajor * MassUnits
CB_Mass_Minor = CBMassMinor * MassUnits

########################################################################################################################

# Generate initial figure #
plt.close()
fig = plt.figure(0, figsize=(10, 7.5))
ax = fig.add_subplot(111, projection='3d')

# 3D bar plot parameters #
width = depth = 0.1
ax.set_xlim(0, 3.1)
ax.set_ylim(9, 11.8)
ax.set_zlim(0, 1.05)
ax.set_xlabel(r'$\mathrm{Redshift}$')
ax.set_ylabel(r'$\mathrm{log_{10}(M_{\bigstar}/M_{\odot})}$')
ax.set_zlabel(r'$\mathrm{M_{comp.}/M_{\bigstar}}$')
plt.tick_params(direction='in', which='both', top='on', right='on')

# Split stellar masses into bins and create 3D bars #
y = np.arange(9, 12.20, 0.20)
for i in range(0, len(y) - 1):
    index = np.where((np.log10(Stellar_Mass) > y[i]) & (np.log10(Stellar_Mass) < y[i + 1]))
    ID_Ratio = np.divide(PB_Mass[index], Stellar_Mass[index])
    Disk_Ratio = np.divide(Disk_Mass[index], Stellar_Mass[index])
    MiMD_Ratio = np.divide(CB_Mass_Minor[index], Stellar_Mass[index])
    MaMD_Ratio = np.divide(CB_Mass_Major[index], Stellar_Mass[index])
    ax.bar3d(0, y[i], 0, width, depth, MaMD_Ratio, color='r', zsort='min', shade=True)
    ax.bar3d(1, y[i], 0, width, depth, Disk_Ratio, color='b', zsort='min', shade=True)
    ax.bar3d(2, y[i], 0, width, depth, ID_Ratio, color='g', zsort='min', shade=True)
    ax.bar3d(3, y[i], 0, width, depth, MiMD_Ratio, color='m', zsort='min', shade=True)

# Save the figure #
plt.savefig('StellarMass_Decomposition_3DBars-' + snap + '-' + date + '.png')