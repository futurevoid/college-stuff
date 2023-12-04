def fibonacci_search(lst, value):
    size = len(lst)

    offset = -1

    f0 = 0
    f1 = 1
    f2 = 1

    while f2 < size:
        f0 = f1
        f1 = f2
        f2 = f0 + f1

    while f2 > 1:
        index = min(offset + f0, size - 1)
        if lst[index] < value:
            f2 = f1
            f1 = f0
            f0 = f2 - f1
            offset = index
        elif lst[index] > value:
            f2 = f1
            f1 = f1 - f0
            f0 = f2 - f1
        else:
            return index
    if f1 and lst[size - 1] == value:
        return size - 1
    return "Value Not Found"


list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(fibonacci_search(list, 5))
