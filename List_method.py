list  = [2,1,3]


list.append(4)  # adds one element at the end
print(list)

list.sort()  #sorts in ascending order
print(list)

list.sort(reverse=True) #sorts in descending order
print(list)

print(list.sort()) # result show none
print(list)

list1 = ["lichi","banana","apple","mango"]
list1.sort()
print(list1)

list2 = ["Lichi","banana","apple","Mango"]
list2.sort()
print(list2)

list3 = ['a','d','b','f','c']
list3.sort()
print(list3)

list4 = ['a','D','b','F','c']
list4.sort()
print(list4)

list5 = ['a','D','b','F','c']
list5.reverse()                #reverse list
print(list5)

list.insert(1,5)  #insert element at index
print(list)

list.remove(1)  #removes first occurrence of element
print (list)

list.pop(3)  #removes element at index
print(list)


