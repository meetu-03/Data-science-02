import numpy as np

number = [1, 2,3, 4, 5, 6, 7, 8, 9]
res = np.array(number, dtype=int)
print(res)
print(res.dtype)
print(number[2])


#additions via index


number = [1, 2, True, 4, 5.2,"meet", 6, 7, 8, 9]
res = np.array(number, dtype=object)
print(res)
print(res.dtype)
print(number[1] + number[2])