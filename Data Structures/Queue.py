#Queue
"""
It is an ordered collection of
homogeneous data element where
the insertion and deletion take place
at two different ends.
It is called a First-in-First-Out (FIFO)
collection.
"""

from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("KJD")
print(queue)
print(queue.popleft())


    
    
