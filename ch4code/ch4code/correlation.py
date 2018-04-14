import numpy as np
from matplotlib.pyplot import plot
from matplotlib.pyplot import show
import os

homedir = os.getcwd()+'/NumPy/ch4code/ch4code/'

bhp = np.loadtxt(homedir+'BHP.csv', delimiter=',', usecols=(6,), unpack=True)
print "bhp", bhp

bhp_returns = np.diff(bhp) / bhp[ : -1]
print "bhp_returns", bhp_returns

vale = np.loadtxt(homedir+'VALE.csv', delimiter=',', usecols=(6,), unpack=True)
print "vale", vale

vale_returns = np.diff(vale) / vale[ : -1]
print "vale_returns", vale_returns


covariance = np.cov(bhp_returns, vale_returns) 
print "Covariance", covariance

print "Covariance diagonal", covariance.diagonal()
print "Covariance trace", covariance.trace()
print "bhp_returns.std()", bhp_returns.std()
print "vale_returns.std()", vale_returns.std()

print covariance/ (bhp_returns.std() * vale_returns.std())

print "Correlation coefficient", np.corrcoef(bhp_returns, vale_returns)

difference = bhp - vale
avg = np.mean(difference)
dev = np.std(difference)

print "Out of sync", np.abs(difference[-1] - avg) > 2 * dev

t = np.arange(len(bhp_returns))
plot(t, bhp_returns, lw=1)
plot(t, vale_returns, lw=2)
show()
