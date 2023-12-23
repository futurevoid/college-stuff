import array as arr
import array as arrd

arr = arr.array("i", [2, 4, 6, 8])
print(arr)

print(f"first element: {arr[0]}")
print(f"second element: {arr[1]}")
print(f"third element: {arr[2]}")
print(f"first to third element: {arr[0:2]}")

for i in arr:
    print(i)

for pnt in range(4):
    print(f"index:{pnt} {arr[pnt]}")

arr.reverse()
print(arr)

print(arr[2])
print(arr.index(2))

arr.append(3)

arr1 = arrd.array("i", [])
size = int(input("enter the size of the array:"))
print("enter %d elements:" % size)
for i in range(size):
    elements = int(input())
    arr1.append(elements)

print(arr1)
