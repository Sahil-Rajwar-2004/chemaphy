# import chemaphy
# from chemaphy import ProjectileMotion as pm
# from chemaphy import LogicGates as lg
# from chemaphy import ModernPhysics as mp
# from chemaphy import Statistics
# from chemaphy import Temperature
# import pandas as pd
# import pandas_datareader as pdr
# from chemaphy import BinaryConverter
# from chemaphy import Statistics as stats
# import numpy as np
# from chemaphy import Statistics as stats

# x = [1,2,3,4,5,6,7,8,9,0]
# y = [2,3,4,4,5,6,7,8,9,1]

# print(stats.MeanSquaredError(x,y))
# print(stats.RootMeanSquaredError(x,y))

#import pandas as pd
#raw = {
#        "a":[1,2,3,4,5,6,7,8,9,0],
#        "b":[1,4,9,16,25,36,49,64,81,0],
#        "c":[0,9,8,7,6,5,4,3,2,1]
#       }

#df = pd.DataFrame(data = raw)

#print(stats.RandomSamplingData(data = df,fraction = 0.5))
#print(stats.RandomSamplingList(args = [1,2,3,4,5,6,7,8,9,0],sample = 5))

# from chemaphy import Algorithm as algo
# print(algo.Prime(1,10))
# print(algo.Sort([9,2,5,3,1,0,4,8,7,6]))
# print(algo.Length([1,2,3,4,5,6,7,8,9,0]))


# print(type(x),type(y))
# print(stats.MeanAbsoluteError(x,y))
# print(stats.StandardError(x))
# print(stats.Divide(x,y))


# print(stats.Slope(a,b))
# print(stats.Intercept(a,b))
# print(stats.LR(a,b))

# from chemaphy import Graphs
# from chemaphy import LoadData

# data = LoadData.load_data("elements")
# x = data["AtomicNumber"]
# y = data["AtomicMass"]
# Graphs.plot(x,y,x_label="Atomic Number",y_label="Atomic Mass",title="Title", yscale = "log", xscale="linear",style_="dark_background")
# Graphs.scatter(x,y,x_label="Atomic Number",y_label="Atomic Mass",title="Title", yscale = "log", xscale="linear",style_="dark_background")





# print(stats.Mean([1,2,3,4,5]))
# a = np.array([1,2,3,3])
# b = np.array([[1,2,3],[4,5,6]])
# print(a)
# print(b)
# print(np.ravel(b,order = "C"))
# print(np.ravel(b,order = "F"))
# print(np.ravel(b,order = "A"))
# print(np.ravel(b,order = "K"))


# from chemaphy import PeriodicTable as pt

# print(pt.element("chlorine")






# print(stats.Subtract([1,2,3,4],[1,2,3,4]))
# print(stats.Add([1,2,3,4],[1,2,3,4]))
# print(stats.Multiply([1,2,3,4],[1,2,3,4]))
# print(stats.Divide([1,2,3,4],[1,2,3,4]))

# print(stats.MinMax([23,63,73,82,39,12,57]))


# print(stats.Count([1,2,3,4,5,6,7,8,9,0]))

# from chemaphy import Stack

# put = Stack()
# put.push(2)
# put.push(3)
# put.push("Sahil")
# put.push(100)
# print(put)
# put.pop()
# print(put.peek())




# rel1 = [375, 211, 23, 39, 118, 97, 971, 702, 143, 9]
# rel2 = sorted(rel1,reverse = False)
# rel3 = [3,4,2,1,7,0,9,6,5,8,1,12]
# rel = [5,8,15,29,10,18,3,12,6,14,11]
# rel4 = [534, 564, 969, 742, 873, 824, 707, 789, 905, 789,200,300,1,2,3,4,5,6,7,8,9,0]

# rel = [113, 26, 391, 976, 65, 880, 575, 682, 892, 873, 745, 661, 783, 520, 531, 57, 316, 610, 404, 425, 170, 321, 623, 368, 705, 451, 947, 945, 772, 250, 79, 221, 412, 248, 991, 248, 118, 759, 47, 679, 646, 200, 490, 761, 458, 33, 77, 886, 127, 535, 783, 695, 610, 755, 572, 11, 406, 552, 439, 351, 841, 571, 330, 64, 252, 223, 792, 405, 543, 785, 591, 717, 93, 939, 265, 951, 383, 228, 363, 407, 41, 728, 127, 272, 636, 716, 184, 292, 
# 635, 164, 614, 203, 394, 660, 789, 620, 274, 667, 548, 215, 335, 898, 702, 279, 678, 785, 546, 533, 959, 751, 647, 962, 972, 745, 904, 671, 420, 571, 330, 866, 908, 21, 609, 449, 324, 821, 477, 479, 522, 37, 716, 469, 897, 537, 386, 918, 861, 684, 70, 139, 783, 572, 555, 81, 833, 909, 537, 538, 102, 646, 55, 758, 534, 613, 601, 274, 642, 819, 417, 451, 458, 996, 805, 205, 975, 881, 455, 386, 576, 782, 601, 976, 613, 190, 911, 
# 251, 82, 565, 38, 613, 493, 729, 316, 46, 608, 370, 430, 188, 535, 501, 152, 884, 125, 574, 61, 436, 891, 202, 520, 112, 683, 213, 419, 689, 807, 872, 944, 284, 396, 702, 988, 265, 26, 912, 415, 163, 395, 991, 322, 
# 0, 202, 380, 667, 597, 30, 983, 292, 673, 36, 646, 966, 79, 271, 904, 141, 166, 608, 24, 473, 895, 78, 643, 888, 181, 512, 350, 367, 956, 564, 134, 870, 986, 872, 88, 225, 277, 0, 232, 957, 728, 657, 705, 35, 89, 314, 970, 920, 470, 39, 540, 810, 734, 310, 481, 641, 236, 510, 236, 405, 528, 478, 174, 437, 953, 710, 805, 579, 27, 118, 923, 310, 499, 677, 894, 757, 288, 123, 535, 379, 217, 118, 615, 889, 655, 209, 220, 861, 63, 
# 241, 357, 716, 418, 979, 145, 813, 458, 709, 497, 334, 459, 280, 830, 883, 154, 577, 221, 480, 452, 949, 625, 806, 768, 540, 411, 476, 49, 67, 672, 577, 182, 285, 818, 481, 146, 924, 237, 49, 577, 123, 522, 225, 893, 226, 278, 588, 614, 434, 202, 501, 465, 502, 786, 189, 883, 705, 127, 653, 1, 314, 247, 161, 604, 116, 240, 284, 260, 993, 625, 655, 973, 849, 928, 311, 676, 177, 623, 219, 211, 781, 630, 558, 826, 816, 605, 984, 
# 699, 948, 737, 87, 754, 440, 310, 755, 155, 751, 245, 600, 448, 863, 932, 982, 774, 674, 34, 291, 677, 698, 377, 205, 115, 900, 296, 527, 139, 233, 27, 356, 652, 821, 811, 610, 481, 947, 628, 230, 792, 782, 210, 745, 640, 571, 773, 990, 289, 823, 979, 597, 528, 407, 602, 399, 111, 541, 314, 32, 562, 116, 688, 364, 834, 40, 541, 265, 39, 148, 714, 630, 507, 768, 832, 437, 704, 716, 5, 255, 952, 924, 78, 462, 942, 638, 440, 69, 
# 788, 103, 281, 896, 993, 285, 177, 322, 125, 425, 334, 358, 586, 767, 654, 873, 911, 19, 608, 956, 562, 73, 579, 804, 464, 801, 102, 819, 399, 163, 85, 570, 594, 857, 819, 212, 775, 237, 891, 888, 156, 32, 98, 626, 
# 762, 830, 721, 864, 255, 369, 216, 923, 175, 500, 555, 790, 482, 179, 53, 260, 948, 644, 709, 232, 948, 984, 506, 194, 481, 35, 727, 174, 3, 80, 885, 137, 833, 734, 776, 924, 776, 415, 519, 197, 830, 652, 428, 806, 
# 533, 323, 355, 247, 296, 753, 85, 522, 477, 374, 736, 516, 413, 529, 305, 226, 536, 648, 368, 69, 655, 429, 6, 601, 542, 80, 79, 23, 902, 227, 325, 701, 930, 991, 536, 894, 201, 298, 48, 549, 986, 897, 626, 684, 299, 881, 861, 350, 514, 767, 887, 500, 516, 98, 733, 867, 199, 134, 660, 182, 21, 367, 405, 373, 602, 549, 853, 149, 36, 159, 849, 75, 154, 497, 170, 574, 275, 711, 524, 200, 10, 836, 610, 180, 603, 688, 322, 376, 318, 509, 651, 514, 216, 675, 120, 919, 525, 567, 764, 21, 176, 412, 432, 56, 391, 951, 988, 591, 56, 73, 997, 802, 844, 410, 12, 824, 148, 279, 206, 210, 670, 434, 703, 677, 539, 205, 13, 796, 150, 209, 290, 180, 631, 510, 391, 790, 868, 277, 764, 160, 70, 635, 589, 663, 630, 946, 847, 776, 224, 341, 482, 872, 669, 40, 50, 658, 679, 603, 846, 654, 828, 2, 371, 925, 26, 936, 963, 451, 581, 83, 906, 887, 903, 306, 211, 191, 706, 248, 515, 431, 5, 208, 45, 734, 63, 337, 200, 11, 140, 180, 526, 338, 302, 362, 990, 412, 445, 633, 698, 916, 474, 382, 913, 169, 2, 217, 51, 516, 838, 77, 786, 698, 274, 362, 626, 8, 482, 794, 681, 968, 190, 246, 770, 530, 147, 893, 229, 352, 157, 628, 173, 926, 543, 983, 4, 396, 246, 875, 190, 215, 52, 57, 947, 208, 685, 598, 569, 142, 401, 384, 578, 759, 503, 834, 720, 972, 935, 552, 302, 688, 190, 779, 792, 912, 346, 17, 880, 555, 739, 852, 799, 701, 179, 183, 459, 190, 943, 737, 342, 578, 132, 333, 223, 446, 378, 261, 286, 57, 390, 242, 226, 952, 319, 192, 764, 585, 190, 91, 0, 372, 922, 474, 152, 152, 820, 532, 507, 962, 612, 67, 562, 966, 72, 328, 218, 361, 979, 351, 374, 954, 979, 76, 358, 876, 510, 411, 339, 989, 597, 902, 875, 302, 260, 354, 293, 101, 38, 640, 92, 994, 242, 911, 829, 659, 23, 868, 743, 428, 538, 889, 575, 372, 989, 913, 893, 20, 922, 399, 933, 977, 318, 787, 20, 231, 185, 648, 974, 324, 693, 48, 412, 0, 202, 577, 72, 81, 879, 640, 410, 202, 283, 175, 949, 239, 244, 763, 946, 870, 396, 100, 528, 110, 563, 605, 420, 15, 69, 724, 631, 985, 419, 873, 129, 975, 804, 899, 520, 412, 439, 911, 69, 851, 4, 523, 266, 590, 573, 927, 296, 145, 823, 684, 729, 409, 268, 137, 350, 5]

# rel1 = [375, 211, 23, 39, 118, 97, 971, 702, 143, 9]

# company = "MSFT"

# data = pdr.get_data_yahoo(company).tail(1000)
# print(data.describe())

# print(Statistics.Quartiles(data.Close))
# print(Statistics.Outliers(data.Close))

# print(Temperature.c2k(300))
# print(Temperature.c2f(300))
# print(Temperature.k2c(27))
# print(Temperature.k2f(27))
# print(Temperature.f2c(27))
# print(Temperature.f2k(27))



# print(BinaryConverter.str2binary("Hello"))
# print(BinaryConverter.str2hexadecimal("Hello"))
# print(BinaryConverter.str2octadecimal("Hello"))

# print(BinaryConverter.int2binary([1,2,3,4,5]))
# print(BinaryConverter.int2binary(5))

# print(BinaryConverter.int2hexadecimal([1,2,3,4,5,222,111]))
# print(BinaryConverter.int2hexadecimal(5))

# print(BinaryConverter.int2octadecimal([1,2,3,4,5]))
# print(BinaryConverter.int2octadecimal(5))










# print(Quartiles(data.Close))
# print(len(rel1))
# Q(rel)
# print(Statistics.Quartiles(rel1))
# print(IQR(rel4))
# print(Outliers(rel))
# print(MedianAvgDeviation(rel1))
# print(MedianAvgDeviation(rel2))
#print(Permutations(6,6))
# print(Mean([1,2,3,4,5,6,7,8,9,0]))
# print(Median([1,2,3,4,5,6,7,8,9,0]))
# print(ZScore([1,2,3,4,5,6,7,8,9,0],10))
# print(StandardDeviation([1,2,3,4,5,6,7,8,9,0]))
# rel1 = [7, 23, 19, 35, 25, 5, 42, 10, 0, 41, 2, 20, 20, 11, 40, 5, 43, 17, 1, 3, 24, 28, 7, 7, 24, 46, 15, 42, 47, 48, 26, 19, 13, 8, 50, 43, 20, 12, 24, 22, 4, 39, 12, 46, 7, 38, 35, 14, 45, 38, 28, 40, 22, 36, 31, 9, 11, 39, 11, 11, 31, 28, 44, 3, 15, 35, 4, 30, 20, 12, 39, 4, 2, 40, 41, 47, 47, 20, 13, 19, 32, 22, 31, 23, 9, 39, 14, 16, 38, 41, 12, 40, 5, 49, 29, 4, 40, 28, 10, 36]
# rel2 = [39, 40, 46, 15, 42, 9, 45, 31, 13, 29, 31, 2, 1, 12, 47, 40, 7, 2, 2, 27, 38, 5, 21, 40, 31, 25, 32, 1, 36, 1, 45, 9, 50, 36, 32, 41, 47, 20, 46, 4, 24, 34, 21, 38, 44, 17, 32, 39, 38, 40, 35, 19, 49, 15, 32, 36, 34, 16, 42, 2, 23, 14, 0, 43, 9, 29, 44, 21, 21, 30, 47, 46, 15, 8, 47, 39, 5, 18, 18, 41, 4, 41, 13, 1, 17, 49, 13, 32, 21, 36, 45, 31, 50, 32, 13, 27, 50, 39, 0, 32]
# lr = Statistics.LR(rel1,rel2)
# print(lr)
# print(Quartiles([34,24,43,5,58,81,29,90,22,67,32,88,57,34,43,44,91,24,62]))
# print(Quartiles([8,10,9,7,7,9,11,11,12,13,11,10,9,9,10]))
# print(Factorial(5))
# print(FibonacciSeries(5))
#  print(Combinations(10,2))
# print(Permutations(10,2))
# print(PopulationVariance([1,3,5,7]))
# print(SampleVariance([1,3,5,7]))
# print(MeanDeviation([1,2,3,4,5,6,7,8,9,0]))
# print(MedianAvgDeviation([1,2,3,4,5,6,7,8,9,0]))
# rel = [56, 49, 74, 35, 19, 71, 63, 59, 64, 97, 21, 88, 90, 87, 96, 13, 86, 17, 25, 11]
# for i in range(0,20):
#     a = random.randint(0,100)
#     rel.append(a)
# print(rel)
# print(Percentile(rel,21))
# print(CumSum([1,2,3,4,5]))
# print(numpy.cumsum([1,2,3,4,5]))
# print(RunningMean([1,2,3,4,5,6,7,8,9,0]))
# print(GeometricMean([10, 25, 5, 30]))
# print(HarmonicMean([6,2,5,3]))
# print(CorrelationCoefficient([4, 1, 2, 4, 5, 1, 5, 7, 9, 0, 5, 3, 2, 5, 9, 5, 2, 3, 0, 8],[5, 10, 15, 20,10, 12, 16, 21, 25,10,8,10,8,8,4,1,2,3,4,5]))
# print(CoefficientDetermination([2,4,3,1],[6,2,5,3]))
# print(Product([1,2,3,4,5,-2]))
# x = [43,21,25,42,57,59]
# y = [99,65,79,75,87,81]
# print(LR(x,y))
# print(RMS([5,4,8,1]))
# print(RelativeFrequency([4, 1, 2, 4, 5, 1, 5, 7, 9, 0, 5, 3, 2, 5, 9, 5, 2, 3, 0, 8]))
# print(Mean([10, 12, 16, 21, 25]))
# print(mode([2,1,2,1]))
# print(StandardDeviation([10, 12, 16, 21, 25]))
# print(StandardError([10, 12, 16, 21, 25]))
# print(Variance([10,8,10,8,8,4]))
# print(Median([1,2,3,4]))
# print(func([1,2,3,4,5,6,7,8,9,10]))
# print(statistics.stdev([10,8,10,8,8,4]))
# print(pm.horizontal_range(100,chemaphy.g_Earth.value,30))
