import datetime

'''
since i'm not supposed to modify the test file... this would include the 
parent directory and thus allow the happy_hour.py file to be found

# # include parent directory in the path
# import sys
# from os.path import dirname, abspath
# sys.path.append(dirname(dirname(abspath(__file__))))


'''


def is_happy_hour(user_date, user_time):
    today = datetime.datetime.strptime(user_date, "%Y-%m-%d").date()
    user_time = datetime.datetime.strptime(user_time, "%H:%M").time()
    #print(today,user_time, user_time)
    if is_christmas(today):
        return False
    elif is_easter(today):
        return False
    elif is_sunday(today):
        return False
    else:
        return 17 <= user_time.hour < 19  # Happy hour between 5 PM and 7 PM

def is_christmas(date):
    return date.month == 12 and date.day == 25

def is_easter(date):
    return date == calc_easter_sunday(date.year)

def is_sunday(date):
    return date.weekday() == 6

def calc_easter_sunday(year):
    a = year % 19
    b = year // 100
    c = year % 100
    d = b // 4
    e = b % 4
    f = (b + 8) // 25
    g = (b - f + 1) // 3
    h = (19 * a + b - d - g + 15) % 30
    i = c // 4
    k = c % 4
    l = (32 + 2 * e + 2 * i - h - k) % 7
    m = (a + 11 * h + 22 * l) // 451
    month = (h + l - 7 * m + 114) // 31
    day = ((h + l - 7 * m + 114) % 31) + 1
    return datetime.date(year, month, day)
if __name__ == "__main__":
    user_date = input("Enter date (YYYY-MM-DD): ")
    user_time = input("Enter time (HH:MM): ")

    result = is_happy_hour(user_date, user_time)
    print("Is it happy hour?", result)
