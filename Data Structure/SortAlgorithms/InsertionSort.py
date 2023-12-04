def InsertionSort(list):
    for i in range(1, len(list)):
        index = i
        while index > 0 and list[index - 1] > list[index]:
            list[index - 1], list[index] = list[index], list[index - 1]
            index = index - 1
    return list


List1 = [8, 4, 16, 24, 32]
print(f"sorted list:{InsertionSort(List1)}")
