# --------------------------1-USING-self-constructor--------------------------------
# Displaying the Employee data using self keyword in a class

class Employee:
    no_of_leaves = 4

    def __init__(self):

    def details(self):  # self is used to the instances of a specific object
        return f"Name of the employee is {self.name} " \
               f"\nSalary of {self.name} is {self.salary} " \
               f"\nDepartment of {self.name} is {self.dept} "


Ron = Employee()
Sam = Employee()

Ron.name = "Ron"
Ron.dept = "Marketing"
Ron.salary = "$ 2000"

Sam.name = "Sam"
Sam.dept = "IT"
Sam.salary = "$ 4000"

print(Sam.details())
print()  # for one line space
print(Ron.details())

"""Output >
Name of the employee is Sam 
Salary of Sam is $ 4000 
Department of Sam is IT 

Name of the employee is Ron 
Salary of Ron is $ 2000 
Department of Ron is Marketing
"""


# -----------------------2-USING-class-method-static-method-AND-__init__()-----------------------------------
# The method of giving argument to the class is known as Constructor
# Making a Class object using __init__() function
# This is more convenient and easy as compared to making class without use of __init__() func
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

# When we don't have need of self in function then we use class-methods
    @classmethod  # 'class-method can access only the instance variables of class'
    def change_leaves(cls, newleaves):  # 'cls' keyword will here take the objects,i.e the name of workers as their argument.
        cls.no_of_leaves = newleaves

    @classmethod   # class-method using > string, args, and split() function
    def from_str(cls, string):
        return cls(*string.split("-"))   # for lines 66 and 77

    @staticmethod   # This is used for displaying any string value or anything which doesn't require self or class or instance variables.
    def staticmethod(string):
        print("This is static method." + string)

mohan = Workers("Mohan", 12000, "Handles the Pipelines")  # These arguments will directly go to the __init__() function
kishan = Workers("kishan", 15000, "works on Machines")
raam = Workers.from_str("Raam-16000-SecurityGuard")   # Using 'string-args' method and split func, we want to display info using a single string.

kishan.change_leaves(7)  # the function change_leaves() will be taken as input func
mohan.no_of_leaves = 12  # THis is a Instance Variable. It can be changed for a specific object.

print("The no of leaves Mohan has taken: ",mohan.no_of_leaves)  # 8 will be displayed. Here the variable "no_of_leaves" is changed to 8 instead of 4.
print(mohan.info())
print()
print(kishan.info())
print("\nThe no of leaves Kishan has taken: ", kishan.no_of_leaves)

print("The salary of Raam is: ", raam.salary)    # Displayed using 'string-args' and split func
print()  # for one line space
Workers.staticmethod("\nAnd here we are printing this.")   # printing the string using static method


"""Output >
The no of leaves Mohan has taken: 12
The name of worker is Mohan.
His monthly salary is Rs. 12000
and he Handles the Pipelines.

The name of worker is kishan.
His monthly salary is Rs. 15000
and he works on Machines.

The no of leaves Mohan has taken: 7
"""
