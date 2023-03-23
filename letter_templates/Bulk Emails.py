##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.


import smtplib

email="ezekieloluwadamy@gmail.com"
password="asiupvvejwgtelug" 
asdf=["ezekieloluwadammy@gmail.com", "ezekieloluwadammi@gmail.com", "ezekieloluwadamy@yahoo.com"]
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=email, password=password)

    for asd in asdf:
        connection.sendmail(
            from_addr=email,
            to_addrs= asd,
            msg=f"Subject:Season Greetings\n\n Hello Bro!"
            )

# import datetime as dt

# date=dt.datetime.now()
# year=date.year
# month=date.month
# weekday=date.weekday()+1
# day_in_month=date.day
# hour=date.hour
# minute=date.minute
# seconds=date.second
# print(weekday)
