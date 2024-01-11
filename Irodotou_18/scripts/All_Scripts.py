# Import required python libraries #
import time
import h5py
import numpy as np
import pandas as pd
import seaborn as sns
import scipy.optimize as so
from scipy.ndimage import zoom
import matplotlib.pyplot as plt
from astropy.table import Table
from matplotlib.colors import LogNorm
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import colors, ticker, cm
import matplotlib.collections as collections
from matplotlib.legend_handler import HandlerBase
from mpl_toolkits.axes_grid1.inset_locator import mark_inset
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes

# Declare the plotting style #
sns.set()
sns.set_style('ticks', {'axes.grid':True})
sns.set_context('notebook', font_scale=1.6)
lw = 3  # linewidth
mc = 3  # mincnt
sp = 3  # scatterpoints
ms = 5  # markersize
gs = 150  # gridsize
size = 50  # size

# Physical units and simulation parameters #
redshift = 0.0
hubble = 0.673  # [dimensionless]
obsHubble = 0.70  # [dimensionless]
boxside = 480.28  # [Mpc/h]
VelocityUnits = 1  # [Km/s]
LengthUnits = 1e3 / hubble  # [Kpc]
MassUnits = 1e10 / hubble  # [Msun]
SpinUnits = 1e3 / hubble  # [Km/s * Kpc]

# Start the time #
start_time = time.time()
date = time.strftime("%d\%m\%y\%H%M")

# Define the desired snap, read local data and save them at SavePath #
snap = '58'
SavePath = './L-Galaxies_Data/Local/'
exec(open("All_Data_Local.py").read())

# Print the time it took to read the data #
print("--- %s seconds ---" % (time.time() - start_time))

########################################################################################################################
# Define the desired snap, read the data and save them at SavePath #
snap = '58'
# SavePath = './L-Galaxies_Data/58/'
# exec(open("All_Data_58.py").read())
# exec(open("Gas.py").read())
exec(open("SMF.py").read())
# exec(open("Tully_Fisher.py").read())
exec(open("Galaxy_Fraction.py").read())
# exec(open("DiskMass_Vs_DiskSpin.py").read())
exec(open("StellarMass_Decomposition.py").read())
# exec(open("BulgeMass_Vs_BlackHoleMass.py").read())
# exec(open("StellarMass_Vs_GalacticSpin.py").read())
# exec(open("BulgeMass_Vs_BlackHoleMass_Types.py").read())

# Define the desired snap, read the data and save them at SavePath #
snap = '56'
SavePath = './L-Galaxies_Data/58/'
# exec (open("All_Data_56.py").read())
# exec (open("CompMass_Vs_DiskScaleLength.py").read())
# exec(open("StellarMass_Vs_DiskScaleLength.py").read())

# Define the desired snap, read the data and save them at SavePath #
snap = '55'
SavePath = './L-Galaxies_Data/58/'
# exec (open("All_Data_55.py").read())
# exec(open("StellarMass_Vs_HalfMassRadius_ETGs.py").read())
# exec(open("StellarMass_Vs_HalfMassRadius_LTGs.py").read())

# Define the desired snap, read the data and save them at SavePath #
SnapList = ['58', '38', '30', '25']
for i in range(0, 4):
    snap = SnapList[i]
    SavePath = './L-Galaxies_Data/Evo/' + snap  # exec (open("All_Data_Evo.py").read())  # exec (open(
    # "StellarMass_Decomposition_Evo.py").read())

# exec(open("XYZ.py").read())

########################################################################################################################

# Print the total time #
print("--- %s seconds ---" % (time.time() - start_time))
