# import numpy as n
# arr=n.array([1,2,3])
# print("min",n.max(arr),"\t")
# print("max",n.min(arr),"\t")
# print("sum2",n.sum(arr))
# print("mean",n.mean(arr))
# print(arr+10,arr-1,arr*2,arr/2)

import numpy as np
arr=np.array([1,2,3,4,5,6,7,8,9,10])
print(np.sum(arr))
print(np.average(arr))
print(arr*5)
print(np.min(arr),np.max(arr))
print(arr[arr>5])