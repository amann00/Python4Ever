"""
Here the Parent Class 'Shape' is created using 'ABC MetaClass Module' which is directing or ordering
all the Child Classes to execute the printarea() function in there respective statements. Now from here all
the Child Classes like 'Rectangle' and 'Square' must have to execute printarea() statement defined by
Parent Class 'Shape' and this is known as 'Abstract Method'
"""

from abc import ABC, abstractmethod
# This is a module for defining custom abstract base class.
# The sub-classes will implement the abstract base methods as provided by the base classes.

class Shape(ABC):   # Parent class inheriting the ABC module

    @abstractmethod   # To declare a specific function to all the Child Classes via Parent Class.
    def printarea(self):
        return 0

class Rectangle:
    Figure = "Rectangle"
    Sides = 4

    def __init__(self):
        self.length = 6
        self.breadth = 4

    def printarea(self):
        return self.length * self.breadth


class Square:
    Figure = "Square"
    Sides = 4

    def __init__(self):
        self.length = 12

    def printarea(self):
        return self.length * self.length

rect1 = Rectangle()
sqr1 = Square()

print(rect1.printarea())

print(sqr1.printarea())