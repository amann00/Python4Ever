num1 = (input("Enter num 1: "))
num2 = (input("Enter num 2: "))
try:
    print("The Product of num1 and num2 is", int(num1) * int(num2))
except Exception as e:
    print(e)

print("Read this if error exists")

"""Output >
Enter num 1: wee
Enter num 2: 23
invalid literal for int() with base 10: 'wee'
Read this if error exists
"""
