a = set()
print(type(a))   # <class 'set'>

list1 = [1,2,3]
s = set(list1)
print(s)
list2 = [5,6]
s1 = set(list2)   #set defining list2
s = s1.union(list1)    #union of set 's' and 's1'
s.add(4)    # adding another value 4 in set 's'
print(s)
print(s.clear())   #remove all the elements from set
"""
{1, 2, 3}
{1, 2, 3, 4, 5, 6}
None
"""

# Some more functions :
X = {2,"hello",8,"hii",5}
Y = {5,"hii",2,7}
print("X-Y = ",X.difference(Y))   # method 1
print("Y-X = ",Y-X)   # method 2

D = X.isdisjoint(Y)   # Returns whether two sets have a intersection or not
print("Disjoint of X and Y: ",D)   # Returns False

I = X.intersection(Y)
print("Intersection of X and Y is: ",I)

X.difference_update(Y)  #Removes the items in this set that are also included in another, specified set
print("X is: ",X)   # Differential value of X printed
print("Y is: ",Y)   # Differential value of X printed

Y.discard(5)   # Remove the specified item
print("New set Y is: ",Y)  # 5 is discarded

"""
22.  X-Y =  {8, 'hello'}
23.  Y-X =  {7}
26.  Disjoint of X and Y:  False
29.  Intersection of X and Y is:  {2, 'hii', 5}
32.  X is:  {8, 'hello'}
33.  Y is:  {'hii', 2, 5, 7}
36.  {2, 'hii', 7}
"""
