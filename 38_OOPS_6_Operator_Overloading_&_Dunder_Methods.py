#---------------------Operator-Overloading------------------------

class Workers:
    no_of_leaves = 4  # This is a class variable. This is FIXED for all instances

    def __init__(self, name, salary, work):  # This is the Constructor of class
        self.name = name
        self.salary = salary
        self.work = work

    def info(self):
        return f"The name of worker is {self.name}." \
               f"\nHis monthly salary is Rs. {self.salary}" \
               f"\nand he {self.work}."

    def __add__(self, other):  # The constructors which start and end with double underscores are known as Dunder Methods.
        # This 'add' constructor is created for adding 'salary' attribute.
        return self.salary + other.salary

    def __truediv__(self, other):
        return self.salary / other.salary

    def __floordiv__(self, other):
        return self.salary // other.salary

    def __and__(self, other):
        return self.salary & other.salary

    def __mul__(self, other):
        return self.salary * other.salary

    def __repr__(self):
        return f"(Employee: '{self.name}', '{self.salary}', '{self.work}')"

    def __str__(self):
        # __str__() amd __repr__() both returns a string. The only differnece is that
        # __str__() has more preference than __repr__(), that is when we call both then, __str__() will be printed.
        # When __str__() is there in the code, then __repr__() can be printed only by mentioning it in the call.

        return f"The name is  {self.name}. Salary is {self.salary}. And {self.name} {self.work}"

kishan = Workers("kishan", 15000, "Works on Machines")
mohan = Workers("Mohan", 12000, "Handles the Pipelines")

print(kishan + mohan)  # Output > 27000
# This is done by __add__() dunder method

print(kishan / mohan)  # Output > 1.25
# This is done by __truediv__() dunder method

print(kishan // mohan)  # Output > 1
# This is done by __floordiv__() dunder method

print(kishan & mohan)  # Output > 10880
# This is done by __and__() dunder method

print(kishan * mohan)  # Output > 180000000
# This is done by __mul__() dunder method

jai = Workers("Jai", 23000, "Manages Worker's Office")

print(jai)   # (Employee: 'Jai', '23000', 'Manages Worker's Office')
# This is done by __repr__() dunder method, object representation dunder method.
# The __repr__() method is used for returning a String value.

print(str(jai))  # The name is  Jai. Salary is 23000. And Jai Manages Worker's Office



# For more related mapping operators consider below link:
"""https://docs.python.org/3/library/operator.html"""
