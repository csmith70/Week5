#Christopher Smith
#HW11: Fourier Series and Spectral Analysis
# Due: October 18, 2019

#import modules
import LHD
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
# Load Data into array 
# Read in vostok_climate_record.dat 
###### 105 lines of header #######
# Mask all -999
# Remove all rows with masks
data_in = LHD.load_space_data('vostok_climate_record.dat', 105)
data_in = np.ma.masked_where(data_in == -999, data_in) # hides -999
data_in = np.ma.compress_rows(data_in)  #Deletes any row containing -999

#Read in the data
depth = data_in[:,0]
age = data_in[:,1]
deut = data_in[:,2]
temp = data_in[:,3]
OrgX = age
OrgY = temp
print(OrgX)
print

## Number of Observations
n = len(age)
print(depth)

n1 = 100000  #Number of X steps to compute
year_min = 150
year_max = 422766

# aEven is evenly spaced age or years
aEven = np.linspace(year_min, year_max, n1, dtype=float)
print(np.shape(aEven))

#tEven is temp data interperlated onto the evenly spaced age
tEven = np.interp(aEven, OrgX, OrgY, left=None, right=None, period=None) 
print(np.shape(tEven))
### From this point forward EVERYTHING is based on evenly spaced age (aEven)
### and evenly spaced temp (tEven)
#figure 1 raw data 
fig1 = plt.figure(figsize=[9,12])
plt.plot(aEven, tEven)
plt.ylim(-10,4)
plt.ylabel('Temperature')
plt.xlabel('Year')
plt.title('Raw Core Data')
plt.show()
#Save Plot as Figure
fig1.savefig('RawData.png')

#figure 2 Frequency (Compute FFT)
fig2 = plt.figure(figsize=[9,12])

Y = np.fft.fft(tEven)
print(np.shape(Y))

# What is the Frequency Step (Freq = 1/time) (FS = 1/change in time per step)
Fs=1/(aEven[4]-aEven[3])
print(np.shape(Fs))

##### Reconstitute X-axis in Frequency (f)
f=np.linspace(0,Fs,n1) # New X axis  from 0 to the Frequency Step with n1 points

##### The modulus (absolute value) of a complex value
power = pow(abs(Y), 2)
print(np.shape(power))

# Normalize the Power Spectrum  ( Values 0-1)
power_norm = power/np.amax(power[1:round(n1/2)])

pmax = 1.1
plt.plot(f, power_norm)
plt.xlim(5e-6, 6e-5)
plt.ylim(0, pmax)
plt.xlabel('cycles/year')
plt.ylabel('power')
plt.title('Frequency without Hanning Taper')
plt.show()
#Save Plot as Figure
fig2.savefig('FnoHan.png')

#figure 3  Power vs Time (t)
t=1/f
fig3 = plt.figure(figsize=[9,12])
plt.plot(t, power_norm)
plt.xlim(1000, 150000)
plt.ylim(0, pmax)
plt.xlabel('year/cycle')
plt.ylabel('power')
plt.title('Time without Hanning Taper')
plt.gca().invert_xaxis() ### this flips the x-axis
plt.show()
#Save Plot as Figure
fig3.savefig('TnoHan.png')

#Need to generate a Hanning Taper Window (han)
han=sp.hanning(n1)
print(np.amax(han))
print(han)

#Condition evenly spaced temperature data with the Hanning Taper Widnow
tEven_han= tEven*han
print(np.amax(tEven_han))
print(np.amax(tEven))

#figure 4
##### Apply Hanning Smoothly
# Compute the FFT with Hanning tapered values
Y_han = np.fft.fft(tEven_han)

power_han = pow(abs(Y_han), 2)
## Normalized Power Spectrum
power_han_norm = power_han/np.amax(power_han[2:round(n1/2)])
pmax = 1.1
fig4 = plt.figure(figsize=[9,12])
plt.plot(f, power_han_norm, label='With Hanning')
plt.plot(f, power_norm, label='Without Hanning')
plt.xlim(5e-6, 6e-5)
plt.ylim(0, pmax)
plt.xlabel('cycles/year')
plt.ylabel('power')
plt.title('Frequency')
plt.legend(loc=0)
plt.show()
#Save Plot as Figure
fig4.savefig('Freq.png')

#figure 5
fig5 = plt.figure(figsize=[9,12])
plt.plot(t, power_han_norm, label='With Hanning')
plt.plot(t, power_norm, label='Without Hanning')
plt.xlim(1000, 150000)
plt.ylim(0, pmax)
plt.xlabel('year/cycle')
plt.ylabel('power')
plt.title('Time')
plt.legend(loc=0)
plt.gca().invert_xaxis()
plt.show()
#Save Plot as Figure
fig5.savefig('Time.png')

'''
#Figure 6
fig6 = plt.figure(figsize=[9,12])
plt.plot(aEven, tEven_han)
plt.ylim(-10,4)
plt.ylabel('Temperature')
plt.xlabel('Year')
plt.title('Hanning v Raw Core Data')
plt.show()
fig1.savefig('HanningT.png')
'''

