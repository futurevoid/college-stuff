import array as arr

arrd = arr.array("d", [1.3, 4.3, 5.5])
print(arrd)
arr2 = arr.array("i", [1, 2, 3])
arr3 = arr.array("i", [1, 2, 3])
print(arr2)
print(f"first element:{arr2[0]}")
print(f"second element:{arr2[1]}")
print(f"third element:{arr2[2]}")

arr2[0] = 4
print(arr2)

arr2[1:3] = arr.array("i", [2, 5, 8])
print(arr2)
arr2.append(9)
print(arr2)
arr2.extend([0, 6, 56])
print(arr2)

sum = arr.array("i")
sum = arr2 + arr3
print()
print(sum)

del sum[1]

print(sum)

del sum
print(sum)

print(arrd.pop(1))
print(arrd)

arrd.remove(1.3)
print(arrd)
arr2.insert(2, 3)
print(arr2)
sumr = arr2[::-1]
print(f"a {sumr}")


rows, cols = (2, 25)

print([[2, 8] * rows] * cols)
