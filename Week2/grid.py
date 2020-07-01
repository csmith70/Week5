# Christopher Smith
# HW3: Lat/Lon Grid
# Due: 9/10/19

#Import numpy module
import numpy as np
#Create numpy array that contains 300 latitudes from -90 to 90
lat = np.linspace(-90, 90 ,300)
#Create numpy array that contains longitudes 0 to 360, every 1.25 degrees. Do not include 360 degrees.
lon = np.arange(0,360,1.25)
#Print out latitudes and longitudes
print('Latitudes include:', lat)
print('Longitudes include:', lon)
# Create a 2D lat and lon array using numpy's meshgrid function
lon2d, lat2d = np.meshgrid(lon, lat)
#Print out latitudes and longitudes 
print('Latitudes include:', lat2d)
print('Longitudes include:', lon2d)
