
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
    
## Installation
```bash
pip install chemaphy
```

## How it works?

```bash

import chemaphy
from chemaphy import Constants
from chemaphy import ProjectileMotion
from chemaphy import LogarithmicFunction
from chemaphy import Statistics

print(chemaphy.pi.value)
print(ProjectileMotion.horizontal_range(100,Constants.g_Earth,45))
print(LogarithmicFunction.log_e(2))
print(LogarithmicFunction.log_10(2))
print(Statistics.Mean([1,2,3,4,5,6,7,8,9,0]))
print(Statistics.Median([1,2,3,4,5,6,7,8,9,0]))
```
### Output

```bash
3.1415
1020.41 m
0.693
0.301
4.5
5.5
```

# Constants

There are so many constants which we use for scientific calculations such as:\

    1. Plank's Constants
    2. pi
    3. e
    4. gravity on different planets
    5. Mass and Radius of different planets
    6. Rydberg's Constants
    and so on...
