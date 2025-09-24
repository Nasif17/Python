"""write a programme the sum of first n numbers(using while loop)"""
n = 0
sum = 0
while n<=7:
    sum =sum+n
   
    print("The sum of first",n+1,"numbers is",sum)
    n +=1

"""write a programme  factorial of first n numbers(using for loop)"""    
n= 5
factorial = 1
for  i in range(1,1+n):
    factorial = factorial * i
    print(" The factorial of ",i,"is",factorial)