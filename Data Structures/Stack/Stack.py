# STACK
""" Stack Definition:
It is an ordered collection of homogeneous data element where
insertion and deletion takes place at one end.
It's called Last-In-First-Out
"""

stack=[]

#Insertion
n=int(input("Enter the number of elements to be added to stack "))
for i in range(n):
    print("Enter the",i+1,"element")
    stack.append(int(input()))

#Deletion
def delete():
    print("Deleted element\t",stack.pop())


#Display
print("STACK =\t",stack[:])
print("Enter 'delete()' to pop an item from stack")
