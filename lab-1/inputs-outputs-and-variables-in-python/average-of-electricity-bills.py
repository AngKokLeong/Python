
bill_counter:int = 1
loop_condition: bool = True

bill_list: list = []


header_text = "Calculate the average of your last 6-months electricity bill"

print("*" * (len(header_text)+ 1))

print(header_text)

print("*" * (len(header_text) + 1))

print(" ")

while(loop_condition):

    if bill_counter > 6:
        break

    current_bill: float = float(input("Enter Bill #{0:d}: ".format(bill_counter)))
    

    bill_list.append(current_bill)

    bill_counter = bill_counter + 1


print("Your electricity bills for the past 6 months are: ")

summary_text: str = ""
total_six_months_bill: float = 0.0

for item in bill_list:
    summary_text += "${0:0.2f}, ".format(item)
    total_six_months_bill += float(item)

print(summary_text[0:(len(summary_text) - 2)])
print("The average of your electricity bill is ${0:0.2f}".format(total_six_months_bill / 6))


    