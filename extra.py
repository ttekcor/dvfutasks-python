import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt
# N = int(input())
# y = list(map(float,(input().split(" "))))
# nums = list(range(1, int(N) + 1))
# x1 = np.arange(0,N)
# f = interpolate.interp1d(nums, y, fill_value='extrapolate')
# print(f(N+1))
data = np.array([[1,5], [2,10], [3,15], [4,20], [5,25]])
fit = np.polyfit(data[:,0], data[:,1] ,1) #The use of 1 signifies a linear fit.

line = np.poly1d(fit)
new_points = np.arange(5)+6
print(new_points)
print(line)
print(fit)
line(new_points)
plt.plot(line)
plt.show()