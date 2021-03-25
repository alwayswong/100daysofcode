import smtplib

email = 'x@gmail.com'
recipient = 'jacob.wong@instacart.com'
password = '1234'
#
# # with will auto close upon leaving the program
# with smtplib.SMTP('smtp.gmail.com') as connection:
#     # encrpytion
#     connection.starttls()
#     connection.login(user=email,password=password)
#     connection.sendmail(from_addr=email,to_addrs=recipient
#                         ,msg='Subject:RESPOND:\n\nSup')

import datetime as dt
import random

now = dt.datetime.now()
year = now.year
dow = now.weekday()
dob = dt.datetime(year=1996,month=8,day=21)
# print(f'My birthday is {dob}')


# wednesday motivations
if dow == 2:

    with open('quotes.txt') as q:
        content = q.readlines()

    with smtplib.SMTP('smtp.gmail.com') as connection:
        # encrpytion
        connection.starttls()
        quote = random.choice(content)
        connection.login(user=email,password=password)
        connection.sendmail(from_addr=email,to_addrs=recipient
                            ,msg=f'Subject:Onwards and upwards..\n\n{quote}')
else:
    pass