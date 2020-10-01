class A:
    classvar1 = "I am a class var of class A"

    def __init__(self):
        self.var1 = "I am inside class A's Constructor"
        self.classvar1 = "I am instance variable of class A"  # If we remove this line..class-variable of class A will be printed.
        # Instance variable is always printed first instead of the class-variable diectly.
        # It will search for the instance variable in both the main and the inherited-class.
        # If it don't get any instance-variable in all classes,then it will print the class variable


class B(A):
    classvar1 = "I am a class var of class B"

    def __init__(self):
        self.var1 = "I am inside class B's Constructor"
        self.classvar1 = "I am instance variable of class B"


a = A()
b = B()

print(b.classvar1)  # "I am instance variable of class A"
# This will be printed when instance variable is there in class A

print(b.classvar1)  # "I am a class var of class B"
# This will be printed when Instance Variablw is not there

print(b.classvar1)  # "I am a class var of class A"
# This will be printed when 'classvar1' variable of class B is removed


# ---------------------super()-Class-Constructor---------------------------

class A:
    classvar1 = "I am a class var of class A"

    def __init__(self):
        self.var1 = "I am inside class A's Constructor"
        self.classvar1 = "I am instance variable of class A"
        self.special = "This is a Special Variable. It can be printed using super() class inheritance"

class B(A):
    classvar1 = "I am a class var of class B"

    def __init__(self):   # Function of class A is overwritten now after inheritance

        super().__init__()  # Super() Class Constructor is used to avoid overwriting of two or more classes
        # Using this we can access all the varibles etc even if they exist in one or more classes.

        self.var1 = "I am inside class B's Constructor"
        self.classvar1 = "I am instance variable of class B"

        # The super() function is used to give access to methods and properties of a parent or sibling class.

        print(super().classvar1)   # I am a class var of class A
        # Even the class-variables can also be directly accessed using super() class constructor

a = A()
b = B()

print(b.classvar1)  # I am instance variable of class B
# Instance variable of class B will be printed as we now have instance variable in class B.

print(b.special)   # Error : becoz class A is overwritten by class B. So the console will not read class A here, without super() function

print(b.special)  # This is a Special Variable. It can be printed using super() class inheritance.

