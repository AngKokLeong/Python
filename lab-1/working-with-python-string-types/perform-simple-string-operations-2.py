
random_strings: str = input("Enter 3 random strings, separated by commas: ")

random_strings_list: list[str] = random_strings.split(',')

if len(random_strings_list) >= 0 and len(random_strings_list) < 3:
    print("There is no enough input")
else:

    s1: str = random_strings_list[0].strip()
    s2: str = random_strings_list[1].strip()
    s3: str = random_strings_list[2].strip()

    print("s1 is {0:s}".format(s1))
    print("Length of {0:s} is {1:d}".format(s1, len(s1)))
    print("2nd and 3rd characters of {0:s} is {1:s}".format(s1, s1[1:4]))

    print("")

    print("s2 is {0:s}".format(s2))
    print("Length of {0:s} is {1:d}".format(s2, len(s2)))
    print("5th to 7th characters of {0:s} is {1:s}".format(s2, s2[4:7]))

    print("")

    print("s3 is {0:s}".format(s3))
    print("Length of {0:s} is {1:d}".format(s3, len(s3)))
    print("Last two characters of {0:s} is {1:s}".format(s3, s3[-2:]))