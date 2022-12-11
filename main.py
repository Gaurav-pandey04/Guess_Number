import random

number = random.randint(1, 100)
attempt = 1
guess = int(input("Guess the number: "))
ask = ''

while(True):
    if(guess > number):
        print("You are wrong! This one is too big ")
        ask = input("Do you waana play again?(If yes type y and if No type n):")
        if ask == 'y':
            guess = int(input('Guess again: '))
        elif ask == 'n':
            print('That was the number:', number)
        else:
            print("Invalid Input")
        attempt += 1
    elif(guess < number):
        print("You are wrong! This one is too small ")
        ask = input("Do you waana play again?(If yes type y and if No type n):")
        if ask == 'y':
            guess = int(input('Guess again: '))
        elif ask == 'n':
            print('That was the number:', number)
        else:
            print("Invalid Input")
        attempt += 1

    else:
        print(
            f"Yeah thats the number! You guessed it right in {attempt} attempts")
        break
