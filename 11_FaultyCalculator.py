"""
FAULTY CALCULATOR >
Design a calculator which will correctly solve all the problems except the following:-
45*3=495 , 56+9=68 , 68/4=4
Program should take operator and the two operands as input and return the result.
"""

print("Welcome to Calc: This calculator is created by Aman\n ")
print("Type in the math operation you want to perform:\n")


while True:
    x = int(input("Enter first operand: "))
    y = int(input("Enter second operand: "))

    print("Select & type in the operator mentioned below: ")
    print("+  for Addition")
    print("-  for Subtraction")
    print("*  for Multiplication")
    print("/  for Division")
    print("**  for Power")
    print("%  for Modulus")
    s=input()
    if s=="*" and x==45 and y==3:
        print("Answer is: ",495)
    elif s=="*" and x==3 and y==45:
        print("Answer is: ",495)
    elif s=="+" and x==56 and y==9:
        print("Answer is: ",68)
    elif s=="+" and x==9 and y==56:
        print("Answer is: ",68)
    elif s=="/" and x==68 and y==4:
        print("Answer is: ",14)
    elif s=="+" and x==4 and y==9:
        print("Answer is: ",68)

    elif s=="*":
        print("Answer is: ",x*y)
    elif s=="+":
        print("Answer is: ",x+y)
    elif s=="/":
        print("Answer is: ",x/y)
    elif s=="-":
        print("Answer is: ",x-y)
    elif s=="**":
        print("Answer is: ",x**y)
    elif s=="%":
        print("Answer is: ",x%y)

    print ("Calculation ended.")
    print("Press y/Y to run again and n/N to exit")
    x = input()
    if(x=="n" or x=="N" or (x!='y' and x!='Y')):
        break


"""
Welcome to Calc: This calculator is created by Aman
 
Type in the math operation you want to perform:

Enter first operand: 56
Enter second operand: 10
Select & type in the operator mentioned below: 
+  for Addition
-  for Subtraction
*  for Multiplication
/  for Division
**  for Power
%  for Modulus
*
Answer is:  560
Calculation ended.
Press y/Y to run again and n/N to exit
y
Enter first operand:
"""