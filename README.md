# ISS Overhead Notification

This Python script periodically checks if the International Space Station (ISS) is passing overhead and if it is nighttime at the specified location. If both conditions are met, an email notification is sent to a specified email address.

## Setup

1. Clone the repository to your local machine.
   git clone https://github.com/your-username/iss-overhead-notification.git

2. Install the required packages.

pip install requests

3. Open the Python file in a text editor and modify the `email` and `password` variables to match your email address and password. Also, update the `MY_LAT` and `MY_LONG` variables to match your location.

4. Run the Python script.

python iss_overhead_notification.py

## How it works

The script runs an infinite loop that pauses for 60 seconds between each iteration. During each iteration, it calls two functions:

- `iss_overhead`: This function sends an HTTP GET request to the "http://api.open-notify.org/iss-now.json" API to get the current location of the ISS. If the ISS is within 5 degrees of the specified latitude and longitude, the function returns True.

- `if_night`: This function sends an HTTP GET request to the "https://api.sunrise-sunset.org/json" API to get the sunrise and sunset times for the specified location. If the current time is outside of the period from 4 hours after sunrise to 4 hours after sunset, the function returns True.

If both functions return True, the script sends an email notification to the specified email address using the `smtplib` library.

## Notes

- The script requires an active internet connection to work properly.

- The script might not work as expected if the specified email address and password are incorrect, if the location values are incorrect, or if the ISS or sunrise-sunset APIs are down or return unexpected values.

- This script can be scheduled to run automatically using tools like cron on Unix-based systems or Task Scheduler on Windows.
