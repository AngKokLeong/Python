
message: str = input("Enter the message you want to repeat: ")

number_of_times_to_repeat: str = input("Enter the number of times you want to repeat this message: ")

if number_of_times_to_repeat.isnumeric() == False:
    print("You have entered the invalid input")
else:
    for number in range(int(number_of_times_to_repeat)):
        print(message)


