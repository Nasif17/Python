str = "i am Nasif"
 
print (str.endswith("if")) #returns true if string ends with substr


str1 = str.capitalize() #capitalize 1st Char
print (str1) 

print (str.replace("a","o")) #replace all occurrences of old sub-string 
print(str.replace("Nasif","rafidi"))

print(str.find("N")) #returns 1st index of 1st occurrer

"""if we put any not existance
character it will show result -1
Here is an example"""

print(str.find("r"))

print(str.count("a"))# counts the occurrence of substring


