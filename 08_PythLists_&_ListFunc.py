mobiles = ["Apple","Samsung","Nokia","Oppo","1+","Vivo"]
print(mobiles[0])
print(mobiles[3])
numbers = [3,54,65,33,55,23]
print(numbers)  #full list printed
numbers.sort()  #func for list-sorting
#numbers.reverse()  #func for reversing list (we'r not using it here to avoid reversing
print(numbers)  #  [3, 23, 33, 54, 55, 65]  sorted list printed
print(numbers[0:4])  # elements before 4th index printed
print(numbers[:])  #by default list range [0:6] is taken
print(numbers[0:-2])  #same as range [0:4]
print(numbers[::-2])  #one number is skipped in reverse listing
"""OUTPUT >
Apple
Oppo
[3, 54, 65, 33, 55, 23]
[3, 23, 33, 54, 55, 65]
[3, 23, 33, 54]
[3, 23, 33, 54, 55, 65]
[3, 23, 33, 54]
[65, 54, 23]
"""

print(len(numbers))  #length of list printed
print(max(numbers))  #max no printed
print(min(numbers))  #min no printed
print(sum(numbers))  #sum of all numbers
"""OUTPUT >
6
65
3
233
"""

mobiles.append("Asus")  # Asus is added to list
print(mobiles)  # ['Apple', 'Samsung', 'Nokia', 'Oppo', '1+', 'Vivo', 'Asus']
numbers.append(37)  # 37 added to numbers list
print(numbers)  # [3, 23, 33, 54, 55, 65, 37]
numbers.extend([9,7,5,3,1])  # for adding multiple items to list
print(numbers)
"""OUTPUT >
['Apple', 'Samsung', 'Nokia', 'Oppo', '1+', 'Vivo', 'Asus']
[3, 23, 33, 54, 55, 65, 37]
[3, 23, 33, 54, 55, 65, 37, 9, 7, 5, 3, 1]
"""

mobiles.insert(2,"LG")  # adding any item to a specific index
print(mobiles)
mobiles.pop()  #last element will be poped/removed
mobiles.remove("Vivo")  #removing any item from list
print(mobiles)
mobiles[2] = "Sony"  #Item at index 2 is replaced by Sony
print(mobiles)
"""OUTPUT >
['Apple', 'Samsung', 'LG', 'Nokia', 'Oppo', '1+', 'Vivo', 'Asus']
['Apple', 'Samsung', 'LG', 'Nokia', 'Oppo', '1+']
['Apple', 'Samsung', 'Sony', 'Nokia', 'Oppo', '1+']
"""

tuple = (1, 2, 3)  #This's a Tupple.A Tupple is similar to List,except the Parenthesis()
#We can't change the values of Tuple.
#Infact a Tuple is made so that its values can't be changed.
# tuple[1] = 5  #invalid because tuple values can't be changed
print(tuple)
"""
(1, 2, 3)
"""

# SWAPPING 2 NOs >
a = 1
b = 8
"""
In C++ >
temp = a
a = b
b = temp
"""
# In Python >
a, b = b, a
print(a,b)
"""
8 1
"""

#Problem of \n in String
print('C:\Docs\newfolder')  # It'll print it wrong as \n is an inbuilt function.
#So use 'r' before the string inside parenthesis to avoid this problem.
print(r'C:\Docs\newfolder')  #This 'r' actually means Raw String
print('C:\Docs\\newfolder')  #Also we can add one more Backslash to avoid this
"""
C:\Docs
ewfolder
C:\Docs\newfolder
C:\Docs\newfolder
"""

d1 = {}     # d1 is a Dictionary
print(type(d1))  # <class 'dict'>

t1 = ()     # t1 is a Tuple
print(type(t1))  # <class 'tuple'>

L1 = []     # L1 is a List
print(type(L1))   # <class 'list'>