import numpy as np

a = np.arange(7)
condition = (a % 2) == 0
print "condition",condition
print "Even numbers", np.extract(condition, a)
print "Non zero", np.nonzero(a)
