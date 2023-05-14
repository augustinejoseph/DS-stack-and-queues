
from collections import deque
dq = deque([1,2,3])
# Enqueue
dq.append(4)
dq.appendleft(0)
print(dq)


# Dequeue
dq.pop()
print(dq)
dq.popleft()
print(dq)

# Acess element by value
print(dq.index(3))

# Delete element
dq.remove(2)
print(dq)


