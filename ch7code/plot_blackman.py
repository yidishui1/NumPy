import numpy as np
from matplotlib.pyplot import plot, show, legend
from matplotlib.dates import datestr2num
import sys
import os

homedir = os.getcwd()+'/NumPy/ch7code/'
closes=np.loadtxt(homedir+'AAPL.csv', delimiter=',', usecols=(6,), converters={1:datestr2num}, unpack=True)
N = int(7)
window = np.blackman(N)
smoothed = np.convolve(window/window.sum(), closes, mode='same')
plot(smoothed[N:-N], lw=2, label="smoothed")
plot(closes[N:-N], label="closes")
legend(loc='best')
show()
