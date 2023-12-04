def evaluate_postfix(expression):
    stack = []

    # Function to perform basic arithmetic operations
    def perform_operation(operator, operand1, operand2):
        if operator == "+":
            return operand1 + operand2
        elif operator == "-":
            return operand1 - operand2
        elif operator == "*":
            return operand1 * operand2
        elif operator == "/":
            return operand1 / operand2
        else:
            raise ValueError(f"Unsupported operator: {operator}")

    # Iterate through each character in the postfix expression
    for char in expression:
        if char.isdigit():
            # If the character is a digit, push it onto the stack
            stack.append(int(char))
        elif char in ["+", "-", "*", "/"]:
            # If the character is an operator, pop two operands from the stack
            operand2 = stack.pop()
            operand1 = stack.pop()
            # Perform the operation and push the result back onto the stack
            result = perform_operation(char, operand1, operand2)
            stack.append(result)
        elif char == "(":
            # If the character is an open parenthesis, push it onto the stack
            stack.append(char)
        elif char == ")":
            # If the character is a close parenthesis, pop and evaluate until an open parenthesis is encountered
            while stack[-1] != "(":
                operator = stack.pop()
                operand2 = stack.pop()
                operand1 = stack.pop()
                result = perform_operation(operator, operand1, operand2)
                stack.append(result)
            # Pop the open parenthesis from the stack
            stack.pop()
        else:
            raise ValueError(f"Invalid character in the expression: {char}")

    # The final result is on the top of the stack
    return stack.pop()


# Example usage:
postfix_expression = input("postfix expression:")
result = evaluate_postfix(postfix_expression)
print(f"Result of postfix expression '{postfix_expression}': {result}")
