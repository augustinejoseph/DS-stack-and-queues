# DS-Stack and Queues

## What are they?
>Stacks and queues are two types of data structure used to store and retrieve data from memory.

1. stack: A stack is a collection of elements that can be accessed in a LIFO manner(Last In First Out). That means, the latest addiions to the stacks are accessed first.
2. Queues: A queue is similar to stack, but follows the FIFO method. Here the first inserted elements are removed first and the last inserted elements are removed last.
---
<br />

## Uses of stack and queues

### Stack
1. **Undo/Redo functionality:**
A stack can be used to store the sequence of actions performed by a user in an application. When the user clicks "undo," the most recent action is popped off the stack and reversed.

2. **Back/Forward stacks on browsers:**
A stack can be used to store the order of webpages opened in a tab. when the user clicks the back button, the page behind the latest webpage is displayed

### Queue
1. **Job scheduling:**
A queue can be used to manage the list of tasks to the completed. When a new job is added, it is added to the queue and when the resources are available, it is processed. 
2. **Printer spooling:**
When multiple requests are send to a printer from multiple sources, the printer queues each request in the order it is recieved. After completing the first request, the printer prints the next one in a order.
3. **Breadth-first search:** 
A queue is used to implement the breadth-first search algorithm in graph theory. Starting with a root node, all of its neighbors are added to the queue. Then, for each neighbor in the queue, all of their neighbors are added to the queue, and so on, until all nodes have been visited. This ensures that nodes are visited in the order of their distance from the root node.

---
<br />

## How to implement stack and queue in python
### stack:
1.**Using List:** In python, list can be used to show the working of stack. In list, <code>append()</code> is used to insert element into the end of the list and <code>pop()</code> is used to remove the last element from the list. The time complexity is <code>O(1)</code>

```python
# Adding an element to stack
stack = [1,2]
stack.append(3)
print(stack)
# output : [1,2,3]
```
```python
# Removing an element from stack
stack = [1,2,3]
stack.pop()
print(stack)
# Output : [1,2]
```

### Queue:
1. **Using List:**  Pyhton List can be used for the implementation of queue. Here, the <code>append()</code> is used to add element and <code>pop(0)</code> is used to remove the first element. 0 shows the index posistion
```python
# Creating a queue
queue = ['Amar, Akbar']
queue.append("Antony")
print(queue)
# output : [Amar, Akbar, Anthony]
```
```python
# Removing first element
queue1 = ['Amar', 'Akbar', 'Antony']
queue1.pop(0)
print(queue1)
#  output : ['Akbar', 'Antony']
```
2. **Using Deque:** In queue, the above list implementation takes more time as compared with deque. Lists in Python have a time complexity of O(1) for adding elements to the end of the list using the append method, but a time complexity of O(n) for inserting elements at arbitrary positions using the insert method. <br>
On the other hand, deques in Python provide O(1) time complexity for adding and removing elements from both the front and back of the deque using the popleft, pop, appendleft, and append methods. This makes deques a more efficient choice for implementing queues in situations where elements need to be added or removed from both ends of the queue.<br>
Furthermore, deques in Python are implemented as doubly-linked lists, which means that elements can be efficiently accessed from either end of the deque. This provides additional flexibility in implementing certain algorithms and data structures that require access to elements from both ends of a collection.
```python
# Enqueue
from collections import deque
dq = deque([1,2,3])
dq.append(4)
dq.appendleft(0)
print(dq)
# output : deque([0, 1, 2, 3, 4])
```
```python
# Dequeue
from collections import deque
dq = deque([0,1,2,3,4])
dq.pop()
print(dq)
dq.popleft()
print(dq)
# output : deque([1, 2, 3])
```
```python
# Acess element by value
from collections import deque
dq = deque([0,1,2,3,4])
print(dq.index(3))
# output : 3
# element 3 is in third index posistion
```
```python
# Delete element
from collections import deque
dq = deque([0,1,2,3,4])
dq.remove(2)
print(dq)
# output : [0,1,3,4]
# The element 2 is removed
```

<br />
<hr>



