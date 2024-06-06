
number_of_seconds_to_count_down: str = input("Enter the number of seconds to count down: ")

if number_of_seconds_to_count_down.isnumeric():
    converted_type_number_of_seconds_to_count_down: int = int(number_of_seconds_to_count_down)

    while(converted_type_number_of_seconds_to_count_down > 0):
        converted_type_number_of_seconds_to_count_down -= 1
        
        print("{0:d} seconds till the timer expires".format(converted_type_number_of_seconds_to_count_down))

    
    print("Time is up!")
else:
    print("The input is invalid. Try again.")