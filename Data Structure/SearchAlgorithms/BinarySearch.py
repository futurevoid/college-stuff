import sys

sys.setrecursionlimit(1000000000)


def BinarySearch(lst, high, low, x):
    if high >= low:
        mid = (high + low) // 2
        if lst[mid] == x:
            return mid
        elif lst[mid] < x:
            return BinarySearch(lst, mid + 1, low, x)
        elif lst[mid] > x:
            return BinarySearch(lst, high, mid - 1, x)
    else:
        return -1


lst1 = [4, 8, 16, 24, 32]
x = 1
result = BinarySearch(lst1, len(lst1) - 1, 0, x)
if result != -1:
    print(f"the element present at the index {result}")
else:
    print("the element doesn't exist in the list")
