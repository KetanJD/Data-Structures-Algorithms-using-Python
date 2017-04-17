#STACK Application
#Reversing a String

""" Algorithm:
1. Push the characters of the string to an empty stack
2. Input: Computer
3. Pop the characters from stack one after another until empty
4. Output: retupmoc
"""

#CODE:

string=input("Enter a string")
stack=[]
for i in range(len(string)):
    stack.append(string[i])
print("Stack",stack[:])
reverse=[]
for i in stack[:]:
    reverse.append(stack.pop())
print("Reverse",reverse[:])
