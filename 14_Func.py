# 1
def func1(a, b):
    print("Average of a and b is", (a + b) / 2)


func1(34, 50)


# 2
def func2(a, b):
    average = (a + b) / 2
    # print(average)
    return average


v = func2(34, 50)  # storing the function in variable 'v'
print(v)


# 3
def leap():
    """This function is to check whether an year is leap or not"""
    year = int(input("Enter any year: "))
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("This is a leap year")
            else:
                print("Not a leap year")
        else:
            print("This is a leap year")
    else:
        print("Not a leap year.")
    return year


print(leap.__doc__)  # double underscores at both sides of doc
leap()
