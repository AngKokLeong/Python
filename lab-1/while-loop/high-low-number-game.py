import random

print("This program will generate a random number between a lower limit and upper limit of your choice: ")

lower_limit: str = input("Enter the lower limit: ")
upper_limit: str = input("Enter the upper limit: ")

if lower_limit.isnumeric() == True and upper_limit.isnumeric() == True:

    secret_number: int = random.randint(int(lower_limit), int(upper_limit))

    user_guessed_correctly: bool = False

    while(not(user_guessed_correctly)):

        user_guess: str = input("Enter your guess ({0:s} to {1:s}) : ".format(lower_limit, upper_limit))

        if user_guess.isnumeric():

            numeric_user_guess: int = int(user_guess)

            if numeric_user_guess > secret_number:
                print("Too high")
            elif numeric_user_guess < secret_number:
                print("Too low")
            elif numeric_user_guess == secret_number:
                print("You are right!")
                user_guessed_correctly = True
        else:
            print("Invalid input. Please key in a numeric value.")