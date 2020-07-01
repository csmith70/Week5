## Christopher Smith
## HW8 Practice
## 06/12/2020

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
	cloud_frac=f['HDFEOS/GRIDS/ColumnAmountO3/Data Fields/CloudFraction'][0,:,:]
	#Mask the ozone data that is a filler value
	cloud_frac=np.ma.masked_where(cloud_frac == -1.2676506E30, cloud_frac)
	cloud_press = f['HDFEOS/GRIDS/ColumnAmountO3/Data Fields/CloudPressure'][0,:,:]
	cloud_press=np.ma.masked_where(cloud_press == -1.2676506E30, cloud_press)
	print(cloud_press)
	#print(cloud_frac)
	day +=1

