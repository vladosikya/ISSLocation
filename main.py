import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import requests
import time

LOGIN_EMAIL = ""
PASSWORD = ""
API_URL_ISS = "http://api.open-notify.org/iss-now.json"
YOURE_COORDINATE = [55.755825, 37.617298]

def send_email(from_addr, to_addr, message):
    msg = MIMEMultipart()
    msg["From"] = from_addr
    msg["To"] = to_addr
    msg["Subject"] = "ISS Notification"

    msg.attach(MIMEText(message, "plain"))

    connection = smtplib.SMTP("SMTP SERVER")
    connection.starttls()
    connection.login(user=LOGIN_EMAIL, password=PASSWORD)
    connection.send_message(msg)
    connection.close()

while True:
    response = requests.get(API_URL_ISS)
    info = response.json()["iss_position"]
    if YOURE_COORDINATE[0] - 0.5 <= float(info["longitude"]) <= YOURE_COORDINATE[0] + 0.5 and YOURE_COORDINATE[1] - 0.5 <= float(info["latitude"]) <= YOURE_COORDINATE[1] + 0.5:
        send_email("from_adr", "to_adr", "Say Hi :)")
        time.sleep(10)
    time.sleep(2)