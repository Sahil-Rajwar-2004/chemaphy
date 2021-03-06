
# Chemaphy

For Scientific Calculations and made for those who daily deals with Scientific Calculations.

The Chemaphy word is derived form 3 words:\
Chemistry\
Mathematics\
Physics



## Author

- [Sahil Rajwar](https://twitter.com/justSahilRajwar)

# Documentation

## Requirments
    1. numpy
    2. trigo
    3. pandas
    4. statistics
    
## Installation
```bash
pip install chemaphy
```

## How it works?

```bash

import chemaphy
from chemaphy import ProjectileMotion as pm
from chemaphy import LogarithmicFunction as lf
from chemaphy import Statistics
from chemaphy import PeriodicTable as pt

print(chemaphy.pi.value)
print(pm.HorizontalRange(100,chemaphy.g_earth.value,45))
print(lf.log_e(2))
print(lf.log_10(2))
print(Statistics.Mean([1,2,3,4,5,6,7,8,9,0]))
print(Statistics.Median([1,2,3,4,5,6,7,8,9,0]))
print(Statistics.Quartiles([375, 211, 23, 39, 118, 97, 971, 702, 143, 9]))
print(pt.element("sodium"))
```
### Output

```bash
3.1415
1020.41 m
0.693
0.301
4.5
5.5
[39, 130.5, 375] -> [Higher Quartile, Middle Quartile, Lower Quartile]
AtomicNumber                         11
Element                          Sodium
Symbol                               Na
AtomicMass                        22.99
ElectronicConfiguration         [Ne]3s1
NumberofNeutrons                     12
NumberofProtons                      11
NumberofElectrons                    11
Period                                3
Group                               1.0
Phase                             solid
Unstable                             no
Stable                              yes
Metal                               yes
Nonmetal                             no
Metalloid                            no
Type                       Alkali Metal
AtomicRadius                        2.2
Electronegativity                  0.93
FirstIonization                  5.1391
Density                           0.971
MeltingPoint                     371.15
BoilingPoint                     1156.0
NumberOfIsotopes                    7.0
Discoverer                         Davy
Year                             1807.0
SpecificHeat                      1.228
NumberofShells                        3
NumberofValence                     1.0
```

# Constants

There are so many constants which we use for scientific calculations such as:

    1. Plank's Constants
    2. pi
    3. e
    4. gravity on different planets
    5. Mass and Radius of different planets
    6. Rydberg's Constants
    and so on...
