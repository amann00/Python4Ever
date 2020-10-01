# Pattern-1
num = int(input("Enter the no of rows: "))
for i in range(1, num + 1):  # i stands for row no
    for j in range(1, num + 1):  # j stands for column no
        print("*", end=" ")
    print()
"""Output ->
* * * *
* * * *
* * * *
* * * *
"""

# Pattern-2
num = int(input("Enter the no of rows: "))
for i in range(1, num + 1):  # i stands for row no
    for j in range(1, i + 1):  # j stands for column no
        print("*", end=" ")
    print()
"""Output ->
* 
* * 
* * * 
* * * *
"""

# Pattern-3
num = int(input("Enter the no of rows: "))
for i in range(1, num + 1):
    for j in range(1, num + 1):
        if j <= i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
# i    j         condition
# 1    1          j<=1
# 2    1,2        j<=2
# 3    1,2,3      j<=3
# 4    1,2,3,4    j<=4
"""Output ->
* 
* * 
* * * 
* * * *
"""

# Pattern-4
num = int(input("Enter the no of rows: "))
for i in range(num + 1, 0, -1):  # i stands for row no
    for j in range(1, i + 1):  # j stands for column no
        print("*", end=" ")
    print()
"""Output ->
* * * * 
* * *
* *
*
"""

# Pattern-5
num = int(input("Enter the no of rows: "))

for i in range(1, num + 1):  # i stands for row no
    for j in range(1, i + 1):  # j stands for column no
        print("*", end=" ")
    print()
for i in range(num - 1, 0, -1):  # i stands for row no
    for j in range(1, i + 1):  # j stands for column no
        print("*", end=" ")
    print()
"""Output ->
Enter the no of rows: 4
* 
* * 
* * * 
* * * * 
* * * 
* * 
* 
"""

# Pattern-6
num = int(input("Enter the no of rows: "))

for i in range(1, num + 1):  # i stands for row no
    for j in range(1, i + 1):  # j stands for column no
        print(i, end=" ")
    print()
"""Output -> for 'i' displayed row-wise
1 
2 2 
3 3 3 
4 4 4 4 
"""

# Pattern-7
num = int(input("Enter the no of rows: "))

for i in range(1, num + 1):  # i stands for row no
    for j in range(1, i + 1):  # j stands for column no
        print(j, end=" ")
    print()
for i in range(num - 1, 0, -1):  # i stands for row no
    for j in range(1, i + 1):  # j stands for column no
        print(j, end=" ")
    print()
"""Output -> for 'j' displayed column-wise
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 
1 2 
1 
"""

# Pattern-8
num = int(input("Enter the no of rows: "))
k = 1
for i in range(1, num + 1):  # i stands for row no
    for j in range(1, k + 1):  # j stands for column no
        print("*", end=" ")
    k = k + 2
    print()
"""Output ->
* 
* * * 
* * * * * 
* * * * * * * 
"""

# Question -> Create a pattern using bool function, in which when the user inputs '0'
# inverse staircase pattern is printed and when inputs '1' correct staircase is printed.

# Method-1 >
rows = int(input("Enter the number of rows: "))
num = int(input("Enter 0 or 1: "))
b = bool(num)

if b == True:
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print("*", end=" ")
        print()
elif b == False:
    for i in range(rows, 0, -1):
        for j in range(1, i + 1):
            print("*", end=" ")
        print()

"""Output ->
Enter the number of rows: 5
Enter 0 or 1: 1
* 
* * 
* * * 
* * * * 
* * * * * 
"""

# Method-2 >
rows = int(input("Enter the number of rows: "))
bool_val = int(input("Enter 0 or 1: "))
if bool_val == "1":
    for i in range(1, rows + 1):
        print(i * "*")

if bool_val == "0":
    for j in range(rows, 0, -1):
        print(i * "*")


# Astrologers"s Stars
rows = int(input("Enter the number of rows: "))
num = int(input("Enter 0 or 1: "))
b = bool(num)

if b == True:
    for i in range(1,rows+1):
        for j in range(1,i+1):
            print("*", end=" ")
        print()
elif b == False:
    for i in range(rows,0,-1):
        for j in range(1,i+1):
            print("*", end=" ")
        print()


"""
Enter the number of rows: 6
Enter 0 or 1: 0
* * * * * * 
* * * * * 
* * * * 
* * * 
* * 
* 

Enter the number of rows: 6
Enter 0 or 1: 1
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * * * 
"""