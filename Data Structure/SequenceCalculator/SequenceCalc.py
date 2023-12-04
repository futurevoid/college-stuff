# User chooses a sequence type
sequence_type = input("Choose a sequence type (1.arithmetic or 2.geometric): ")

if sequence_type == "1":
    # User inputs parameters for the sequence
    first_term = float(input(f"Enter the first term of the arithmetic sequence: "))
    common_parameter = float(input(f"Enter the common difference: "))
    n = int(input("Enter the number of terms (n): "))
    result = n * (2 * first_term + (n - 1) * common_parameter) / 2
    print(f"The sum of the arithmetic sequence is: {result}")
elif sequence_type == "2":
    first_term = float(input(f"Enter the first term of the geometric sequence: "))
    common_parameter = float(input(f"Enter the common ratio: "))
    n = int(input("Enter the number of terms (n): "))
    if common_parameter == 1:
        result = n * first_term
    else:
        result = first_term * (1 - common_parameter**n) / (1 - common_parameter)
    print(f"The sum of the geometric sequence is: {result}")


else:
    print("Invalid sequence type. Please choose either 'arithmetic' or 'geometric'.")
