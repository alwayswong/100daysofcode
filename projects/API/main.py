# API is just a fancy way to say interact with some external data or software
# API endpoint is where the data is stores, usually a URL

import requests

# # 1: hold on, 2: success, 3: no permission, 4: some problem
# # can also raise an exception when you get certain error codes which is a cleaner way to use break + print i think
# reponse = requests.get(url='http://api.open-notify.org/iss-now.json')
# print(reponse.json())

from tkinter import *


# def get_quote():
#     quote = requests.get(url='https://api.kanye.rest')
#     quote.raise_for_status()
#     json = quote.json()['quote']
#     return json
#
#     #Write your code here.
#
#
#
# window = Tk()
# window.title("Kanye Says...")
# window.config(padx=50, pady=50)
#
# canvas = Canvas(width=300, height=414)
# background_img = PhotoImage(file="background.png")
# canvas.create_image(150, 207, image=background_img)
# quote_text = canvas.create_text(150, 207, text=get_quote(), width=250, font=("Arial", 30, "bold"), fill="white")
# canvas.grid(row=0, column=0)
#
# kanye_img = PhotoImage(file="kanye.png")
# kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
# kanye_button.grid(row=1, column=0)
# window.mainloop()

# from datetime import datetime
# now = datetime.now()
# LAT = 21.3069
# LONG = 157.8583
#
# parameters = {
#     'lat': LAT,
#     'lng': LONG,
#     'formatted': 0
# }
#
#
# response = requests.get(url='https://api.sunrise-sunset.org/json', params=parameters)
# response.raise_for_status()
# data = response.json()
# sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
# sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
# now.hour
#
# print(f'The sunrise in Honolulu is at {sunrise} and the sunset is at {sunset}')

import requests
from datetime import datetime

MY_LAT = 21.3069 # Your latitude
MY_LONG = 157.8583 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
print(sunrise)
print(sunset)
time_now = datetime.now()
print(time_now)
#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



