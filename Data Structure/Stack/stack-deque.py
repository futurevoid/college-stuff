from collections import deque

numbers = deque()

numbers.append(99)
numbers.append(15)
numbers.append(82)
numbers.append(50)
numbers.append(47)

numbers = list(numbers)
print(f"the elements of the stack are: {numbers}")


if numbers:
    deleted_element = numbers.pop()
    print(f"deleted element from the stack: {deleted_element}")


try:
    print(f"the updated elements of the stack : {numbers}")
except NameError:
    print("the stack is empty")
