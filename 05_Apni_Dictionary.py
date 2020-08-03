print("Welcome to Apni Dictionary")

dict = {"Abandon":"leave out",
        "Solitude":"loneliness",
        "Maneuver":"move skillfully or carefully",
        "Matriarch":"a woman who is head of family"}
val = input("Enter a word : ")
print(dict.get(val))


"""Output >
Welcome to Apni Dictionary
Enter a word : Maneuver
move skillfully or carefully
"""