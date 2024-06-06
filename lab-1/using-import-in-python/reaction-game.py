import time

time_now:float = time.time()

user_input:str = input("Timer starts now! Press any key as quickly as possible!")

time_entered: float = time.time()

time_response: float = time_entered - time_now

print("You took {0:f} seconds to to type {1}".format(time_response, user_input))

