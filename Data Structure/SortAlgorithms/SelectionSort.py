def SelectionSort(list):
    Len = len(list) - 1
    for i in range(0, Len):
        min_idx = i
        for j in range(i + 1, len(list)):
            if list[j] < list[min_idx]:
                min_idx = j
        list[i], list[min_idx] = list[min_idx], list[i]
    return list


list1 = [64, 8, 32, 2, 16, 4]
print(f"Sorted List:{SelectionSort(list1)}")
