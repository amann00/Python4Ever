var1 = 30
var2 = 10
print("Enter a number")
var3 = int(input())

if var1>var2:
    print("Greater")
elif var1==var2:
    print("Equal")
else:
    print("Smaller")
#############################

list1 = [2,7,5,10]
print(4 in list1)   # It'll return whether it is True or False
if 4 in list1:
    print("Yes its in the list")
else:
    print("No its not in the list")

list2 = [13,19,23,20]
print(13 in list2)
if 13 not in list2:
    print("This no is not in list")
else:
    print("Yes,the no is in the list")

"""Output >
False
No its not in the list
True
The no is in the list
"""

#############################

age = int(input("Please,enter your age: \n"))
if 18 < age < 80 :
    print("Yes, you are eligible for driving license.Gud Luck")
elif 6 < age < 18 :
    print("You are under age. You cannot drive")
elif age == 18:
    print("You are 18. So you can have license for two wheelers only")
else:
    print("People above age 80 are not allowed to drive")

"""Output >
Please,enter your age: 
82
People above age 80 are not allowed to drive
"""