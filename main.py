
import pandas as pd
import smtplib
import datetime as dt
import random

#Fetch current month and day
current_date = dt.datetime.now()
current_month = current_date.month
current_day = current_date.day

#Fetch birthdays from csv
df = pd.read_csv("birthdays.csv")
birthdays = df.to_dict(orient="dict")

#Check if month and day matches and send mail
for index,row in df.iterrows():
    if row["month"] == current_month and row["day"] == current_day:
        name = row["name"]
        mail = row["email"]
        letter_number = random.randint(1,3)
        with open(f"letter_templates/letter_{letter_number}.txt", mode="r") as my_file:
            data = my_file.read()
        message = data.replace("[NAME]", name)
        with smtplib.SMTP("smtp.gmail.com") as connection:
            sender = "DuongJoachim@gmail.com"
            password = "ymiiuskzlvpkfizy"
            connection.starttls()
            connection.login(sender,password)
            connection.sendmail(
                from_addr=sender,
                to_addrs=mail,
                msg=f"subject:Happy birthday!\n\n{message}"
            )
