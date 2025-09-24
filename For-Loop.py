"""print numbers from 1 to 100 using for loop and range function"""

for i in range (1,101):
    print(i)
    

"""print numbers from 100 to 1 using for loop and range function"""    
for j in range (100,0,-1):
    print(j)
    
"""print the multipication table of a number n using for loop and range function"""    

n=int (input("Enter the number you want the multiplication table of : "))
for k in  range(1,11):
    print(n,"X",k,"=",n*k)