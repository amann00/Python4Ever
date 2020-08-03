list1 = [["Sunday", 10], ["Monday", 6],
         ["Tuesday", 18], ["Wednesday", 14],
         ["Thursday", 22], ["Friday", 8],
         ["Saturday", 15]]
dic = dict(list1)
print(list1)
for item, products in list1 :  # printing the list1 using python Lists
    print(item, "products sold", products)  # method-1

print()  # space
dic = dict(list1)
print(list1)

for item, products in dic.items() :  # printing the list1 using python Dictionary
    print(item, "products sold", products)  # method-2

    print(item)  # print only the items

# Question > There is a list having strings and integers both.
# But you have to print the integers which are greater than 7.

# Method-1
ls = [2, 3, "Sam", 7, 5, "Happy", 12, 16, "Joy", 14, "Bella", 1]
for item in ls :
    if str(item).isnumeric() and item > 6 :  # here isnumeric() func is used to to get only the numeric items.
        print(item, end=" ")
print()  # for space

# Method-2
print()  # for space
ls = [2, 3, "Sam", 7, 5, "Happy", 12, 16, "Joy", 14, "Bella", 1]
for item in ls :
    if type(item) is int and item > 6 :  # using the type() func
        print(item,end= " ")
print()  # for space

# Output > 7 12 16 14
#
#          7 12 16 14


i = 0
while (i < 5) :
    print(i,end=" ")
    i = i + 1
print()  # for space
# Output > 0 1 2 3 4


i = 7
while i > 0 :
    i -= 1
    if i == 1 :
        break
    print(i, end=" ")
print("loop ends")
# Output >  6 5 4 3 loop ends