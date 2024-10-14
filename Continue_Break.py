# i = 1
# while i <= 5:
#     print(i)
#     if(i==3):
#         break
#     i += 1

print("end of loop")   

i = 0
while i <= 5:
    if(i == 3):
       i += 1
       continue #skip
    print(i)
    i += 1  





print ("Only odd number")
i = 0
while i <= 20:
    if(i%2 == 0):
       i += 1
       continue #skip
    print(i)
    i += 1      
    



print ("Only even number")
i = 0
while i <= 20:
    if(i%2 != 0):
       i += 1
       continue #skip
    print(i)
    i += 1          