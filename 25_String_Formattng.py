# 1. Method-1


me = "Johny Baba"
var1 = "This is"
var2 = "From Billu da Dhaba"

a = "Hello Ji ! %s %s %s" % (var1, me, var2)
print(a)
# Hello Ji ! This is Johny Baba From Billu da Dhaba


# 2. Method-2
b = "This is {} {}"
x = "This is {1} {0}"
c = b.format(me, var2)
d = x.format(me, var2)
print(c)
print(d)

"""This is Johny Baba From Billu da Dhaba
This is From Billu da Dhaba Johny Baba"""

import math

# Method-3 (F-String method) (Best of all)
v = f"Bhaiya Ji {var1} {me} {var2} {6 * 45} {math.cos(45)}"
print(v)

"""Bhaiya Ji This is Johny Baba From Billu da Dhaba 270 0.5253219888177297"""
