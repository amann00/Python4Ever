# factorial of a number

# n! = n*(n-1)*(n-2)*(n-3).......
# n! = n*(n-1)!

def factorial_iterative(n):
    """This is iterative function not recursive """

    fact = 1
    for i in range(1, n + 1):
        fact = fact*i
    print("The factorial of", n, "is", fact)

print(factorial_iterative.__doc__)
num = int(input("Enter any number: "))  # num is global variable
factorial_iterative(num)

######################################
def factorial_recursive(n):
    """This is a recursive function"""
    print(num)
    if n == 1:
        return 1
    else:
        return n*factorial_recursive(n-1)

    # 5*factorial_recursive(4)
    # 4*factorial_recursive(3)
    # 3*factorial_recursive(2)
    # 2*factorial_recursive(1)  # Here factorial_recursive(1) will return simply 1.So here 2*1 is returned

print(factorial_recursive.__doc__)
num = int(input("Enter any number: "))
print("Factorial of", num," is", factorial_recursive(num))
factorial_recursive(num)


##########################################
# Fibonacci Series > 0,1,1,2,3,5,8,13.......
def fibonacci(n):
    if n < 0:
        print("Please enter a number greater than 0")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# fibonacci(5) = fibonacci(4) + fibonacci(3)
# fibonacci(4) = fibonacci(3) + fibonacci(2)
# fibonacci(3) = fibonacci(2) + fibonacci(1)

num = int(input("Enter the nth term: "))
print("Fibonacci number is", fibonacci(num))
fibonacci(num)

"""Output >
Enter the nth term: 8
Fibonacci number at  8 th position is 13
"""



