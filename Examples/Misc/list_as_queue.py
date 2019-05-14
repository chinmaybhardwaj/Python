
#
# Using Lists as Queues
#
from collections import deque

queue = deque(['A', 'B', 'C'])
print(queue)
# insert into queue
queue.append('D')
queue.append('E')
#
print(queue)

# pop from queue
queue.popleft()
print(queue)
#
queue.popleft()
print(queue)
#
queue.popleft()
print(queue)
