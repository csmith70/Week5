import LHD
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
# Load Data into array 
# Read in vostok_climate_record.dat 
###### 104 lines of header #######
# Mask all -999
# Remove all rows with masks
data_in = 
data_in =  # hides -999
data_in =  #Deletes any row containing -999

depth = data_in[:,0]
age = data_in[:,1]
deut = data_in[:,2]
temp = data_in[:,3]

## Number of Observations
n = ???

n1 = 100000  #Number of X steps to compute
year_min = 150
year_max = ????

# aEven is evenly spaced age or years
aEven = 

#tEven is temp data interperlated onto the evenly spaced age
tEven =  

### From this point forward EVERYTHING is based on evenly spaced age (aEven)
### and evenly spaced temp (tEven)
#figure 1 raw data 
plt.plot(?????)
plt.ylabel('Temperature')
plt.xlabel('Year')
plt.title('Interp Core Data')
plt.show()

#figure 2 Frequency (Compute FFT)
Y = np.fft.fft(???)

# What is the Frequency Step (Freq = 1/time) (FS = 1/change in time per step)
Fs = 

##### Reconstitute X-axis in Frequency (f)
f =   # New X axis  from 0 to the Frequency Step with n1 points

##### The modulus (absolute value) of a complex value
power = 

# Normalize the Power Spectrum  ( Values 0-1)
power = 

pmax = 1.1
plt.plot(f, power)
plt.xlim(5e-6, 6e-5)
plt.ylim(0, pmax)
plt.xlabel('cycles/year')
plt.ylabel('power')
plt.title('Frequency without Hanning Taper')
plt.show()

#figure 3  Power vs Time (t)
t=????
plt.plot(t, power)
plt.xlim(1000, 150000)
plt.ylim(0, pmax)
plt.xlabel('year/cycle')
plt.ylabel('power')
plt.title('Time without Hanning Taper')
plt.gca().invert_xaxis() ### this flips the x-axis
plt.show()

#Need to generate a Hanning Taper Window (han)
han = sp.hanning(??)

#apply hanning
tEven_han = 

#figure 4
##### Apply Hanning Smoothly
# Compute the FFT with Hanning tapered values
Y_han = np.fft.fft()

power_han = 
## Normalized Power Spectrum
power_han = 
pmax = 1.1
plt.plot(f, power_han, label='With Hanning')
plt.plot(f, power, label='Without Hanning')
plt.xlim(5e-6, 6e-5)
plt.ylim(0, pmax)
plt.xlabel('cycles/year')
plt.ylabel('power')
plt.title('Frequency')
plt.legend(loc=0)
plt.show()

#figure 5
plt.plot(t, power_han, label='With Hanning')
plt.plot(t, power, label='Without Hanning')
plt.xlim(1000, 150000)
plt.ylim(0, pmax)
plt.xlabel('year/cycle')
plt.ylabel('power')
plt.title('Time')
plt.legend(loc=0)
plt.gca().invert_xaxis()
plt.show()
