
import random
import smtplib
from datetime import  datetime
import pandas
print("Please enter your loved ones' information in birthdays.csv")
print("Please get the app password for your Google account to use as your login password.")
mail_input = input("Enter your mail:\n")
passkey_input = input("enter your email app password: \n")
print("The system is connecting to your email account. Thank you for your patience.")


mail = mail_input
password =  passkey_input


today = datetime.now()
today_tuple = (today.month, today.day)


data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_a["month"], data_a["day"]): data_a for (index, data_a) in data.iterrows()}
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_template =f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_template) as letter_file:
        contents = letter_file.read()
        aho = contents.replace("[NAME]", birthday_person["name"] )


    with smtplib.SMTP("smtp.gmail.com") as Connection:
        Connection.starttls()
        Connection.login(password=password, user=mail)
        Connection.sendmail(to_addrs=birthday_person["email"],from_addr=mail, msg=f"Subject:Happy Birthday!\n\n {aho}")
        print("Message sent successfully! Thanks for using our service.")



