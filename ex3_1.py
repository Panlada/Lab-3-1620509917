# Python program to
# demonstrate stack implementation
# using list
# Part1 ##################################################################################################################################################################################
from queue import Empty


stack = []

# append() function to push
# element in the stack
stack.append('A')                                             
print(stack)
stack.append('B')     
print(stack)
stack.append('C')     
print(stack)
stack.append('D')
print(stack)
stack.append('E')
print(stack)
stack.append('F')
print(stack)

while stack:
    stack.pop()
    print(stack)
    if not stack:
        break


# Part2 ##################################################################################################################################################################################
stack1 =[]
stack1.append('A')
print(stack1)
stack1.append('B')
print(stack1)
stack1.append('C')
print(stack1)
stack1.append('D')
print(stack1)
stack1.append('E')
print(stack1)
stack1.append('F')
print(stack1)

while stack1:
    stack1.pop(0)
    print(stack1)
    if not stack1:
        break
