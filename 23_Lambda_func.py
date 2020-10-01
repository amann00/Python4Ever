# Normal Function
def minus(x, y):
    return x - y
print(minus(9, 4))


# LAMBDA FUNCTION Example-1 >
minus = lambda x, y: x - y  # lambda function is nothing, just another method of making functions
"""This is a lambda function"""

print(minus.__doc__)
print(minus(9, 4))


# LAMBDA FUNCTION Example-2 >
a = [[87,65],[65,34],[23,10],[90,45]]
a.sort(key=lambda x: x[1])  # key function is used for calling a function
# 1st index i.e 65,34,10,45 are sorted
print(a)

# [[23, 10], [65, 34], [90, 45], [87, 65]]


# Normal Function >
def func(x):
    return x[1]

x = [[87,65],[65,34],[23,10],[90,45]]
x.sort(key=func)   # key function is used for calling a function
print(x)

# [[23, 10], [65, 34], [90, 45], [87, 65]]
