list1 = ["Maggi","Lays","Ketchup","Cold-Drinks","Pizza"]

i = 1
for item in list1:
    if i % 2 != 0:
        print(f"Hey Siri, Please order {item} for me")
    i += 1

"""
Hey Siri, Please order Maggi for me
Hey Siri, Please order Ketchup for me
Hey Siri, Please order Pizza for me
"""

for index, item in enumerate(list1):   # index keyword here start numbering from 0,1,2,3,4....
    if index % 2 != 0:
        print(f"Hey Siri, Please order {item} for me")  # So the items at 1 and 3 index will be printed

"""
Hey Siri, Please order Lays for me
Hey Siri, Please order Cold-Drinks for me
"""