collection = set()
collection.add(1) # adds an element
collection.add(2)
collection.add(2)
collection.add("Nasif")
collection.add((1,2,3)) # tuples in set


collection.remove(1)  # remove an element
print (collection) # {1,2} ignor duplicate value

collection.clear()
print (collection)  # For erasing all elements
print(len(collection))

collection = {"helllo","AIUB","Nasif","world","coding","Python"}
print(collection.pop())  #popping out random value
print(collection.pop())

set1 = {1,2,3}
set2 = {3,4,5}

print (set1.union(set2))
print (set1.intersection(set2))