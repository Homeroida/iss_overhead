import requests
from datetime import datetime
import smtplib
import time

email = "pythontesting17@outlook.com"
password = "Kakanati!1"

MY_LAT = 41.616756  # Your latitude
MY_LONG = 41.636745  # Your longitude


def iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if (MY_LAT - 5) <= iss_latitude <= (MY_LAT - 5) and (MY_LONG - 5) <= iss_longitude <= (MY_LONG - 5):
        return True


def if_night():
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

    time_now = datetime.now().hour

    if time_now >= (sunset + 4) or time_now <= (sunrise + 4):
        return True


while True:
    time.sleep(60)
    if iss_overhead() and if_night():
        with smtplib.SMTP("smtp.office365.com", 587) as connection:
            connection.starttls()
            connection.login(user=email, password=password)
            connection.sendmail(
                from_addr=email,
                to_addrs="chanishvili@yahoo.com",
                msg="subject:ISS is Overhead \n\nlook outside and find ISS"
            )
