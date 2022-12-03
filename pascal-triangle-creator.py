num_of_rows = int(input("Enter the number of rows:"))  
for nums in range(num_of_rows):  
    print(' '*(num_of_rows-nums), end='')   
    print(' '.join(map(str, str(11**nums))))  