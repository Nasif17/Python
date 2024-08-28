student = {
    "name" : "Nasif",
    "score" : {
        "chem": 98,
        "phy": 97,
        "math":95
    }
}

print (student.keys())
print (list(student.keys()))
print (type(list(student.keys()))) #typecasting with list

print(len(student)) #printing total keys
print(len(student.keys()))

print(student.values())
print(list(student.values()))

"""we can store list in a dictonary and also
a dictonary in list"""

print(student.items()) #returns all (key,values)pairs as tuples
print(list(student.items()))

pairs = list(student.items())
print(pairs[0])
print(pairs[1])

print (student.get("name"))
print (student.get("name1")) # print ----> none

print(student["name"])
#print(student["name1"]) # print ---------> error

student.update({"city" : "Dhaka"})
print(student)

new_dict = {"age" : 22}
student.update(new_dict)
print(student) 
