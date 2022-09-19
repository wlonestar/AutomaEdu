from datetime import datetime


# only for 2022-2023 1
def get_week_num(d=datetime.today()):
    return d.isocalendar().week - 34


# mon -> 1, ect..
def get_weekday(d=datetime.today()):
    return datetime.weekday(d) + 1


def get_format_date(d=datetime.today()):
    return d.strftime('%Y年%m月%d日')


if __name__ == '__main__':
    if datetime.now() < datetime(2023, 1, 1):
        print("run")
    # get today
    print(datetime.today().strftime('%Y年%m月%d日'))
    print(get_format_date(datetime.today()))
    # get weekday
    print(datetime.weekday(datetime.today()))
    print(get_weekday(datetime.today()))
    print(get_weekday(datetime(2022, 11, 15)))
    # get week num
    print(get_week_num(datetime(2022, 11, 15)))
    print(get_week_num(datetime.today()))
