#### HDF Code
# Import modules
import numpy as np
import matplotlib.pyplot as plt
import h5py
from mpl_toolkits.basemap import Basemap

## Open the .he5 file and assign it to the file object 'f' 
#  mode = 'r' opens as read-only
filename = '/homes/metofac/jeff/AOSC652/Week5/NC+HDF/OMI-Aura_L3-OMTO3d_2016m0331_v003.he5'
f = h5py.File(filename,mode='r')

## Extract variables from the file object
lon = np.arange(-180,180,1)  ## Generate Lon since not included in file 
lat = np.arange(-90,90,1)  ## Generate Lat since not included in file
ozone = f['HDFEOS/GRIDS/OMI Column Amount O3/Data Fields/ColumnAmountO3'][:,:]
ozone = np.ma.masked_where(ozone == -1.2676506E30, ozone) ## Missing value in metadata
f.close()

#Define the map
#m=Basemap(projection='ortho', lat_0=51.5, lon_0=-117)
m= Basemap(projection='mill',lon_0=0)
m.drawcoastlines()
#m.drawstates(color='gray')
m.drawcountries()
#m.drawcoastlines()
#m.fillcontinents(color="#ddaa66")
#m.drawrivers()
m.drawmeridians(np.arange(-180,180,10))
m.drawparallels(np.arange(-90,90,10))

## Plotting the data
## turn 1D Lat and Long into 2D
lon2d,lat2d = np.meshgrid(lon,lat)
x,y = m(lon2d,lat2d)

# Generate filed contours
cf = m.contourf(x,y,ozone, 16)
# Generate countour lines
#cnt = m.contour(x, y, ozone, 16, colors='black')

%cb = plt.colorbar(cf)
cb.set_label('O3 in Dobson Units')

plt.title('OMI Column Ozone')
plt.xlabel('Longitude')
plt.ylabel('Latitude')

plt.show()
