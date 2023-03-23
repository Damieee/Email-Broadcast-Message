import pandas as pd
import smtplib

# read csv file and create a dictionary ihiihihihy Seyi's part
try:
    data = pd.read_csv("Raaaaaa.csv")
    contact = pd.DataFrame(data, columns=["Emails", "First Names"])
except Exception as e:
    print(e)

contact_dict = {}
for (index, row) in contact.iterrows():
    name = str(row["First Names"]).title()
    email = str(row["Emails"])
    if name.lower() != "nan" and email.lower() != "nan":
        contact_dict[name] = email

# login to the email server
my_email = ""
password = ""

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)

    # send emails to each recipient
    for (name, email) in contact_dict.items():
        with open("letter_templates/letter_1.txt", "r") as message:
            my_message = message.read()
            my_message = my_message.replace("[NAME]", name)
            my_message = my_message.replace("[IMAGE_SRC]", "Pastor.png")
            my_message = my_message.replace("[EMAIL_LINK]", "")
            my_message = my_message.replace("[PHONE_NUMBER]", "09025637257")

        try:
            connection.sendmail(
                from_addr=my_email,
                to_addrs=email,
                msg=f"Subject: Hi Dear Pastor!\nContent-Type: text/html;\n\n{my_message}"
            )
            print(f'Email sent to {name} <{email}>')
        except Exception as e:
            print(f'Error: Email not sent to {name} <{email}>')
            print(e)
