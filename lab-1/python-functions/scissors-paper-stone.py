
player_one: str = input("Enter name of Player 1: ")
player_two: str = input("Enter name of Player 2: ")

def compare(input1: str, input2: str) -> None:

    if len(input1) <= 0 or len(input2) <= 0:
        print("Invalid input! Please try again.")
        return

    allowed_values: list[str] = ["Scissors", "Paper", "Stone"]

    #define the matrix for scissors, paper and stone relationship
    #Relationship Mapping
        # 0 = tie
        # 1 = weak against
        # 2 = strong against

    TIE: int = 0
    WEAK_AGAINST: int = 1
    STRONG_AGAINST: int = 2

    # Matrix Positioning Index
        # 0 = Scissors
        # 1 = Paper
        # 2 = Stone

    
    #Mapping in the following order (Scissors, Paper, Stone) for left to right of the matrix
        #           Scissors    Paper   Stone
        # Scissors     0          2       1
        # Paper        1          0       2
        # Stone        2          1       0

    # For example this is how you can interpret:
        # Scissors is tie against Scissors
        # Scissors is strong against Paper
        # Scissors is weak against Stone 

    relationship_matrix = [[0, 2, 1], [1, 0, 2], [2, 1, 0]]

    input1 = input1[0].upper() + input1[1:]
    input2 = input2[0].upper() + input2[1:]

    

    if (input1 in allowed_values) == False or (input2 in allowed_values) == False:
        print("Invalid input! Please try again.")
    else:
        #Match the input text from user against the allowed values in the list 
        input1_index:int = allowed_values.index(input1)
        input2_index:int = allowed_values.index(input2)

        outcome: int = relationship_matrix[input1_index][input2_index]

        if outcome == TIE:
            print("It's a tie!")
        elif outcome == WEAK_AGAINST:
            print("{0:s} wins!".format(input2))
        elif outcome == STRONG_AGAINST:
            print("{0:s} wins!".format(input1))

       
user_one_command: str = ""
user_two_command: str = ""

while user_one_command != "quit" or user_two_command != "quit":

    user_one_command = input("{0:s}, please choose Scissors, Paper or Stone: ".format(player_one))

    if user_one_command == "quit":
        print("Quitting the program...")
        exit()

    user_two_command = input("{0:s}, please choose Scissors, Paper or Stone: ".format(player_two))

    if user_two_command == "quit":
        print("Quitting the program...")
        exit()

    compare(user_one_command, user_two_command)
