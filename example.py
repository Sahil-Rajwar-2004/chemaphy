import chemaphy
from chemaphy import ProjectileMotion as pm
from chemaphy import LogicGates as lg
from chemaphy import AlternatingCurrent as ac
from chemaphy import Statistics as stats
from chemaphy import Temperature as temp
from chemaphy import PeriodicTable as pt
from chemaphy import BinaryConverter

print(pm.(100,chemaphy.g_earth.value,45))
print(ac.Vrms2V(220))
print(lg.OR(1,0))
print(stats.Mean([1,2,3,4,5,6,7,8,9,0]))
print(stats.Median([1,2,3,4,5,6,7,8,9,0]))
print(stats.Quartiles([375, 211, 23, 39, 118, 97, 971, 702, 143, 9]))

print(temp.c2k(27)) #-> celcius to kelvin
print(temp.c2f(27)) #-> celcius to fahrenheit
print(temp.k2c(27)) #-> kelvin to celcius
print(temp.k2f(27)) #-> kelvin to fahrenheit
print(temp.f2c(27)) #-> fahrenheit to celcius
print(temp.f2k(27)) #-> fahrenheit to kelvin

print(BinaryConverter.str2binary("Hello"))
print(BinaryConverter.str2hexadecimal("Hello"))
print(BinaryConverter.str2octadecimal("Hello"))

print(BinaryConverter.int2binary([1,2,3,4,5]))
print(BinaryConverter.int2binary(5))

print(BinaryConverter.int2hexadecimal([1,2,3,4,5,222,111]))
print(BinaryConverter.int2hexadecimal(5))

print(BinaryConverter.int2octadecimal([1,2,3,4,5]))
print(BinaryConverter.int2octadecimal(5))

print(pt.atomic_number(17))
print(pt.element("chlorine"))
print(pt.symbol("cl"))
