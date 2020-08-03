for letter in 'python':
    if letter == 'o':
        continue
    print(letter,end=" ")

print()  #space

i=10
while i > 0:
    i=i-1
    if i==5:
        continue
    print(i,end=" ")

print()  #for space

for letter in 'entrepreneur':
    if letter == 'p':
        continue
    print(letter,end=" ")
    if letter == '':
        break

"""Output >
p y t h n 
9 8 7 6 4 3 2 1 0 
e n t r e r e n e u
"""


# Ex > Take input from user until the user enters a number greater than 100.
inp = int(input("Enter a number : "))
val = inp
while val <= 100:
    print ("Hello",end=" ")
    if val == inp:
        break
else:
    print("Sorry you entered a no greater than 100")

