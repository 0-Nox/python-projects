import random
x=int(input("Enter the max range of the number: "))
def guess(x):
    random_number=random.randint(1,x)
    guess=0
    while guess != random_number:
        guess=int(input(f"Guess a number between 1 to {x}: "))
        if(guess==random_number):
            print("Your guessed number is correct")
        elif(guess>random_number):
            print("Your guess number is high")
        else:
            print("Your guess number is low")

guess(x)