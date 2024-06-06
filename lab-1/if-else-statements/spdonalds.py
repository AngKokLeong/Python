
print("Welcome to SPdonalds")

print("Below is our Breakfast menu:")

breakfast_menu_list: list[str] = ["1.SPMuffin ($5.00)", "2.SPancakes ($3.00)", "3.SPHashbrown ($1.50)"]

print("{0:s}  {1:s}  {2:s}".format(breakfast_menu_list[0], breakfast_menu_list[1], breakfast_menu_list[2]))

user_choice: str = input("Enter your choice of food: ")

if user_choice.isnumeric() == False or (int(user_choice) >= 1 and int(user_choice) <= 3) == False:
    print("Sorry, you have entered an invalid choice")

    print("Unable to continue.  Exiting program....")
else:
    numerical_user_choice: int = int(user_choice)
    
    data: str = breakfast_menu_list[numerical_user_choice - 1]

    product_price_data: str = data[-6:-1].strip()
    product_name_data: str = data[2:11].strip()

    print("{0:s} {1:s} added!".format(product_name_data, product_price_data))

    number_of_products: str = input("How many {0:s} do you want to order? : ".format(product_name_data))

    if number_of_products.isnumeric() == False:
        print("Sorry, you have entered an invalid data")

        print("Unable to continue. Exiting program....")
    else:
        print("The total cost for {0:d} {1:s} is ${2:.2f}".format(int(number_of_products), product_name_data, float(product_price_data[1:]) * float(number_of_products)))