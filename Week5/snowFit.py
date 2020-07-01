import LHD
import numpy as np
import matplotlib.pyplot as plt
import MyFunctions as mf
import scipy.stats as sps

# Load Data into array
data_in = LHD.load_space_data('LancasterPA_Snow.csv', 2)
data_in = np.ma.masked_where(data_in == -999, data_in) # hides -999

season = data_in[:,0]
snow = data_in[:,2]
print(snow)

# Plot XY original data
plt.plot(season, snow, 'o', label='Original Data') 

# Running mean 5 year
## Generate Running Mean
rmsnow, window = mf.running_mean(snow, 5)
plt.plot(season[2:-2], rmsnow[2:-2], label='5-yr running mean')

# Linear Fit
## Generate Linear Fit Coef
coef_lin = np.polyfit(season,snow,1)
print(coef_lin)
## Generate Linear Fit Formula
lfit = np.poly1d(coef_lin)
## Need New X Values  (Could reuse Season)
xfit = np.linspace(np.amin(season), np.amax(season), 300)
yfit_1 = lfit(xfit)
plt.plot(xfit, yfit_1, color='red', label='Linear Fit')

### How to Plot 100 years in past???
xfit_p = np.linspace(np.amin(season)-100, np.amax(season), 300)
yfit_1p = lfit(xfit_p)
plt.plot(xfit_p, yfit_1p, ls='--', color='red', label='Linear Fit Projection: y={0:1.3f}x + {1:1.3f}'.format(coef_lin[0], coef_lin[1]))

# Scipy linregress
## Generate Linear Fit Coef
lr = sps.linregress(season, snow) ## Returns (m, b, r, p, error)
## General Linfit Function
LinFit = np.poly1d(lr[:2])
## Generate new y values
LinY = LinFit(xfit)
plt.plot(xfit, LinY, label='Linear Regression Fit')

# Quadratic Fit 
## Generate Quadratic Fit Coef
coef_quad = np.polyfit(season, snow, 2)
## Generate Quad Fit Function
qfit = np.poly1d(coef_quad)
## Generate New y Values
yfit_2 = qfit(xfit)
plt.plot(xfit, yfit_2, label='Quadritic Fit')

# General Plotting Parts
plt.title('Seasonal Snowfal for Lancaster, PA\n1926-2017')
plt.xlabel('Snow Season')
plt.ylabel('Snowfall in inches')
plt.legend(loc=0)
plt.show()

