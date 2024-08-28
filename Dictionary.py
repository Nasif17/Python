dict = {
    "name" : "Nasif",       # string
    "Cgpa" : 3.7,              #float
    "marks" : [98 , 97 , 95],      #list
    "age" : 22,                   #integer
    "is_adult" : True,           #boolean
    "topics" : ("dict","set")     #tuples
 }

print (dict)
print(type(dict))

print (dict["name"])
print (dict["Cgpa"])
print (dict["marks"])
print (dict["age"])
print (dict["is_adult"])
print (dict["topics"])


print (type(dict["name"]))
print (type(dict["Cgpa"]))
print (type(dict["marks"]))
print (type(dict["age"]))
print (type(dict["is_adult"]))
print (type(dict["topics"]))

dict["name"] = "Rafidi"
dict["lastname"] = "Nasif"
print(dict)

null_dict = {} # empty  dictonary
print(null_dict)

