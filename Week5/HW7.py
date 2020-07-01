## Christopher Smith
## HW7 : Fitting Lines to Data
## 9/27/19

#Import modules
import LHD
import numpy as np
import matplotlib.pyplot as plt
import MyFunctions as mf

#Load data using LHD load text data fxn.
data_in = LHD.load_space_data('global_temperature_record.dat', 7)
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

# Running mean 5 year
## Generate Running Mean & Plot
rmtemps, window = mf.running_mean(temps, 5)
plt.plot(years[2:-2], rmtemps[2:-2], color = 'orange', label='5-yr running mean')
print(len(temps))

# Linear Best Fit
coef_lin = np.polyfit(years[0:138], temps[0:138], 1)
print(coef_lin)
## Generate Linear Fit Formula
lfit = np.poly1d(coef_lin)
## Need New X Values  (Could reuse Years)

xfit = np.linspace(np.nanmin(years), np.nanmax(years), 300)

## Generate New Y Values
yfit_1 = lfit(xfit)
#Plot Linear Fit
plt.plot(xfit, yfit_1, color='red', label='Linear Fit')

# Quadratic Fit 
## Generate Quadratic Fit Coef
coef_quad = np.polyfit(years[0:138], temps[0:138], 2)
## Generate Quad Fit Function
qfit = np.poly1d(coef_quad)
## Generate New Y Values
yfit_2 = qfit(xfit)
#Plot Quadratic Fit
plt.plot(xfit, yfit_2, color = 'green',label='Quadritic Fit')


# Cubic Fit 
## Generate Cubic Fit Coef
coef_cube = np.polyfit(years[0:138], temps[0:138], 3)
## Generate Cubic Fit Function
wfit = np.poly1d(coef_cube)
## Generate New Y Values
yfit_3 = wfit(xfit)
# Plot Cubic Fit
plt.plot(xfit, yfit_3, color='black',label='Cubic Fit')
print(coef_cube)

### Plot Linear Projection to 2050
xfit_p = np.linspace(np.amin(years), np.amax(years)+31, 300)

yfit_1p = lfit(xfit_p)
#Use scientific notation for variable x
plt.plot(xfit_p, yfit_1p, ls='--', color='red', label='Linear Fit Projection: y=({0:1.3E})x + {1:1.3f}'.format(coef_lin[0], coef_lin[1]))

### Plot Quadratic Projection to 2050
yfit_2p = qfit(xfit_p)
#Use scientific notation in equation
plt.plot(xfit_p, yfit_2p, ls='--', color='green', label='Quadratic Fit Projection: y=({0:1.3E})x^2 + {1:1.3E}'.format(coef_quad[0], coef_quad[1]))

### Plot Cubic Projection to 2050
yfit_3p = wfit(xfit_p)
#Use scientific notation in equation
plt.plot(xfit_p, yfit_3p, ls='--', color='black', label='Cubic Fit Projection: y=({0:1.3E})x^3 + {1:1.3E}'.format(coef_cube[0], coef_cube[1]))


#Make plot include labels, title, and legend
fig = plt.figure()
ax3 = plt.subplot2grid((8,2), (3,1))
plt.show()

plt.plot(yearsav, tempsav, color='green', label='FORTRAN running mean')
#Make plot include labels, title, and legend
plt.xlabel('Years')
plt.ylabel('Temp Anomaly in\n Degrees Celsius')
plt.title('Global Temperature Anomaly 1880-2018')
plt.legend(loc = 0)
plt.show()






