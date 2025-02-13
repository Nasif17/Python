"""using for
print the elements of the following list using Loop
[1,4,9,16,25,36,49,64,81,100]"""

list = [1,4,9,16,25,36,49,64,81,100]
for i in list:
    print(i)

"""Search for a number x in this tuple using loop
[1,4,9,16,25,36,49,64,81,100]"""

tuple = (1,4,9,16,25,36,49,64,81,100)
x = 36
for i in tuple:
    if  i ==x:
        print("Numbere found")
        break
else:
    print("number not found")