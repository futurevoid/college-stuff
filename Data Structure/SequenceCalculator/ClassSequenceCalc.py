class SequenceCalc:
    # Function to calculate the sum of an arithmetic sequence
    def calculate_arithmetic_sum(self, first_term, common_difference, n):
        return n * (2 * first_term + (n - 1) * common_difference) / 2

    # Function to calculate the sum of a geometric sequence
    def calculate_geometric_sum(self, first_term, common_ratio, n):
        if common_ratio == 1:
            return n * first_term
        else:
            return first_term * (1 - common_ratio**n) / (1 - common_ratio)


# Main function
def main():
    calc = SequenceCalc()
    # User chooses a sequence type
    sequence_type = int(input("Choose a sequence type (1. Arithmetic, 2. Geometric): "))

    if sequence_type == 1:
        # User inputs parameters for arithmetic sequence
        first_term = float(input("Enter the first term of the arithmetic sequence: "))
        common_difference = float(input("Enter the common difference: "))
        n = int(input("Enter the number of terms (n): "))
        result = calc.calculate_arithmetic_sum(first_term, common_difference, n)
        print(f"The sum of the arithmetic sequence is: {result}")

    elif sequence_type == 2:
        # User inputs parameters for geometric sequence
        first_term = float(input("Enter the first term of the geometric sequence: "))
        common_ratio = float(input("Enter the common ratio: "))
        n = int(input("Enter the number of terms (n): "))
        result = calc.calculate_geometric_sum(first_term, common_ratio, n)
        print(f"The sum of the geometric sequence is: {result}")

    else:
        print("Invalid choice. Please enter either 1 or 2.")


# Execute the main function if the script is run
if __name__ == "__main__":
    main()
