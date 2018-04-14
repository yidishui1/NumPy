import numpy as np
import datetime
import os

def datestr2num(s):
   return datetime.datetime.strptime(s, "%d-%m-%Y").toordinal()

print


homedir = os.getcwd()+'/NumPy/ch7code/'
dates,closes=np.loadtxt(homedir+'AAPL.csv', delimiter=',', usecols=(1, 6), converters={1:datestr2num}, unpack=True)
print "datestr2num", datestr2num
print "dates",dates
print "closes", closes
indices = np.lexsort((dates, closes))

print "Indices", indices
print ["%s %s" % (datetime.date.fromordinal(int(dates[i])),  closes[i]) for i in indices]
