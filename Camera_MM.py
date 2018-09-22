# This python code uses MicroManager device drivers to control a camera.
# Tested on MM_DemoCam, should work similarly on other cameras.
#Environment setup instructions: https://micro-manager.org/wiki/Using_the_Micro-Manager_python_library

import sys
sys.path.append("C:\Program Files\Micro-Manager-1.4")
import MMCorePy #load MicroManager for device control
import matplotlib.pyplot as plt

mmc = MMCorePy.CMMCore()  # Instance micromanager core
mmc.getVersionInfo()
print(mmc.getVersionInfo())
#print_out='MMCore version 8.1.0'
mmc.getAPIVersionInfo()
print(mmc.getAPIVersionInfo())
#print out='Device API version 65, Module API version 10'

# Demo camera example, continuation of previous listing
mmc.loadDevice('Camera', 'DemoCamera', 'DCam')
mmc.initializeAllDevices()
mmc.setCameraDevice('Camera')

#Snapping single image/grayscale
mmc.snapImage()
img = mmc.getImage()  # img - it's just numpy array
#img
#array([[12, 12, 13, ..., 11, 12, 12],
#       [12, 12, 13, ..., 11, 12, 12],
#       [12, 13, 13, ..., 12, 12, 12], dtype=uint8)

plt.imshow(img, cmap='gray')
plt.show()  # And window will appear

#Snapping single image/color
mmc.setProperty('Camera', 'PixelType', '32bitRGB')  # Change pixel type
rgb32 = mmc.getImage()
rgb32
#array([[1250067, 1250067, 1315860, ..., 1250067, 1250067, 1250067],
#      [1250067, 1315603, 1315860, ..., 1250067, 1250067, 1250067],
#      [1250067, 1315859, 1315860, ..., 1250067, 1250067, 1250067],
#      ...,
#      [1246483, 1246483, 1246483, ..., 1181204, 1246740, 1246484],
#      [1246483, 1246483, 1246483, ..., 1246740, 1246740, 1246483],
#      [1246483, 1246483, 1312019, ..., 1246740, 1246740, 1246483]], dtype=uint32)

#plt.imshow(img, cmap='jet')
plt.imshow(img, cmap='Blues', interpolation='nearest')
#Possible values are: Accent, Accent_r, Blues, Blues_r, BrBG, BrBG_r, BuGn, BuGn_r, BuPu, BuPu_r, CMRmap, CMRmap_r, Dark2, Dark2_r, GnBu, GnBu_r, Greens, Greens_r, Greys, Greys_r, OrRd, OrRd_r, Oranges, Oranges_r, PRGn, PRGn_r, Paired, Paired_r, Pastel1, Pastel1_r, Pastel2, Pastel2_r, PiYG, PiYG_r, PuBu, PuBuGn, PuBuGn_r, PuBu_r, PuOr, PuOr_r, PuRd, PuRd_r, Purples, Purples_r, RdBu, RdBu_r, RdGy, RdGy_r, RdPu, RdPu_r, RdYlBu, RdYlBu_r, RdYlGn, RdYlGn_r, Reds, Reds_r, Set1, Set1_r, Set2, Set2_r, Set3, Set3_r, Spectral, Spectral_r, Wistia, Wistia_r, YlGn, YlGnBu, YlGnBu_r, YlGn_r, YlOrBr, YlOrBr_r, YlOrRd, YlOrRd_r, afmhot, afmhot_r, autumn, autumn_r, binary, binary_r, bone, bone_r, brg, brg_r, bwr, bwr_r, cividis, cividis_r, cool, cool_r, coolwarm, coolwarm_r, copper, copper_r, cubehelix, cubehelix_r, flag, flag_r, gist_earth, gist_earth_r, gist_gray, gist_gray_r, gist_heat, gist_heat_r, gist_ncar, gist_ncar_r, gist_rainbow, gist_rainbow_r, gist_stern, gist_stern_r, gist_yarg, gist_yarg_r, gnuplot, gnuplot2, gnuplot2_r, gnuplot_r, gray, gray_r, hot, hot_r, hsv, hsv_r, inferno, inferno_r, jet, jet_r, magma, magma_r, nipy_spectral, nipy_spectral_r, ocean, ocean_r, pink, pink_r, plasma, plasma_r, prism, prism_r, rainbow, rainbow_r, seismic, seismic_r, spring, spring_r, summer, summer_r, tab10, tab10_r, tab20, tab20_r, tab20b, tab20b_r, tab20c, tab20c_r, terrain, terrain_r, viridis, viridis_r, winter, winter_r
plt.show()  # And window will appear