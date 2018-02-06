import numpy as np

def mean(array):
    for value in array:
        length = len(array)
        sum = 0
        sum = sum + int(value[:])
        mean = 0
        mean = sum / length
    return mean

l = [1, 3, 5]
#
# areaMean = mean(l)
# print(areaMean)
#
# mean = float(sum(l)) / float(len(l))
# print(mean)

print(np.mean(l))