def funargs(normal, *args_countries, **kwargs_veto):  # arguments  # We can name '*args' with any
    # name such as harry*args , countries*args etc
    print(type(args_countries))  # 'args' will take both lists and tuples as tuple
    print(args_countries)
    print(normal)
    for items in args_countries:  # We can add as many items to the tuple as we want.
        # This is why we use 'args'
        print(items)
    print("\nNow I wanna show you which countries among these have Veto-Powers")
    for key, value in kwargs_veto.items():
        print(f"{key} is {value} Country")


list1 = ["India", "China", "Pakistan", "USA", "France", "Germany"]
normalarg = "These are some of the big countries of world:- "
kw = {"India": "Non-Veto", "China": "Veto", "Pakistan": "Non-Veto",
      "USA": "Veto", "France": "Veto", "Germany": "Non-Veto"}
funargs(normalarg, *list1, **kw)


"""
<class 'tuple'>
('India', 'China', 'Pakistan', 'USA', 'France', 'Germany')
These are some of the big countries of world:- 
India
China
Pakistan
USA
France
Germany

Now I wanna show you which countries among these have Veto-Powers
India is Non-Veto Country
China is Veto Country
Pakistan is Non-Veto Country
USA is Veto Country
France is Veto Country
Germany is Non-Veto Country
"""
