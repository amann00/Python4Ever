#1 > Assigning one function to other and deleting a function
def function1():
    print("Johny Baba is high today")

func2 = function1   # function1() is assigned to func2
del function1   # function1() will be deleted
func2()   # Yes the the given string will be printed as the value of function() is assigned to func2


#2 > Returning a function inside main()
def main(num):
    if num==0:
        return print  # returning print() func to main() function
    if num==1:
        return int
a = main(1)
b = main(0)
print(a)    # <class 'int'>
print(b)    # <built-in function print>


#3 > Using decorators
def executor(func):
    func("Johny Baba")
executor(print)   # "Johny Baba" will be printed


#4 >
def decorator1(func1):
    def nowexec():
        print("Executing Now")
        func1()
        print("Executed")
    return nowexec

@decorator1
def who_is_johny():
    print("Johny works in Billu da Dhaba")

# who_is_johny = decorator1(who_is_johny)
who_is_johny()

"""Executing Now
Johny works in Billu da Dhaba
Executed"""
