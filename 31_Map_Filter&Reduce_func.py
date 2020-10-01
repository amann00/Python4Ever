#----------------------MAP-------------------------
numbers = ["3", "6", "9", "12"]
numbers = list(map(int, numbers))  # without the list() func the map() func will return it as object.
# list() and map() will always ne written together if we are applying it to a list
# As shown in below print() func
print(map(int, numbers))   # <map object at 0x02BE0FB8>
# 1 > Instead of using 'for' loop for the same thing-
for i in range(len(numbers)):  # When the object is a string, the len() function
    # returns the number of characters in the string
    numbers[i] = int(numbers[1])

numbers[2] = numbers[2] + 3
print(numbers[2])  # 9 will be printed


# 2 Simply using a normal function with map()
def sq(a):
    return a*a

num = [2,5,3,8,6,12,10,4]
square = list(map(sq, num))
print(square)   # [4, 25, 9, 64, 36, 144, 100, 16]


# 3 ALTERNATIVE > Using map() function with lambda()
num = [2,5,3,8,6,12,10,4]
square = list(map(lambda x: x*x, num))  # Using lambda func() here is much reliable and easy than normal func()
print(square)   # [4, 25, 9, 64, 36, 144, 100, 16]


# 4 Square and Cube of numbers using lambda() func >
def square(a):
    return a*a

def cube(a):
    return a*a*a

calc = [square, cube]  # List having just the names of functions
for i in range(0,5):  # no from 0 to 4
    val = list(map(lambda x:x(i), calc))

"""
[0, 0]
[1, 1]
[4, 8]
[9, 27]
[16, 64]
"""

#-----------------------FILTER-------------------------

list1 = [1,2,3,4,5,6,7,8,9]

def greater(num):
    return num > 5

result = list(filter(greater, list1))
print(result)  # [6,7,8,9]


#----------------------REDUCE----------------------------
# Normal Program without using REDUCE() func >
list2 = [1,2,3,4,5,6,7,8]
num = 0
for i in list2:
    num = num + i
print("Answer = ",num)   # Answer =  36

# Using REDUCE() Func >
from functools import reduce

num = reduce(lambda x,y:x+y, list2)
print("Answer = ",num) # Answer =  36
