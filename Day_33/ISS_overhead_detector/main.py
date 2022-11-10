import smtplib

import requests
from datetime import datetime
import math
from geopy import distance

MY_LAT = 12.915727  # Your latitude
MY_LONG = 80.178331  # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

# Your position is within +5 or -5 degrees of the ISS position.


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

time_now = datetime.now()

if distance.distance((iss_latitude, iss_longitude), (MY_LAT, MY_LONG)).km <= 500 and sunrise > time_now.hour > sunset:
    my_email = '100daysofpythonbyme@gmail.com'
    password = 'beifvgxozxuddlxb'
    recipient = 'iwontellmyemail@gmail.com'

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as connection:
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=recipient,
            msg=f'Subject:Look Up \n\n There is a satellite within 500km around you.?')

