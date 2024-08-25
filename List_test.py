"""write a prigramme to ask the user to enter name of their 3 favourite 
movies & store theme ina list"""

movies = []
mov1 = input("enter 1st movies : ")
mov2 = input("enter 2nd movies : ")
mov3 = input("enter 3rd movies : ")

movies.append(mov1)
movies.append(mov2)
movies.append(mov3)

print(movies)

"""write a programme to check ifa list contains a palindrome of elements. (Hint : use copy() method)"""

list1 = [1,2,1]


copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    {
        print ("palindrome")
    }
else:
    print("Not palindrome")    
    
    
list2 = ['m','a','a','m']


copy_list2 = list2.copy()
copy_list2.reverse()

if(copy_list2 == list2):
    {
        print ("palindrome")
    }
else:
    print("Not palindrome")    

"""write a programme to count the number of students with the "A" grade in the following tuple"""

tup = ("C","D","A","A","B","B","A")
print (tup.count('A'))

"""Now store the above values in a list & sort theme from "A" to "D" """
grade = ["C","D","A","A","B","B","A"]
grade.sort()
print (grade)