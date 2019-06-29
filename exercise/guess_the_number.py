import random

secret = random.randint(1, 100)


while True:
    user_guess = int(input("please input your guess number:"))
    if user_guess < secret:
        print("target number is higher than your guess please guess again")
    elif user_guess > secret:
        print("target number is less than what you have guessed please try again")
    elif secret == user_guess:
        print("congrats you have guessed the correct number")
        break
