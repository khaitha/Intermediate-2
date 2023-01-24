import numpy as np

randList = np.random.rand(10)

mean = np.mean(randList)

median = np.median(randList)

stdDev = np.std(randList)

print(randList)
print("Mean: ", mean)
print("Median: ", median)
print("Standard Deviation:", stdDev)