outputStack = []
operatorStack = []

#A+B
outputStack.append('A')
print(outputStack)
operatorStack.append('+')
print(operatorStack)
outputStack.append('B')
print(outputStack)
operatorStack.pop()
print(operatorStack)
outputStack.append('+')
print(outputStack)
while outputStack:## clear output stack
    outputStack.pop()
    if not outputStack:
        break
#A-B
outputStack.append('A')
print(outputStack)
operatorStack.append('-')
print(operatorStack)
outputStack.append('B')
print(outputStack)
operatorStack.pop()
print(operatorStack)
outputStack.append('-')
print(outputStack)

while outputStack:## clear output stack
    outputStack.pop()
    if not outputStack:
        break
#A+B-C
outputStack.append('A')
print(outputStack)
operatorStack.append('+')
print(operatorStack)
outputStack.append('B')
print(outputStack)
operatorStack.append('-')
print(operatorStack)
outputStack.append('c')
print(outputStack)
operatorStack.pop()
outputStack.append("-")
print(operatorStack)
operatorStack.pop()
outputStack.append('+')
print(operatorStack)
print(outputStack)

while outputStack: ## clear output stack
    outputStack.pop()
    if not outputStack:
        break
#A*B
outputStack.append('A')
print(outputStack)
operatorStack.append('*')
print(operatorStack)
outputStack.append('B')
print(outputStack)
operatorStack.pop()
print(operatorStack)
outputStack.append('*')
print(outputStack)
while outputStack:## clear output stack
    outputStack.pop()
    if not outputStack:
        break

#(A+B)*C
operatorStack.append('(')
print(operatorStack)
outputStack.append('A')
print(outputStack)
operatorStack.append('+')
print(operatorStack)
outputStack.append('B')
print(outputStack)
operatorStack.append(')')
print(operatorStack)
operatorStack.pop()
print(operatorStack)
operatorStack.pop()
print(operatorStack)
outputStack.append('+')
print(outputStack)
operatorStack.append('*')
print(operatorStack)
outputStack.append('C')
print(outputStack)
operatorStack.pop()
print(operatorStack)
operatorStack.pop()
print(operatorStack)
outputStack.append('*')
print(outputStack)

while outputStack:## clear output stack
    outputStack.pop()
    if not outputStack:
        break

#A*(B+C)
outputStack.append('A')
print(outputStack)
operatorStack.append('*')
print(operatorStack)
operatorStack.append('(')
print(operatorStack)
operatorStack.pop(0)
print(operatorStack)
outputStack.append('*')
print(outputStack)
outputStack.append('b')
print(outputStack)
operatorStack.append('+')
print(operatorStack)
outputStack.append('c')
print(outputStack)
operatorStack.append(')')
print(operatorStack)
operatorStack.pop()
print(operatorStack)
operatorStack.pop()
print(operatorStack)
outputStack.append('+')
print(outputStack)
operatorStack.pop()
print(operatorStack)

while outputStack:## clear output stack
    outputStack.pop()
    if not outputStack:
        break