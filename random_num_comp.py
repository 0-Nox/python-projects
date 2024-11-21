#Imports a inbuilt module called random
import random
#Taking the input from the user to set the maximum range value e.g 1-10 or 1-20
x=int(input("Enter the max range of the number: "))
#This is a function for the guess
def guess(x):
    #This is function in random module it selects a random number between (a,b) in this case its (1-x)
    random_number=random.randint(1,x)
    guess=0
    #This a loop take input until the user gets the right number
    while guess != random_number:
        guess=int(input(f"Guess a number between 1 to {x}: "))
        if(guess==random_number):
            print("Your guessed number is correct")
        elif(guess>random_number):
            print("Your guess number is high")
        else:
            print("Your guess number is low")

guess(x)
