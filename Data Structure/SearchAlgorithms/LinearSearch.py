def LinearSearch(list, term):
    for i in range(len(list)):
        if list[i] == term:
            return i
    return


list1 = [3, 6, 5, 4, 7]
print(LinearSearch(list1, 5))
