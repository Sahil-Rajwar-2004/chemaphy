from chemaphy import Statistics as stats
from chemaphy import Sort
from chemaphy import Sets

array = [9,8,7,6,5,4,3,2,1,0]

print(stats.mean(array))
print(stats.median(array))
print(stats.geometric_mean(array))
print(stats.harmonic_mean(array))
print(Sort.merge_sort(array))


x = [1,2,3,1,5]
y = [1,3,5]
print(Sets.union(Sets.set(x),Sets.set(y)))

# x = [2,2,3,4,5,5,5,6,7,8,8,8,8,8,9,9,10,11,11,12]
# print(stats.percentile(x,45))
# print(stats.quartiles(x))
# print(stats.iqr(x))
