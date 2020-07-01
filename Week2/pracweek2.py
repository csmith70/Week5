import LHD
import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np
import statsmodels.api as sm

data_in = LHD.load_comma_data('practice.csv', 5)
df= pd.DataFrame(data_in)
#China = data_in[38,:]
China = df.iloc[38,4:59]
years = np.arange(1960, 2015, 1)
a= np.array(China)
print(a)
'''
plt.plot(years, a)
plt.show()

print(a)
print(a[0])

month = []
day = 1
while day < 55:
	fig=plt.figure(figsize=[9,12])
	emissions = a[day]
	plt.xlim([1960,2014])
	plt.ylim([100,6100])
	month.append(emissions)
	plt.xlabel('Year Past 1960')
	plt.ylabel('GDP/Capita(Constant 2010 $US)')
	plt.title('China GDP/Capita Per Year Since 1960')
	plt.plot(years[:day], month[:day])
	fig.savefig('plot{0:03.0f}.png'.format(day))
	day += 1
'''
b = a**2
#print(b)

data2_in = LHD.load_comma_data('practice2.csv', 5)
df2 = pd.DataFrame(data2_in)
ChinaCO2 = df2.iloc[38,4:59]
#print(ChinaCO2)
c = np.array(ChinaCO2)
#print(c)

###LINEAR REGRESSION PRACTICE###
nobs = len(c)
#print(nobs)
nrgs = 3

regressors = np.ones((nobs, nrgs), dtype=np.float)
regressors[:,1] = b
regressors[:,2] = a
#regressors[:,3] = c

#Create an ordinary least squares model
model = sm.OLS(c, regressors)

#Extract the constants 
constants = model.fit().params
print(constants)
#print('____Summary_____')
#print(model.fit().summary())

#Calculate the model fit result
model_T = constants[0] + constants[1]*b + constants[2]*a
print(model_T)

#Scatter Plot Practice
fig = plt.figure()
ax1 = fig.add_subplot(121)
ax1.scatter(years, a, color='b',label='GDP per Capita')
plt.title('GDP per Capita for China')
plt.xlabel('Year')
plt.ylabel('GDP/Capita (Constant 2010 $US')
plt.legend(loc=0)
plt.show()






	



