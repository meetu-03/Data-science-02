import numpy as np

number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
res = np.array(number, dtype=int)
print(res)
print(res.dtype)



number = [1.0, 2.4, 3.4, 4.7, 5.5, 6.5, 7.8, 8.8, 9.5]
res = np.array(number, dtype=float)
print(res)
print(res.dtype)


#OBJECT
number = [1, 2, True, 4, 5.2,"meet", 6, 7, 8, 9]
res = np.array(number, dtype=object)
print(res)
print(res.dtype)


#COMPLEX

number = [1+2j,5+9j,]
res = np.array(number, dtype=complex)
print(res)
print(res.dtype)

