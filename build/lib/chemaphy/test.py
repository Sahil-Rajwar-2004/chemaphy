                                        ## TEST ##



# from __init__ import Sets

# x = Sets.set([1,1,2,3,5])
# y = Sets.set([1,5,2])
# print(x,y)
# print(Sets.union([1,1,2,3,5],[1,2,5,2]))
# print(Sets.intersect(x,y))
# print(Sets.belongsto(x,3,idx=False))
# print(Sets.belongsto(x,3,idx=True))
# print(Sets.subset(x,y))
# print(Sets.subset(y,x))
# print(Algorithm.fibonacci_series(10))

# x = [8,2,6,4,0,3,5,1,7,9]

# print(Sort.bubble_sort(x))
# print(Sort.insertion_sort(x))
# print(Sort.merge_sort(x))
# print(Sort.quick_sort(x))

# import pandas as pd

# array = [1,2,3,7,9]
# data = pd.Series(array)
# moving_averages = round(data.ewm(alpha=0.2, adjust=False).mean(), 2)
# moving_averages_list = moving_averages.tolist()

# print(stats.moving_avg([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],3))
# print(stats.exp_moving_avg([1,2,3,7,9],0.2))

# arr = [1,2,3,7,9]
# x=0.2

# i = 1
# moving_averages = []
# moving_averages.append(arr[0])

# while i < len(arr):
#     window_average = round((x*arr[i])+(1-x)*moving_averages[-1], 2)
#     moving_averages.append(window_average)
#     i += 1
  
# print(moving_averages)
# print(moving_averages_list)