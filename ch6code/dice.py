import numpy as np
from pylab import *

N = 10000
outcome = np.random.geometric(1.0/6.0, size=N)
print "outcome:",outcome
enemy = np.zeros(N)
print "enemy:",enemy
enemy[0] = outcome[0]

for i in range(1, len(outcome)):
   enemy[i] = outcome[i] + enemy[i - 1]

print "enemy:",enemy

us = 6 * np.arange(1, len(enemy) + 1)
print "us:",us
t = np.arange(N)
print "t:",t

plot(t, enemy, lw=1)
plot(t, us, lw=2)
show()
