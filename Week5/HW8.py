
## Christopher Smith
## HW8: Global Ozone Animation
## 10/3/19

#import modules
import numpy as np
import matplotlib.pyplot as plt
import netCDF4
from mpl_toolkits.basemap import Basemap
import glob
import os
import h5py
import MCB


#import the path that contains Jeff's OMI_DATA
path='/homes/metofac/jeff/AOSC652/Week5/OMI_Data'

#conduct a while loop starting from day 1 to 31.

day=1
while(day<32):
	#Import the filename to include the day of the month of may
	filename=glob.glob('/homes/metofac/jeff/AOSC652/Week5/OMI_Data/OMI-Aura_L2G-OMDOAO3G_2017m05'+format(day,'02d')+'*.he5')
	print(filename)

	#Read each file
	f=h5py.File(filename[0],mode='r')
	#Assign variables to only the second and third colums (not n-candidate)
	ozone=f['HDFEOS/GRIDS/ColumnAmountO3/Data Fields/ColumnAmountO3'][0,:,:]
	#Mask the ozone data that is a filler value
	ozone=np.ma.masked_where(ozone == -1.2676506E30, ozone)
	print(ozone)
	'''
	lat=f['HDFEOS/GRIDS/ColumnAmountO3/Data Fields/Latitude'][0,:,:]
	lon=f['HDFEOS/GRIDS/ColumnAmountO3/Data Fields/Longitude'][0,:,:]
	
	#Define the figure
	fig1=plt.figure(figsize=[6,9])

	
	#Define the basemap parameters
	m= Basemap(projection='ortho', lat_0=40, lon_0=-5)
	m.fillcontinents(color="white")
	#Convert the 2D lon/lat arrays to x,y
	x,y = m(lon,lat)
	#Define the x,y (lon,lat) for Paris and plot the star/label on the map
	px, py = m(2.3522, 48.8566)
	pm, pb = m(2.3522, 40)
	plt.plot(px, py, marker = '*',markersize=9,color ='blue')
	plt.text(pm, pb, 'Paris, France', fontsize = 10, fontweight = 'bold', bbox=dict(facecolor='white', edgecolor='white'))
	#counter should start at 1
	m.plot(x[:day], y[:day])
	m.plot(x[day-1], y[day-1])
	v = np.linspace(150.,555.,46.)
	#Define color scale for map
	cm = MCB.Jeff1()
	cf = m.contourf(x, y, ozone, v, cmap=cm)
	#cf = m.contourf(x, y, ozone, v, cmap="jet")
	#cnt = m.contour(x, y, ozone, v, cmap="jet")
	cb = plt.colorbar(cf)
	#Set labels and limits
	cb.set_label('Total Column Ozone (DU)', rotation=270, labelpad=10)
	plt.clim(150.,550.)
	plt.title('OMI Total Column Ozone: May' + ' '+format(day, '02d')+' ' +'2017')
	m.drawcoastlines()
	#Save each figure as a .png 
	fig1.savefig('ozone{0:03.0f}.png'.format(day))
	plt.show()
	print(day)
	'''
	day+=1




	

	
	
	



