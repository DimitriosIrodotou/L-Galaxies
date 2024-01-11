# select mvir
# from Henriques2015a..MRscPlanck1
# where snapnum=14 and stellarMass > 0.01 and Type in (0,1)

dlog10 = 0.25

# Generate initial figure #
plt.close()
figure = plt.figure(0, figsize=(10, 7.5))

# Figure parameters #
plt.ylim(0, 0.2)
plt.xlim(1e9, 1e12)
plt.xscale('log')
plt.xlabel(r'$\mathrm{M_{200c} / M_{\odot}}$')
plt.ylabel(r'$\mathrm{f_{b}}$')
plt.tick_params(direction='in', which='both', top='on', right='on')

######################################################################################################################################################

colours = ['black' ,'red']
Mfs = [2.55322e+07, 5.59236e+07] #, 8.07818e+07, 1.10913e+08, 1.55786e+08, 1.95897e+08, 2.67120e+08,
    #    3.24999e+08, 3.83205e+08, 4.59202e+08, 5.58132e+08, 6.57569e+08, 7.53754e+08, 8.72445e+08, 1.05091e+09,
    #    1.30317e+09, 1.50271e+09, 1.62489e+09, 1.88957e+09, 2.05972e+09, 2.24168e+09, 2.37815e+09, 2.57857e+09,
    #    2.76060e+09, 2.88968e+09, 3.05478e+09, 3.29195e+09, 3.49527e+09, 3.69078e+09, 3.87066e+09, 3.98155e+09,
    #    4.09987e+09, 4.27223e+09, 4.54563e+09, 5.07460e+09, 5.32280e+09, 5.32373e+09, 5.44407e+09, 5.67396e+09,
    #    5.85088e+09, 5.88537e+09, 6.06476e+09, 6.31654e+09, 6.48256e+09]

for i, Mf in enumerate(Mfs):
    Masses = np.genfromtxt('./L-Galaxies_Data/' + str(i + 13) + '.txt', names=['Mvir'])
    Masses['Mvir'] *= MassUnits
    a = 2
    print(np.log10(min(Masses['Mvir'])))
    fb = 0.155 * (1 + (2 ** (a / 3) - 1) * (Masses['Mvir'] / Mf / hubble) ** (-a)) ** (-3/a)
    # Plot median and 1-sigma lines #
    x_value, median, shigh, slow = plot_tools.binned_median_1sigma(Masses['Mvir'], fb,
                                                                   bin_type='equal_width', n_bins=25, log=True)
    plt.plot(x_value, median, color=colours[i], linewidth=3)

# # Create the legends #
# colors = ['black', 'grey', 'lightgrey']
# squares = collections.RegularPolyCollection(numsides=6, sizes=(20,), facecolors=colors)
# legend = plt.legend([squares], [r'$\mathrm{This\;work}$'], scatterpoints=len(colors), scatteryoffsets=[.5],
# handlelength=len(colors), markerscale=2,
#                     frameon=False, loc=4)
#
# plt.gca().add_artist(legend)
# plt.legend(frameon=False, loc=2)
#
# # Plot L-Galaxies data - 2D histogram #
# hexbin = plt.hexbin(Bulge_Mass, Black_Hole_Mass, bins='log', cmap="Greys", mincnt=2)
#
# # Adjust the color bar #
# cbaxes = figure.add_axes([0.9, 0.11, 0.02, 0.77])
# cb = plt.colorbar(hexbin, cax=cbaxes)
# cb.set_label('$\mathrm{Counts\; per\; hexbin}$')

######################################################################################################################################################

# Save the figure #
plt.savefig('Okamoto-' + date + '.pdf', bbox_inches='tight')