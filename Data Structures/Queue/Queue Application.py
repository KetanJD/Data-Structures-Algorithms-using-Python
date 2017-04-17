#Queue Application
"""
Q) Imagine an airport check-in queue of size N, where a new passenger is
Enqueued to the check-in queue from rear end and Dequeued through
the front end. However, when the queue has number of passengers
greater than or equal to 80% of N, then Dequeue operation involves
removing passengers from front as well as rear end. In a special case,
when a passenger is a VIP, then he/she enqueued at front end instead
of rear. Implement the above data structure and operations.
"""

#CODE:

from collections import deque
n=int(input("Enter size of queue"))
p=int(input("Enter how much % queue is full"))
N=int((p*n)/100)
queue=deque()
for i in range(N):
    queue.append(int(input("Enter element :")))
def Enqueue(x,V):
    if(V=='F'):
        queue.append(x)
    elif(V=='T'):
        queue.insert(0,x)
def Dequeue(p):
    if(p<80):
        queue.popleft()
    else:
        queue.pop()
        queue.popleft()
Dequeue(p)
x=int(input("Enter the element x to be added"))
V=input("Enter if x is VIP (T/F)")
Enqueue(x,V)
print(queue)
