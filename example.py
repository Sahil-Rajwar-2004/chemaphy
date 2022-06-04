import chemaphy
from chemaphy import ProjectileMotion as pm
from chemaphy import LogicGates as lg
from chemaphy import AlternatingCurrent as sc

print(pm.horizontal_range(100,chemaphy.g_Earth.value,45))
print(ac.vrms2v(220))
print(lg.OR(1,0))

"""
Outputs:
1020.41 m
311.13 Volts
True
"""
