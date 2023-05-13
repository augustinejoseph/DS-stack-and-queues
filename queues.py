
from collections import deque
dq = deque([1,2,3])
# Enqueue
dq.append(5)
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


# # Queue operations in simple pyhton list
# queue = [1,2,3,4,5]
# print(queue)
# # Enqueue
# queue.append(6)
# print(queue)
# # Dequeue
# queue.pop(0)
# print(queue)