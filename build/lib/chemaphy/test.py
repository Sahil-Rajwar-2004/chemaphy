from chemaphy import Statistics as stats
from chemaphy import Sort
from chemaphy import Algo
from chemaphy import Matrix
from chemaphy import Sets
import numpy as np

array = [9,8,7,6,5,4,3,2,1,0]

print(stats.mean(array))
print(stats.median(array))
print(stats.geometric_mean(array))
print(stats.harmonic_mean(array))
print(Sort.merge_sort(array))


x = [1,2,3,1,5]
y = [1,3,5]
print(Sets.union(Sets.set(x),Sets.set(y)))
