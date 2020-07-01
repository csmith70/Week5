import numpy as np
import matplotlib.pyplot as plt
import netCDF4
from mpl_toolkits.basemap import Basemap

filename = 'start08_rf01_AWAS_merged_final_v03.nc'
f= netCDF4.Dataset(filename, mode='r')
time = f.variables['UTMID'][:]
lon = f.variables['LONC'][:]
lat = f.variables['LATC'][:]
alt = f.variables['GGALT'][:]
ozone = f.variables['O3_NOAA'][:]
wind = f.variables['WSC'][:]
print(lat)
print(len(time))
print(np.shape(lat))
f.close()
i=1
while i < len(time):
	fig1 = plt.figure(figsize=[6,9])

	# we are plotting a 6row 1 column grid
	ax1 = plt.subplot2grid((6,1),(0,0), rowspan=3)
	ax2 = plt.subplot2grid((6,1),(3,0))
	ax3 = plt.subplot2grid((6,1),(4,0))
	ax4 = plt.subplot2grid((6,1),(5,0))

	# Map Stuff
	m = Basemap(projection='lcc', lat_0=45, lon_0=-100, lat_1=50, width=9000000, height=6000000, ax = ax1)
	m.drawmapboundary(fill_color='#000000')
	m.fillcontinents(color='#ddaa66', lake_color='#9999FF')
	m.drawcoastlines()

	#convert lat and lon to X and Y
	x,y = m(lon, lat)

	# counter should start at 1
	m.plot(x[:i], y[:i])
	print(i)
	i+=1

	m.plot(x[i-1], y[i-1], marker='o')
	ax2.plot(time[:i], alt[:i])
	ax2.plot(time[i-1], alt[i-1], marker='o')
	ax3.plot(time[:i], ozone[:i])
	ax3.plot(time[i-1], ozone[i-1], marker='o')
	ax4.plot(time[:i], wind[:i])
	ax4.plot(time[i-1], wind[i-1], marker='o')

	ax1.set_title('Flight Path Apr 18, 2008')
	ax2.set_title('Observations Collected During Flight')
	ax1.set_ylabel('Latitude')
	ax2.set_ylabel('Altitude (m)')
	ax3.set_ylabel('Ozone (PPB)')
	ax4.set_ylabel('Wind Speed (m/s)')

	ax2.set_xlim(np.min(time), np.max(time))
	ax2.set_ylim(np.min(alt), np.max(alt))
	ax3.set_xlim(np.min(time), np.max(time))
	ax3.set_ylim(np.min(ozone), np.max(ozone))
	ax4.set_xlim(np.min(time), np.max(time))
	ax4.set_ylim(np.min(wind), np.max(wind))
	print(i)
	i+=1
	#plt.show()

	fig1.savefig('plot{0:03.0f}.png'.format(i))

	print(i)
	i+=1








