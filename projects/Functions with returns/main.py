# def format_name(fname,lname):
#     fname = fname.title()
#     lname = lname.title()
#     return fname
#
# # return actually returns something from the function whereas print is literally just surfacing letters on the screen
# # return tells the function to exit as it is the end fo the fuction
# x = format_name('jacob','wong')
# print(x)

def is_leap(year):
    """Returns whether or not its a leap year"""
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year,month):
    """Returns the days in any month of any year after Jesus was born"""
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year) == True:
        if month == 2:
            return 29
        else:
            return month_days[month - 1]
    else:
        return month_days[month - 1]


# 🚨
y = int(input("Enter a year: "))
m = int(input("Enter a month: "))
days = days_in_month(y, m)
print(f'{days} days')

