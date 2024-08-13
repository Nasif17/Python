#Write a programme to chack if a number entered by user is odd or even.

num = int (input("Enter your number : "))

if(num%2==0):
    print("Even Number")
    
else:
    print("Odd Number")    

#write a programme to find the greatest of 3 numbers entered by user

num1 = int(input("Enter your first number : "))
num2 = int(input("Enter your second number : "))
num3 = int(input("Enter your third number : "))

if (num1<num2):
    if(num2<num3):
        print(num3," is the greatest")
    else:
        print(num2, " is the greatest")
else:
    print(num1, " is the greatest")   

if (num1 >= num2 and num1 >= num3):
    print("first number is the leargest")
    
elif(num2 >= num3):
    print("Second number is the leargest")

else:
    print("third number is the largest")        
 
 
# Write a programme to check if a number is a multiple of 7 or not         
x = int (input("Enter your number: "))

if(x%7==0):
    print(True)
else:
    print(False)             