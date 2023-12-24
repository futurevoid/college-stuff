import numpy as np

narr1 = [1, 4, 7, 9]
narr2 = [6, 1, 1, 4.5]

arr = np.array([narr1, narr2])
print(arr)

div = arr[0] / arr[1]
print(div)
print(type(div))

arr = np.append(arr, [div], axis=0)
print(arr)

d1 = np.array([100])
d2 = np.array([[100, 200], [300, 400]])
d3 = np.array([[[100, 200], [225, 250]], [[300, 400], [450, 475]]])
print(d3[1, 0, 1])
print(d1.ndim)
print(d2.ndim)
print(d3.ndim)

print(d3[:2, :2:2])

arr2x25 = np.arange(start=1, stop=51).reshape(2, 25)
print(arr2x25)

for pntr in range(0, 2):
    for ptr in range(9, 25):
        print(arr2x25[pntr][ptr])
