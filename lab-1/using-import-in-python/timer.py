from time import sleep

time_to_wait = int(input("Enter the number of seconds to count down: "))

print("Let's count down {0:d} seconds now....".format(time_to_wait))

sleep(time_to_wait)

print("Time is up!")
