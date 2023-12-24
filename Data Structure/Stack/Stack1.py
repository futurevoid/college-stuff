from Stack import *

stack1 = Stack()

s1 = stack1

s1.empty()

s1.push(16)

s1.push(True)

s1.push(16.7)

s1.push("abo obaidah amk")

print("\nThe stack elements are:")
s1.printstack()

print(f"\n{s1.size()} is the size of the stack\n")

print(f"{s1.peek()} is the top value\n")

print(f"{s1.pop()} is popped")

print("\nThe updated stack elements are:")

s1.printstack()
