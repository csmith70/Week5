#Christopher Smith
#HW16(alt): FORTRAN Running Mean and Root Finding

#Import modules
import numpy as np
import matplotlib.pyplot as plt
import MyFunctions as mf
from scipy.io import FortranFile
import LHD

#Load data using LHD load text data fxn.
data_in = LHD.load_space_data('global_temp_rec.dat', 0)
#Mask data that is of non-expected (filler) values
masked_data = np.ma.masked_where(data_in == -999., data_in)
#Load array of just the years using all the rows and the first column of data
years = masked_data[:,0]
print(years)

#Load array of just temperatures using all the rows and the second column of data
temps = masked_data[:,1]
print(temps)

#Plot scatterplot of Years versus Temperature Anomalies
plt.scatter(years, temps, label = 'Original Data')
masked_data = np.ma.masked_where(data_in == -999., data_in)

#Load in running mean data from fort.98 file
av = LHD.load_space_data('fort.98',0)
print(av)

#Load array of all the rows and first column of data (years)
yearsav = av[:,0]
#Load array of all rows and second column of data (running mean temps)
tempsav = av[:,1]

##Calculate third order best fit for running mean data
## Need New X Values  (Could reuse Years)
xfit = np.linspace(np.nanmin(yearsav), np.nanmax(yearsav))
print(xfit)
# Cubic Fit 
## Generate Cubic Fit Coef
coef_cube = np.polyfit(yearsav[0:135], tempsav[0:135], 3)
print(coef_cube) #Use to plug in bisection.f to find root
## Generate Cubic Fit Function
wfit = np.poly1d(coef_cube)
#print(wfit)
## Generate New Y Values
yfit_3 = wfit(xfit)

# Plot Cubic Fit and fort.98 file (running mean)
#plt.plot(years, temps, color ='red', label='Original Data')
plt.plot(yearsav, tempsav, color='green', label='FORTRAN Running Mean')
plt.plot(xfit, yfit_3, color='black',label='Cubic Fit')
#idx = np.argwhere(np.diff(np.sign(tempsav - temps[2:136]))).flatten()
#plt.plot(years[idx], yfit_3[idx], 'ro')

plt.legend(loc = 0) #Plot legend in best location
#Plot x intercept from root found in bisection.f
xs = 1961.940
ys = 0
plt.plot(xs, ys, '-r*', label='Global Mean Turns Positive')
#Plot labels,title, and line for y=0 
plt.xlabel('Years') 
plt.ylabel('Temp Anomaly in\n Degrees Celsius')
plt.title('Global Temperature Anomaly 1880-2018')
plt.hlines(0,1880,2018)
plt.legend(loc = 0)
plt.show()
