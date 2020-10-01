list1 = ["John Cena","Randy Orton","Goldberg","The Great Khali",
         "Jinder Mahaal"]

# Using Normal for loop method
for index, item in enumerate(list1):
    if index <= 4:
        print(item,"and ", end="")

"""John Cena and Randy Orton and Goldberg and The Great Khali and Jinder Mahaal and"""


# Using Join Function >
a = ", ".join(list1)   # For joining any string or character to the list items.
print(a, "are my favourite WWE Superstars ")