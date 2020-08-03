height = float(input("Input your height in meters : "))
weight = float(input("Input your weight in Kilograms : "))
# Calculating BMI >
bmi = round(weight / (height * height),3)  # round() func will round-off bmi unto '3'
print("Body Mass Index is: ",bmi )

if bmi < 18.5 : 
    print("You are Underweight.You should eat balanced diet and workout to gain weight.")
elif 18.5 < bmi < 24.9:
    print("Your weight is normal.")
elif 25 < bmi < 29.9:
    print("You are overweight.Workout to lose your weight.")
elif 30 < bmi < 34.9:
    print("You have Obesity Class-I.Do Cardio daily to lose your weight.")
elif 35 < bmi < 39.9:
    print("You have Obesity Class-II.Do Cardio daily & avoid oily foods.")
else:
    print("You have Obesity Class-III.Do Cardio & strict workout daily.Say No to fatty foods.")


"""Output >
Input your height in meters : 1.68
Input your weight in Kilograms : 90
Body Mass Index is:  31.888
You have Obesity Class-I.Do Cardio daily to lose your weight.
"""
