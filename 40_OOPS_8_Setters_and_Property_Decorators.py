class Cricketers:

    def __init__(self,f_name,l_name):
        self.f_name = f_name
        self.l_name = l_name
        # self.email = f"{self.f_name}{self.l_name}987@yahoo.com"

    def printdetails(self):
        return f"The Cricketers Name is {self.f_name}{self.l_name} and his Mail Address is {self.email}"

    @property  # @property is a decorator.
    def email(self):
        return f"{self.f_name}{self.l_name}987@yahoo.com"

mahender_singh_dhoni = Cricketers("Mahender_Singh","Dhoni")

print(mahender_singh_dhoni.printdetails())

print(mahender_singh_dhoni.email)

# Now if we change the name of this cricketer
mahender_singh_dhoni.f_name = "Mahender"

print(mahender_singh_dhoni.email)  # Still the same output will be printed evem after changing the name.
# This problem is solved by 'setters'.

# After creating a function named email and commenting the instance attribute 'self.email' we will get >
print(mahender_singh_dhoni.email)   # Hureey! Now the name got changed in output
# Now due to property decorator there is no need to run above print function having email as a function.

"""
The Cricketers Name is Mahender_SinghDhoni and his Mail Address is Mahender_SinghDhoni987@yahoo.com
Mahender_SinghDhoni987@yahoo.com
Mahender_SinghDhoni987@yahoo.com
MahenderDhoni987@yahoo.com
"""