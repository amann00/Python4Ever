class BilluDaDhaba:
    leaves_pm = 4   # This entity is fixed for all employee
    pass

johnybaba = BilluDaDhaba()
bhola = BilluDaDhaba()
munna = BilluDaDhaba()

johnybaba.name = "Johny Baba"
johnybaba.food_cooking = ["Chole Bhature","Jalebi","Rasgulla"]
johnybaba.other_works = "Handling the goons if anyone come to Dhaba"
johnybaba.address = "420/C Badmash Mohalla,Near Soonsan Road, Gumnaam Nagar"
johnybaba.leaves_pm = 8  # We declared that johnybaba has 8 leaves per month

print(johnybaba.address)    # 420/C Badmash Mohalla,Near Soonsan Road, Gumnaam Nagar
print(johnybaba.leaves_pm)   # 8
print(BilluDaDhaba.leaves_pm)  # 4
print(bhola.leaves_pm)   # 4

print(johnybaba.__dict__)  # Dictionary of instances of Johny Baba will be displayed
print(BilluDaDhaba.__dict__)  # Dictionary of i nstances of all the members will be displayed
