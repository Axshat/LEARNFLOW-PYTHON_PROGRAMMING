import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import schedule
import time
from datetime import datetime

FROM_EMAIL = "addd74497@gmail.com"
PASSWORD = "Assss@12"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

def send_email(subject, body, to_email):
    msg = MIMEMultipart()
    msg['From'] = FROM_EMAIL
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(FROM_EMAIL, PASSWORD)
        text = msg.as_string()
        server.sendmail(FROM_EMAIL, to_email, text)
        server.quit()
        print(f"Email sent to {to_email} successfully.")
    except Exception as e:
        print(f"Failed to send email to {to_email}. Error: {str(e)}")

def schedule_email(subject, body, to_email, send_time):
    schedule_time = datetime.strptime(send_time, "%Y-%m-%d %H:%M:%S")
    now = datetime.now()
    delay = (schedule_time - now).total_seconds()

    if delay > 0:
        schedule.enter(delay, 1, send_email, (subject, body, to_email))
        print(f"Email scheduled to {to_email} at {send_time}.")
    else:
        print("Scheduled time is in the past. Please provide a future time.")

def main():
    subject = input("Enter the subject of the email: ")
    body = input("Enter the body of the email: ")
    to_email = input("Enter the recipient's email address: ")
    send_time = input("Enter the scheduled time (YYYY-MM-DD HH:MM:SS): ")

    schedule_email(subject, body, to_email, send_time)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
