import chemaphy
from chemaphy import ProjectileMotion as pm
from chemaphy import LogicGates as lg
from chemaphy import AlternatingCurrent as ac
from chemaphy import Statistics as stats

print(pm.(100,chemaphy.g_earth.value,45))
print(ac.Vrms2V(220))
print(lg.OR(1,0))
print(stats.Mean([1,2,3,4,5,6,7,8,9,0]))
print(stats.Median([1,2,3,4,5,6,7,8,9,0]))
print(stats.Quartiles([375, 211, 23, 39, 118, 97, 971, 702, 143, 9]))
