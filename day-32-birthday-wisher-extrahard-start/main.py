##################### Extra Hard Starting Project ######################
import smtplib
import datetime as dt
import pandas
import random

# 1. Update the birthdays.csv
# Added today as a test day

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates
# and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

# Get current day and month
now = dt.datetime.now()
current_day = now.day
current_month = now.month

# Read data from birthdays.csv
birthday_data = pandas.read_csv("birthdays.csv")

for index, row in birthday_data.iterrows():
    # Check if today is anybody's birthday
    if row["month"] == current_month and row["day"] == current_day:
        my_email = "nmsparkles@gmail.com"
        password = "tqbh bgpz kboa lenq"

        to_email = row["email"]

        # Choose a random letter from the letter templates
        letter_list = ["letter_templates/letter_1.txt", "letter_templates/letter_2.txt", "letter_templates/letter_3.txt"]
        letter_file = random.choice(letter_list)
        with open(letter_file, "r") as file:
            letter = file.read()

        # Replace [NAME] placeholder with person's name
        name = row["name"]
        message = letter.replace("[NAME]", name)


            # Make connection secure: encrypt the email
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=to_email,
                                msg=f"Subject:Happy Birthday {name}!\n\n{message}")
