from datetime import date
from datetime import datetime


def getCountTable(table):
    a = 0
    for i in table:
        a = a + 1
    print(a)
    return a


def getDays():
    curdate = datetime.today()
    l_date = date(curdate.year, curdate.month, curdate.day)
    a = l_date.day
    b = l_date.month
    if (b == 1):
        b = "Января"
    elif (b == 2):
        b = "Февраля"
    elif (b == 3):
        b = "Марта"
    elif (b == 4):
        b = "Апреля"
    elif (b == 5):
        b = "Мая"
    elif (b == 6):
        b = "Июня"
    elif (b == 7):
        b = "Июля"
    elif (b == 8):
        b = "Августа"
    elif (b == 9):
        b = "Сентября"
    elif (b == 10):
        b = "Октября"
    elif (b == 11):
        b = "Ноября"
    else:
        b = "Декабря"
    c = l_date.year
    result = str(a) + " " + str(b) + " " + str(c) + " г."
    return str(result)


def getDayWeek():
    curdate = datetime.today()
    day = datetime.isoweekday(curdate)
    if day == 1:
        day_str = "Понедельник"
    elif day == 2:
        day_str = "Вторник"
    elif day == 3:
        day_str = "Среда"
    elif day == 4:
        day_str = "Четверг"
    elif day == 5:
        day_str = "Пятница"
    elif day == 6:
        day_str = "Суббота"
    else:
        day_str = "Воскресенье"
    return str(day_str)

# if int(delta / 7) % 2 == 1:


def getWeek():
    # curdate = datetime.today()
    # f_date = date(2017, 10, 26)
    # l_date = date(curdate.year, curdate.month, curdate.day)
    # delta = l_date - f_date

    # wek = 1
    # return week
    return str(2)
