# import cv2 #opencv module
# import math #press n hold ctrl then click on 'module' to see its code
#
# print("Hello everyone!\n This is Maddy here.")
# print("5+3")
# print(math.gcd(3,6)) #finding GCD of 2 no using math
#
# a=54
# b="aman"
# c=57.76
# A = type(a) # 'type' is a function which tells us which type of Data Type we're using.
# B = type(b)
# print(A) #Output- <class 'int'>
# print(B) #Output- <class 'str'>
# print(type(c)) #Output- <class 'float'>
#
# e="45"  #45 is a string
# print(e+1)  #error shown in output
#
# e=int(45)  # 'e'is declared as int var again
# print(e+4) #no error this time
# '''OUTPUT >
#  Hello everyone!
#  This is Maddy here.
# 5+3
# 3
# <class 'int'>
# <class 'str'>
# <class 'float'>
# '''
#
# print("hello world", end=" ")  # joining adjacent lines
# print("hey yesterday we saw a rainy day", "but its a sunny day today")
# print("hello duniya")
# print("C:\\narry")  # ' \n ' is next line or its an escape sequence character
# print("Harry is \n a fit boy.\t He is fond of cycling")  # ' \t ' is new tab
#
# var1 = "Jaat "
# var2 = "Boy"
# var3 = 45
# var4 = 78.23
# print(var3 + var4)
# print(var1 + var2)
# '''
# OUTPUT > hello world hey yesterday we saw a rainy day but its a sunny day today
# hello duniya
# C:\narry
# Harry is
#  a fit boy.	 He is fond of cycling
#  123.23
# Boy
# '''
#
# var1: int = 12  # integer
# var2 = "Hello Bhai"  # string
# var3 = 5.5  # float
# var4 = "18"  # string
# print(var2 + var4)
# print(var1 + var3)
# print(str(var1) + var2)
# print(5*str(int(var4) + var1))
'''
OUTPUT> 
Hello Bhai18
17.5
12Hello Bhai
3030303030
'''

a=8
print(id(a))  #address of 'a' = 1684908016

b=a
print(id(b))  #address of 'b' = 1684908016
#If 2 variables have same data then they both have same address.
c=8+6j
print(type(c))   # <class 'complex'>

d=5.8
e=int(d)  #converting a 'float' into 'int'
print(e)

f=complex(d,a)   #making a complex value
print(f)   #(5.8 + 5j)


