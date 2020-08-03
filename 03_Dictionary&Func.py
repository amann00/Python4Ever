# Dictionary is nothing but the key value pairs

d1 = {}
print(type(d1))   # <class 'dict'>

d2 = {"Happy":"Burger",
      "Sam":"Chowmin",
      "David":"Pizza",
      "Ronny":{"Breakfast":"Sandwich","Dinner":"Chicken"}}
d2["Jack"] = "Ice-Cream"  # Adding another value to dictionary
d2[420] = "Maggie"   # Adding a value of integer to dictionary
del d2["David"]   # David is deleted from dictionary

print(d2["Ronny"]["Breakfast"])
print(d2["Happy"])
print(d2["Ronny"])   # dictionary of Ronny printed
print(d2)  # whole dictionary printed

#SOME FUNCTIONS OF DICTIONARIES >
d3 = d2.copy()   # Here d3 is a Copy of d2. d3 is not a reference
del d3["Happy"]  #Now Happy'll not be deleted from d3, due to .copy() func
print(d3)  #so when d3 printed, Happy is deleted.
print(d2)  #When d2 printed Happy not deleted.

print(d2.get("Sam"))  # Value of 'Sam' printed
d2.update({"Enni":"Chocolate"})   # Enni is updated in dictionary
print(d2)

print(d2.keys())   #keys'll be printed
print(d2.items())  # items'll be printed


""" OUTPUT >
14.  Sandwich
15.  Burger
16.  {'Breakfast': 'Sandwich', 'Dinner': 'Chicken'}
17.  {'Happy': 'Burger', 'Sam': 'Chowmin', 'Ronny': {'Breakfast': 'Sandwich', 'Dinner': 'Chicken'}, 'Jack': 'Ice-Cream', 420: 'Maggie'}
22.  {'Sam': 'Chowmin', 'Ronny': {'Breakfast': 'Sandwich', 'Dinner': 'Chicken'}, 'Jack': 'Ice-Cream', 420: 'Maggie'}
23.  {'Happy': 'Burger', 'Sam': 'Chowmin', 'Ronny': {'Breakfast': 'Sandwich', 'Dinner': 'Chicken'}, 'Jack': 'Ice-Cream', 420: 'Maggie'}
25.  Chowmin
27.  {'Happy': 'Burger', 'Sam': 'Chowmin', 'Ronny': {'Breakfast': 'Sandwich', 'Dinner': 'Chicken'}, 'Jack': 'Ice-Cream', 420: 'Maggie', 'Enni': 'Chocolate'}
29.  dict_keys(['Happy', 'Sam', 'Ronny', 'Jack', 420, 'Enni'])
30.  dict_items([('Happy', 'Burger'), ('Sam', 'Chowmin'), ('Ronny', {'Breakfast': 'Sandwich', 'Dinner': 'Chicken'}), ('Jack', 'Ice-Cream'), (420, 'Maggie'), ('Enni', 'Chocolate')])
"""