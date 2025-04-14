import datetime
from bday_messages import get_msg

# This program will calculate the number of days until your birthday
today = datetime.date.today()
next_birthday = datetime.date(2025,7,1)




days_away = today - next_birthday
if days_away.days < 0:
    days_away = - days_away
    print("Your birthday is in", days_away.days, "days")
elif days_away.days == 0:
    print ("Today is your BDay!")
    print (get_msg())
else: 
    print("Your birthday has passed ", days_away.days, "days")


