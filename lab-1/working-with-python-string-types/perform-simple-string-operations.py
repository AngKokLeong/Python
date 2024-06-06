
s1: str = input("Enter string 1: ")
s2: str = input("Enter string 2: ")
s3: str = input("Enter string 3: ")

#refer to https://docs.python.org/3/library/string.html#formatstrings
print("Length of string 1 {0:s} is {1:d}".format(s1, len(s1)))
print("Length of string 2 {0:s} is {1:d}".format(s2, len(s2)))
print("Length of string 3 {0:s} is {1:d}".format(s3, len(s3)))

print("String 1 in all caps  {0:s}".format(s1.upper()))

character_a_index_location_list: list[int] = []
index = 0
if ('a' in s2) == False:
    print("The letter a is not found in {0:s}".format(s2))
else:
    for character in s2:
        if character == 'a':
            character_a_index_location_list.append(index)
        
        index = index + 1
    
    print("The letter a is found in the following index in {0:s}: {1}".format(s2, character_a_index_location_list))

print("The first two characters of {0:s} is {1:s}".format(s3, s3[0:2]))