import LHD
import numpy as np
import matplotlib.pyplot as plt
# Load Data into array (sunspot_number_monthly.dat)
data_in = LHD.load_space_data('sunspot_number_monthly.dat', 3)
#data_in = ???? # hides -999
#data_in = ???? #Deletes any row containing -999

# Raw Data
year = data_in[:,0]
month = data_in[:,1]
year_frac = data_in[:,2]
sunspot_number = data_in[:,3]

## Number of Data Points
n = len(year)

## Take the FFT of the evenly spaced sunspot data
Y = np.fft.fft(sunspot_number)
print(np.shape(Y))
# What is the Frequency Step (Freq = 1/time) (FS = 1/change in time per step)
Fs=1/(year_frac[4]-year_frac[3])
print(np.shape(Fs))

## Reconstitute X-axis in Frequency Space
## From 0 to Fs with number of Obs Points 
f = np.linspace(0,Fs,n)
## Get rid of negative values by taking the square of the absolute value of Y
power = pow(abs(Y), 2)

## Normalize the Power Spectrum  0<P<1
power_norm = power/np.amax(power[1:round(n/2)])
pmax = 1.1

# Plot 1 Year vs Raw Sunspot Numbers
plt.plot(year_frac,sunspot_number)
plt.title('Raw Sunspot Numbers')
plt.show()

# Plot 2 Frequency Power Spectrum
plt.xlim(0,0.5)
plt.ylim(0,pmax)
plt.plot(f,power_norm, marker='o', color='c', ls='none')
plt.vlines(f,0,power_norm)
plt.xlabel('cycles/year')
plt.ylabel('power')
plt.title('Sunspot Cycle Frequency')
plt.show()

# Plot 3 Time Power Spectrum
### How to get the X axis is Time Space
t = 1/f
pmax = 1.1  ## Set Max Y
plt.plot(t,power_norm, marker='o', label="Python FFT")
plt.vlines(t,0,power_norm)
plt.xlim(5,15)
plt.ylim(0,pmax)
plt.xlabel('years/cycle')
plt.ylabel('power')
plt.title('Length of Sunspot Cycle')
plt.legend(loc=0)
plt.show()

# Plot 4  Inverse FFT
iY = np.fft.ifft(Y)
plt.plot(year_frac,iY)
plt.plot(year_frac,sunspot_number)
plt.title('Raw Sunspot Numbers vs Inverse FFT')
plt.show()


