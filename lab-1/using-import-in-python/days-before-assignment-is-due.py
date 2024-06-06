from datetime import date
import calendar

date_today: date = date.today()

print("Today is " + date_today.__format__("%d-%b-%Y"))

assignment_duedate: str = str(input("Please enter the due date of the assignment (dd-mm-yyyy) :"))

formatted_assignment_duedate: date = date(int(assignment_duedate[-4:]), int(assignment_duedate[3:5]), int(assignment_duedate[0:2]))

print("Assignment due date is " + formatted_assignment_duedate.__format__("%d-%b-%Y"))


remaining_assignment_duration:date = formatted_assignment_duedate - date_today

if remaining_assignment_duration.days >= 30:

    estimated_number_of_years : int = int(remaining_assignment_duration.days / 365)
    estimated_number_of_months : int = int((remaining_assignment_duration.days % 365) / 30)
    estimated_number_of_days: int = int((remaining_assignment_duration.days % 365) % 30)


    if estimated_number_of_years > 0:
        if estimated_number_of_years > 1:
            print("{0:d} years, {1:d} months, {2:d} days till assignment is due".format(estimated_number_of_years, estimated_number_of_months, estimated_number_of_days))
        elif estimated_number_of_years == 1:
            print("{0:d} year, {1:d} months, {2:d} days till assignment is due".format(estimated_number_of_years, estimated_number_of_months, estimated_number_of_days))
    else:
        if estimated_number_of_months > 1:
            print("{0:d} months, {1:d} days till assignment is due".format(estimated_number_of_months, estimated_number_of_days))
        elif estimated_number_of_months == 1:
            print("{0:d} month, {1:d} days till assignment is due".format(estimated_number_of_months, estimated_number_of_days))
    

elif remaining_assignment_duration.days > 1 and remaining_assignment_duration.days < 30:
    print("{0:d} days till assignment is due".format(remaining_assignment_duration.days))
else:
    print("{0:d} day till assignment is due".format(remaining_assignment_duration.days))