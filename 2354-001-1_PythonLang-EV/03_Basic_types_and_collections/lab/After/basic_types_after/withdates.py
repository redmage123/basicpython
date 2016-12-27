import datetime

print("Working with dates:")
print()

today = datetime.date.today()
print("Right now it's {0}".format(today))

year = int(input("What year were you born? "))
month = int(input("What month were you born? "))
day = int(input("What day were you born? "))

birth = datetime.date(year=year, month=month, day=day)

age = today - birth
print("Ok, your birthday is {0}/{1}/{2}".format(month, day, year))
print("Looks like you are {0} years old".format(int(age.days / 365.25)))

birth_this_year = datetime.date(year=today.year, month=birth.month, day=birth.day)

if birth.month < today.month or (birth.month == today.month and birth.day < today.day):
    birth_this_year = datetime.date(year=today.year + 1, month=birth.month, day=birth.day)

untilBirthday = birth_this_year - today

print("Hope you're looking forward to your birthday, it's in {0} days.".format(untilBirthday.days))

print()
print()
