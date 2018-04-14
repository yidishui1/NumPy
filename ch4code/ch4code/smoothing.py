import numpy as np
import sys
from matplotlib.pyplot import plot
from matplotlib.pyplot import show
import os

homedir = os.getcwd()+'/NumPy/ch4code/ch4code/'

N = 8

weights = np.hanning(N)
print "Weights", weights

bhp = np.loadtxt(homedir+'BHP.csv', delimiter=',', usecols=(6,), unpack=True)
print "bhp",bhp
bhp_returns = np.diff(bhp) / bhp[ : -1]
print "bhp_returns",bhp_returns
smooth_bhp = np.convolve(weights/weights.sum(), bhp_returns)[N-1:-N+1]
print "smooth_bhp",smooth_bhp

vale = np.loadtxt(homedir+'VALE.csv', delimiter=',', usecols=(6,), unpack=True)
vale_returns = np.diff(vale) / vale[ : -1]
smooth_vale = np.convolve(weights/weights.sum(), vale_returns)[N-1:-N+1]

K = 3
t = np.arange(N - 1, len(bhp_returns))
poly_bhp = np.polyfit(t, smooth_bhp, K)
poly_vale = np.polyfit(t, smooth_vale, K)

poly_sub = np.polysub(poly_bhp, poly_vale)
xpoints = np.roots(poly_sub)
print "Intersection points", xpoints

reals = np.isreal(xpoints)
print "Real number?", reals

xpoints = np.select([reals], [xpoints])
xpoints = xpoints.real
print "Real intersection points", xpoints

print "Sans 0s", np.trim_zeros(xpoints)

plot(t, bhp_returns[N-1:], lw=1.0)
plot(t, smooth_bhp, lw=2.0)

plot(t, vale_returns[N-1:], lw=1.0)
plot(t, smooth_vale, lw=2.0)
show()
