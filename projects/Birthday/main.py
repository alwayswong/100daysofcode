import datetime as dt
import pandas as pd
import random
import smtplib

EMAIL = 'x'
PASSWORD = 'y'

now = dt.datetime.now()
day = now.day
month = now.month
today = (day, month)

# HINT 2: Use pandas to read the birthdays.csv
df = pd.read_csv('birthdays.csv')
dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in df.iterrows()}
#print(dict)

if today in dict:
    bday_person = dict[today]
    file_path = f"letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", bday_person["name"])

    with smtplib.SMTP("YOUR EMAIL PROVIDER SMTP SERVER ADDRESS") as connection:
        connection.starttls()
        connection.login(EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=bday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )

