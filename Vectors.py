import numpy as np

val = np.array([1,2,3,4,5,6])

#Prints every element in the next line
for i in range(0,6):
    print(val[i])

#Prints every elements of the array in the same line
for i in range(0,6):
    print(val[i], end=" " if i < 5 else "\n")

#Experimenting with dtype

val_str = np.array(['str', 'str1', 'str2'])
print(val_str.dtype)
print(val.dtype)

print(np.flip(val))

print(np.insert(val, 1, [50]))

print(np.append(val, [7, 8]))