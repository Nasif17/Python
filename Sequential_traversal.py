list = [1,2,3,4,5,6,7,8,9,10]
print("List elements are:")

for el in list:
    print(el)
    

tup = (1,2,3,4,5,6,7,8,9,10)
print("Tuple elements are:")

for el in tup:
    print(el)
    
print("String elements are:")
name = "Nasif"
for char in name:
    if char == "s":
        break
    print(char)
else:
        print("No character found")