class A:
    def check(self):
        print("This is a method from Class A")

class B(A):
    def check(self):
        print("This is a method from Class B")

class C(A):
    pass

class D(B, C):
    pass

a = A()
b = B()
c = C()
d = D()

print(d.check())  # "This is a method from Class A"..will be printed when class B is empty
# It will search in class B and C first as they are inherited by class D

print(d.check())   # "This is a method from Class B"..will be printed as class D is inheriting class B and c.
# So it will look in class b and C first,instead of A.

"""Multiple inheritance sometimes creates problems in some programming languages like Java, C++ etc.
When we inherit more than one classes in each other, then a confusion is created to get the result.
Thats why in some cases its recomended to avoid Multiple Inheritance. 
However this problem does not occur in Python in most of the cases and we get the right output.   
"""