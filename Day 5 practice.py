
def do_year():
    year = int(input("Enter the year: "))
    if year % 4 == 0:
        c = year % 100
        if c != 0:
            leap_year = True
        else:
            d = year % 400
            if d == 0:
                leap_year = True
            else:
                leap_year = False
    else:
        leap_year = False

    def do_month():
        month = int(input("Enter the month: "))
        days_plain = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 31, 10: 31, 11: 30, 12: 31}
        days_leap = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 31, 10: 31, 11: 30, 12: 31}
        total = 0
        if month > 12 or month <= 0:
            print("Error")
        elif leap_year is True:
            for n in range(1, month):
                total += days_leap[n]
        else:
            for n in range(1, month):
                total += days_plain[n]

        day = int(input("Enter the day: "))
        total2 = 0
        if 0 < day <= 31:
            total2 += day
            print(total2+total)
        else:
            print("Error")
    do_month()

if __name__ == '__main__':
    do_year()

























