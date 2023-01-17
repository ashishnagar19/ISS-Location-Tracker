import time
import requests
from datetime import datetime
import smtplib
MY_LAT = 28.393333
MY_LONG = 77.375688

def is_overhead():
        response = requests.get(url="http://api.open-notify.org/iss-now.json")
        response.raise_for_status()
        data = response.json()
        iss_latitude = float(data["iss_position"]["latitude"])
        iss_longitude = float(data["iss_position"]["longitude"])
        if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LAT+5:
            return True

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}
def is_night():
        response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
        response.raise_for_status()
        data = response.json()
        sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
        sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
        time_now = datetime.now().hour
        if time_now >= sunset or time_now <= sunrise:
            return True
while True:
            time.sleep(60)
            if is_night() and is_overhead():
                with smtplib.SMTP("smtp.gmail.com") as connection:
                    connection.starttls()
                    connection.login(user="ash92199@gmail.com", password="hagikfnjqpofdwkb")
                    connection.sendmail(from_addr="ash92199@gmail.com", to_addrs="ashishnagar9650@gmail.com",
                           msg=f"Subject:ISS location Tracker\n\nISS is passing over your location.")







