n=int(input("Enter n: "))


# Printing a Fibonacci Series
def fib(n):
    a,b=0,1
    while a<n:
        print(a,end='\n')
        a,b=b,a+b
        

# Storing a Fibonacci series in a list
def fib2(n):
    result=[]
    a,b=0,1 
    while a<n:
        result.append(a)
        a,b=b,a+b
    return result

fib(n)
print("fib2\n",fib2(n))

