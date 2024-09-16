"""Store following word meanings in ptthon dictonary
table : "a piece of furniture" , "list of facts & figures"
cat  : "a small animal" """

dictionary = {
    "cat" : "a samll animal",
    "table" : ["a piece of furniture","list of facts & figures"]
    
}
print (dictionary)

"""you are given a list subject for students. Assume one classroom is rerquiredd for
1 subject. How many Classrooms are needed by all students.

"python","java","C++","python","javascript",
"java","python","java","C++","C"

"""

set = {"python","java","C++","python","javascript",
"java","python","java","C++","C"}

print(len(set))


"""Write a programme marks of 3 subjects from the user and store them in dictonary.
Start with an empty dictonary & add one  by one.Use subject names as keys & marks as values"""

# marks = {}

# x = int (input("Enter physics number :  "))
# marks.update({"physics" : x})

# x = int (input("Enter math number :  "))
# marks.update({"math" : x})

# x = int (input("Enter chemistry number :  "))
# marks.update({"chemistry" : x})

# print (marks)

"""Figure out a way to store 9 & 9.0 as separate values in a set.
(you can take help of built-in data type)"""


values = {9,"9.0"}

print(values)

values = {
    ("float",9.0),
    ("int",9)
} 

print(type(values))
print(values)
