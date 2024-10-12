# print number 1 to 100 by using while loop 


# i = 1
# while i<=100:
#     print (i)
#     i +=1
    
#    print number 100 to 1 by using while loop 

# i = 100
# while i>=1:
#     print (i)
#     i -=1


# print the multipuication table of number n. 

# n = int(input("Enter the number you want to see the multipication table  = "))
# m = 0

# i = 1
# while i<=10:
#     m = n*i
#     print(n ,"*" ,i ," = ",m)
#     i+=1


""" print the elements of the following list using a loop:
        [1,4,9,16,25,36,49,64,81,100]"""

# i = 1
# while i<=10:
#     n = i*i
#     print(n,",")
#     i+=1


# nums = [1,4,9,16,25,36,49,64,81,100]

# i = 0
# while i<len(nums):
#     print(nums[i])
#     i+=1
    

"""Search for a number x in this tuple using loop
           [1,4,9,16,25,36,49,64,81,100]"""
           
           

nums = (1,4,9,16,25,36,49,64,81,100)
x = 36
i = 0
while i<len(nums):
    if (nums[i]==x):
        print("Found in index ",i,nums[i]) 
        break 
    i+=1
               
               
          