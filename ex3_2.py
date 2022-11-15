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

stack.append('F')
print(stack)
stack.append('E')
print(stack)
stack.append('D')
print(stack)
stack.append('C')
print(stack)
stack.append('B')
print(stack)
stack.append('A')
print(stack)