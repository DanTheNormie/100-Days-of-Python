# import random
# import smtplib
# import datetime
#
# my_email = '100daysofpythonbyme@gmail.com'
# password = 'beifvgxozxuddlxb'
# recipient = 'pkakarshgreentiger@gmail.com'
#
# with smtplib.SMTP_SSL('smtp.gmail.com', 465) as connection:
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs=recipient,
#         msg=f'Subject:Hi da noobdae \n\n This is a remainder that you are a Noobdae}')



# import random
# import smtplib
# import datetime
#
# my_email = '100daysofpythonbyme@gmail.com'
# password = 'beifvgxozxuddlxb'
# recipient = 'pkakarshgreentiger@gmail.com'
#
# now = datetime.datetime.now()
# year = now.year
# month = now.month
# weekday = now.weekday()
# if weekday == weekday:
#     with open(file='motivational_quotes.txt') as file:
#         quotes_list = file.readlines()
#         with smtplib.SMTP_SSL('smtp.gmail.com', 465) as connection:
#             connection.login(user=my_email, password=password)
#             connection.sendmail(
#                 from_addr=my_email,
#                 to_addrs=recipient,
#                 msg=f'Subject:Hi da noobdae \n\n This is a remainder that you are a Noobdae}')


import random
import smtplib
import pandas
import datetime

my_email = '100daysofpythonbyme@gmail.com'
password = 'beifvgxozxuddlxb'
recipient = 'pkakarshgreentiger@gmail.com'

template_list = [open(file=f'./letter_templates/letter_{i}.txt',mode='r').read() for i in range(1,4)]

data = pandas.read_csv('birthdays.csv')
list_of_birthdays = data.to_dict(orient='records')

print(list_of_birthdays)

now = datetime.datetime.now()
this_month = now.month
this_day = now.day
for birthday in list_of_birthdays:
    if birthday['month'] == this_month and birthday['day'] == this_day:
        recipient_name = birthday['name']
        recipient_email = birthday['email']
        birthday_template: str = random.choice(template_list)
        birthday_template = birthday_template.replace('[NAME]', recipient_name)
        birthday_template = birthday_template.replace('Angela', 'Danny')
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as connection:
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=recipient,
                msg=f'Subject:Happy Birthday \n\n {birthday_template}')


