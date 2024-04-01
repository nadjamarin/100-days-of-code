# ------------------ Sending Emails Using smtplib ------------------
# import smtplib
#
# my_email = "nmsparkles@gmail.com"
# password = "tqbh bgpz kboa lenq"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     # Make connection secure: encrypt the email
#     connection.starttls()
#     connection.login(user=my_email, password=password)
# # Add subject line with Subject:, use \n\n to write body of email
#     connection.sendmail(from_addr=my_email,
#                         to_addrs="nadjamarin99@gmail.com",
#                         msg="Subject:Hello\n\nThis is the body of my email.")

# ------------------ Using the datetime Module ------------------
# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# # weekday() gives number of the day, starting with Monday as 0
# day_of_week = now.weekday()
# # if year == 2024:
# #     print("It is 2024")
# print(day_of_week)
#
# date_of_birth = dt.datetime(year=1999, month=1, day=6, hour=4)
# print(date_of_birth)

# ------------------ Monday Motivational Quotes ------------------
# import datetime as dt
# import random
# import smtplib
#
# # Use datetime module to get current day of the week
# now = dt.datetime.now()
# current_day = now.weekday()
# # Choose motivational day to be same day of the week as today (for testing)
# # Change it to Monday (0) after testing
# motivate_day = 0
#
# # If today is Monday, email yourself a random quote
# if current_day == motivate_day:
#     # Read motivational quotes into a list
#     with open("quotes.txt", "r") as quote_file:
#         quote_list = quote_file.readlines()
#
#     # Choose a random quote
#     random_motivation = random.choice(quote_list)
#
#     my_email = "nmsparkles@gmail.com"
#     password = "tqbh bgpz kboa lenq"
#
#     with smtplib.SMTP("smtp.gmail.com") as connection:
#         # Make connection secure: encrypt the email
#         connection.starttls()
#         connection.login(user=my_email, password=password)
#         connection.sendmail(from_addr=my_email,
#                             to_addrs=my_email,
#                             msg=f"Subject:Motivational Quote\n\n{random_motivation}")

