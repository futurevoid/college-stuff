def BubbleSort(list):
    Len = len(list) - 1
    Sorted = False
    for i in range(Len):
        for index in range(0, Len - i):
            if list[index] > list[index + 1]:
                Sorted = True
                list[index], list[index + 1] = list[index + 1], list[index]
        if not Sorted:
            break
    return list


List1 = [2, 16, 8, 32, 1]
print(f"sorted list:{BubbleSort(List1)}")
