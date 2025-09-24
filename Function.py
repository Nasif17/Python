# Function Defination
def Calc_sum (a,b):  #parameters
    sum=a+b
    print("The sum of two numbers is",sum)

Calc_sum(5,10)  #arguments or function call
Calc_sum(20,30)


def print_hello():
    print("Hello, World!")

print_hello()


#Average of 3 numbers
def average (x,y,z):
    avg = (x+y+z)/3
    print("The average of three numbers is",avg)

average(99,97,90)

#defult parameter
def defult_para(a=1,b=2):
    Mul= a*b
    print("The multiplication is",Mul)
defult_para()
defult_para(5,5)