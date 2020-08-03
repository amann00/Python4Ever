"""This is a game in which you have to guess the hidden number in 7 chances
"""

print("THIS IS A NUMBER GUESSING GAME ('_')\n")
print("Game Rules- ")
print("You have to guess a no from 1 to 100")
print("Total no of chances you have for winning are 7.So lets play.\n")
no_of_guess = 1
while(no_of_guess<=7):
    guess = int(input("Guess a no : "))
    if(guess<45):
        print("You entered a smaller no,please input some greater no")
    elif(guess>45):
        print("You entered a greater no,please input a smaller no")
    else:
        print("Oh great, 'YOU WON' ! .You guessed the correct no.\n")
        break
    print(7-no_of_guess,"chances left\n")
    no_of_guess = no_of_guess + 1
    if(no_of_guess > 7):
         print("   'GAME OVER' You have exceeded the limit of total chances")


"""Sample -
THIS IS A NUMBER GUESSING GAME ('_')

Game Rules- 
You have to guess a no from 1 to 100
Total no of chances you have for winning are 7.So lets play.

Guess a no : 34
You entered a smaller no,please input some greater no
6 chances left

Guess a no : 50
You entered a greater no,please input a smaller no
5 chances left

Guess a no : 44
You entered a smaller no,please input some greater no
4 chances left

Guess a no : 48
You entered a greater no,please input a smaller no
3 chances left

Guess a no : 45
Oh great, 'YOU WON' ! .You guessed the correct no.
"""