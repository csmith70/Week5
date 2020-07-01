import LHD
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

data_in = LHD.load_space_data('sunspot_number_monthly.dat',3)
print(data_in)

year = data_in[:,0]
sunspot = data_in[:,3]

n1 = 10000
year_min = 1784
year_max = 2017
OrgX = year
OrgY = sunspot


##FFT
aEven = np.linspace(year_min, year_max, n1, dtype=float)
sunEven = np.interp(aEven, OrgX, OrgY, left=None, right=None, period=None)
print(max(sunEven))

