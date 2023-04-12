# 🚨 Email SMTP and the datetime module

import smtplib

my_email = "ex_email_1@gmail.com"
# go to your email, manage google account, security, activate 2-step verification,
# app passwords, create birthday_wisher, copy password a put on line 6
password = "yknevdshbllzlisf"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="ex_email_2@yahoo.com",
        msg="Hello\n\nThis is the body of my email."
    )

# 🚨 Datetime module

import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
print(year)
print(month)
print(day_of_week)
print(type(now))
print(type(year))

date_of_birth = dt.datetime(year=1990, month=4, day=26)
print(date_of_birth)

# 🚨 Run code in the cloud
