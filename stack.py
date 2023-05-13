stack = [1,2,3,4,5]
print(stack)

# Adding an element to stack
stack.append(1)
print(stack)

# Removing an element from stack
stack.pop()
print(stack)


# Print stack
for item in stack:
    print(item)

# Remove specific
def removeSpecific(value):
    sec = [100]
    while item in stack:
        if item == value:
            print("isnide  print",item)
            stack.pop(item)
        else:
            stack.pop(item)
            sec.push(item)
    print(stack)

removeSpecific(3)