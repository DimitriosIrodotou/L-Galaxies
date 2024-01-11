# Load data arrays #
DiskRadius = np.load(SavePath + 'DiskRadius.npy')
CBMI = np.load(SavePath + 'CBMassMinor.npy')
CBMA = np.load(SavePath + 'CBMassMajor.npy')
CBM = np.load(SavePath + 'CBMass.npy')
NMI = np.load(SavePath + 'NMinorMergers.npy')
NMA = np.load(SavePath + 'NMajorMergers.npy')
PBM = np.load(SavePath + 'PBMass.npy')
BM = np.load(SavePath + 'BulgeMass.npy')
DM = np.load(SavePath + 'DiskMass.npy')
SM = np.load(SavePath + 'StellarMass.npy')

########################################################################################################################

# Generate initial figure #
plt.close()
fig = plt.figure(0, figsize=(10, 7.5))

# plt.xscale('log')
# plt.yscale('log')
# plt.xlim(0.01, 0.1)
plt.ylim(-0.1, 10)
plt.xlabel(r'$\mathrm{Minor\, merger\,mass}$')
plt.ylabel(r'$\mathrm{NMinor}$')

plt.scatter(CBMI, NMI, s=1)

# Save the figure #
plt.savefig('XYZ-' + date + '.png')

########################################################################################################################

plt.close()
fig = plt.figure(0, figsize=(10, 7.5))

# plt.xscale('log')
# plt.yscale('log')
# plt.xlim(0.01, 0.1)
plt.ylim(-0.1, 10)
plt.xlabel(r'$\mathrm{Major\, merger\,mass}$')
plt.ylabel(r'$\mathrm{NMajor}$')

plt.scatter(CBMA, NMA, s=1)

# Save the figure #
plt.savefig('XYZ1-' + date + '.png')

########################################################################################################################

plt.close()
fig = plt.figure(0, figsize=(10, 7.5))

# plt.xscale('log')
# plt.yscale('log')
# plt.xlim(0.01, 0.1)
# plt.ylim(-0.1, 10)
plt.xlabel(r'$\mathrm{CBM}$')
plt.ylabel(r'$\mathrm{CBMA+CBMI}$')

plt.scatter(CBM, CBMA + CBMI, s=1)

# Save the figure #
plt.savefig('XYZ2-' + date + '.png')

########################################################################################################################

plt.close()
fig = plt.figure(0, figsize=(10, 7.5))

# plt.xscale('log')
# plt.yscale('log')
# plt.xlim(0.01, 0.1)
# plt.ylim(-0.1, 10)
plt.xlabel(r'$\mathrm{BM}$')
plt.ylabel(r'$\mathrm{CBM+PBM}$')

plt.scatter(BM, CBM + PBM, s=1)

# Save the figure #
plt.savefig('XYZ3-' + date + '.png')

########################################################################################################################

plt.close()
fig = plt.figure(0, figsize=(10, 7.5))

# plt.xscale('log')
# plt.yscale('log')
# plt.xlim(0.01, 0.1)
# plt.ylim(-0.1, 10)
plt.xlabel(r'$\mathrm{SM}$')
plt.ylabel(r'$\mathrm{BM+DBM}$')

plt.scatter(SM, BM + DM, s=1)

# Save the figure #
plt.savefig('XYZ4-' + date + '.png')