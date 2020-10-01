#Arithmetic Operators
print("13+2 is", 13+2)  # 13+2 is 15
print("13-2 is", 13-2)  # 13-2 is 11
print("13/2 is", 13/2)  # 13/2 is 6.5
print("13*2 is", 13*2)  # 13*2 is 26
print("13%2 is", 13%2)  # 13%2 is 1  (Remainder is printed)
print("13//2 is", 13//2)  # 13//2 is 6 (Only the integer value of quotient is printed)
print("13**2 is", 13**2)  # 13**2 is 169

#Assignment Operators
x=5
print(x)  # 5
x+=7
print(x)  # 12
x*=7
print(x)  # 12*7 = 84
x-=7
print(x)  # 84-7 = 77
x%=6
print(x)  # 77%6 = 5 (Remainder)
 
#Comparison Operators
y=5
print(y==6)  # False
print(y<7)   # True
print(y<=5)  # True

#Logical Operators
a = True
b = False
print(a and a)  # True
print(a and b)  # False
print(a or a)   # True 
print(a or b)   # True

#Identity Operators
print(a is b)   # False
print(a is not b)  # True

#Membership Operators
ls = [34,54,65,23,87,56]
print(34 in ls)   # True
print(100 in ls)  # False
print(199 not in ls)  # True


#Bitwise Operators
                        #  No  -  8   4   2   1     
                        #  0   -  0   0   0   0
                        #  1   -  0   0   0   1
                        #  2   -  0   0   1   0
                        #  3   -  0   0   1   1
                        #  4   -  0   1   0   0
print(0 & 2)   # 0   (0,0)
print(0 | 3)   # 3   (1,1)          
                        
                        