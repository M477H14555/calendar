import datetime

DAYS = (
    "MONDAY",
    "TUESDAY",
    "WEDNESDAY",
    "THURSDAY",
    "FRIDAY",
    "SATURDAY",
    "SUNDAY"
)

MONTHS = (
    "JANUARY",
    "FEBRUARY",
    "MARCH",
    "APRIL",
    "MAY",
    "JUNE",
    "JULY",
    "AUGUST",
    "SEPTEMBER",
    "OCTOBER",
    "NOVEMBER",
    "DECEMBER"
)

while True:
    print("Enter the year for the calendar (IN DIGITS): ")
    yy = input("> ")

    if yy.isdecimal():
        if int(yy) > 0:
            yy = int(yy)
            print("CONFIRMED\n")
            break

while True:
    print("Enter the month for the calendar (IN DIGITS): ")
    mm = input("> ")

    if not mm.isdecimal():
        print("DENIED - Please write is in the digits form. E.g, January = 1, February = 2 and so on.")
        continue

    mm = int(mm)
    if 1 <= mm <= 12:
        print("CONFIRMED\n")
        break
    else:
        print("\nDENIED - Your number doesn't fit in the range, please choose another month.\n")

calendar = f"{MONTHS[mm-1]} {yy}".center(80)
calendar += "\n   MONDAY    TUESDAY  WEDNESDAY   THURSDAY    FRIDAY    SATURDAY     SUNDAY\n"
week_sep = "+----------"*7
BLNKRW =  "|          "*7

TIME = datetime.date(yy, mm, 1)
print(f"NOW: {TIME}")
weekday = TIME.weekday()

while weekday != 0:
    TIME -= datetime.timedelta(days=1)
    weekday = TIME.weekday()

while True:
    day_row = ""
    calendar += week_sep + "+"

    for i in range(7):
        day_label = str(TIME.day)

        if TIME.month != mm:
            day_label = "  "
        else:
            if len(day_label) < 2:
                day_label = f" {day_label}"

        day_row += "|" + day_label + " "*8
        TIME += datetime.timedelta(days=1)

    day_row += "|\n"
    calendar += f"\n{day_row}"
    for _ in range(3):
        calendar += BLNKRW + "|\n"

    if TIME.month != mm:
        calendar += week_sep + "+"
        break

print(calendar)



