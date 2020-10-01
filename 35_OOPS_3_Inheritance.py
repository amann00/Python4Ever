# -----------------------SINGLE INHERITANCE----------------------

class Fsociety:

    def __init__(self, ID, name, contact_no ):
        self.name = name
        self.ID = ID
        self.contact_no = contact_no

    def society_info(self):
        return f"The name of the society member is {self.name}" \
               f"\nTheir Id is {self.ID}" \
               f"\nand Contact No is {self.contact_no}"


class Hackers_Club(Fsociety):  # Here we inherited the class 'Fsociety' inside the class 'Hacker'

    def __init__(self,ID, name, contact_no, work):
        self.name = name
        self.ID = ID
        self.contact_no = contact_no
        self.work = work


    def print_hack(self):  # Here we created another function for the class "Hacker"
        return f"The name of the society member is {self.name}" \
               f"\nTheir Id is {self.ID}" \
               f"\nand Contact No is {self.contact_no}" \
               f"\nAnd he is {self.work}"


Mr_Robot = Fsociety("001", "Mr Robot", 6787934175)
Darlene = Fsociety("002", "Darlene", 7874672472)
Elliot = Hackers_Club("003", "Elliot", 9867257527, "Expert Hacker")

print(Darlene.society_info())
print()
print(Elliot.print_hack())  # Additional info "Expert Hacker" will be displayed about Elliot,
# as we added that in constructor of class 'Hackers_Club' and inherited class 'Fsociety' inside class 'Hackers_Club'
print()
print(Elliot.society_info())


"""
The name of the society member is Darlene
Their Id is 002
and Contact No is 7874672472

The name of the society member is Elliot
Their Id is 003
and Contact No is 9867257527
And he is Expert Hacker

The name of the society member is Elliot
Their Id is 003
and Contact No is 9867257527
"""


# -----------------------MULTIPLE-INHERITANCE---------------------------

class Fsociety:

    def __init__(self, ID, name, contact_no, role_in_fsociety):
        self.name = name
        self.ID = ID
        self.contact_no = contact_no
        self.role_in_fsociety = role_in_fsociety

    def society_info(self):
        return f"The name of the society member is {self.name}" \
               f"\nTheir Id is {self.ID}" \
               f"\nand Contact No is {self.contact_no}" \
               f"His he is {self.role_in_fsociety} in Fsociety"


class White_Hat:
    def __init__(self, name, company, job):
        self.name = name
        self.company = company
        self.job = job

    def White_Hat_info(self):
        return f"The name of this Grey Hat Hacker is {self.name} and he also works" \
               f" in {self.company} company as an {self.job}."


class Grey_Hat(White_Hat, Fsociety):

    Expert_in = ["Social Engineering", "Vulnerability Detection", "Reverse Enginerring"]

    def print_Expert_in(self):
        print(self.Expert_in)


Elliot = White_Hat("Elliot", "All Safe", "Ethical Hacker and Security Analyst")

Sam = Grey_Hat("Sam", "360 Security", "Ethical Hacker and Bug Hunter")

print(Elliot.White_Hat_info())
print()
Sam.print_Expert_in()


"""
The name of this Grey Hat Hacker is Elliot and he also works in 
All Safe company as an Ethical Hacker and Security Analyst.

['Social Engineering', 'Vulnerability Detection', 'Reverse Enginerring']
"""

# ---------------------MULTILEVEL-INHERITANCE--------------------------

class Grandfather:
    g = "Azad Hind Fauj"

class Father(Grandfather):
    f = "Indian Army"

    def IAF(self):
        return f"My father served the Indian Army as a great soldier"

class Son(Father):
    f = "Indian Air Force"

    def IAF(self):
        return f"And now I aslo want to join {self.f}, " \
               f"this is my biggest dream and I am working hard over it."

Dev = Son()
Rajveer = Father()
Hukum_Singh = Grandfather()

print(Dev.IAF())  # Here the f-string of Son will be displayed, but if we remove the
# function 'IAF' of class Son,,,then the f-string of father will be displayed.

print(Dev.g)  # As class 'Son' is inheriting class 'Father' and 'Father' is inheriting class 'Grandfather'

"""
And now I aslo want to join Indian Air Force, this is my biggest dream and I am working hard over it.
Azad Hind Fauj
"""