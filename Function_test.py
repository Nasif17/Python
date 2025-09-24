"""write a function length of list (list is the parameter)"""
def list_length(lst):
    
    print("The length of the list is", len(lst))
    
list_length([1, 2, 3, 4, 5])   
list_length(['a', 'b', 'c'])
list_length(["Banana", "Apple", "Mango", "Grapes"])

Cars = ["Ford", "BMW", "Volvo"]
list_length(Cars)




"""write a fuction to print all list in a single line (list is the parameter)"""

def print_list(lst):
    for item in lst:
        print(item, end=' ')
    print()  # for newline after printing the list
    
print_list([1, 2, 3, 4, 5])
print_list(['a', 'b', 'c'])
print_list(["Banana", "Apple", "Mango", "Grapes"])
print_list(Cars)

"""write a function to find the factorial of the n (n is the parameter)"""

def factorial(n):
    
    fact = 1
    for i in range(1,n+1):
        fact *= i
    print("The factorial of", n, "is", fact)
    
factorial(5)
factorial(7) 
        
        

"""write a finction to convert USD to INR """

def converter(a,b=83):
    inr = a*b
    print(a,"USD is equal to",inr,"INR")
    
converter(10)