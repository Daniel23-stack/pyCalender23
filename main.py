import datetime

# Set up constants
DAYS = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')
MONTHS = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November')

print('calendar')

while True:
    print('Enter the year for the calendar:')
    response = input('>')

    if response.isdecimal() and int(response) > 0:
        year = int(response)
        break
    print('Enter a numeric year, like 2023.')

while True:
    print('Enter the month for the calendar: 1-12')
    response = input('>')

    if not response.isdecimal():
        print('Please enter a numeric month')
        continue

    month = int(response)
    if 1 <= month <= 12:
        break
    print('Please enter a number between 1 and 12')

def getCalendarFor(year, month):
    calTex = ""

    calTex += (' ' * 34) + MONTHS[month-1] + ' ' + str(year) + '\n'

    calTex += '...Sunday.....Monday....Tuesday...Wednesday...Thursday....Friday....Saturday..\n'

    weekSeparator = ('+----------' * 7) + '+\n'
    blankRow = ('| ' * 7) + '|\n'

    currentDate = datetime.date(year, month, 1)

    while currentDate.weekday() != 6:
        currentDate -= datetime.timedelta(days=1)

    while True:  # Loop over each week in the month.
        calTex += weekSeparator

        dayNumberRow = ''
        for i in range(7):
            dayNumberLabel = str(currentDate.day).rjust(2)
            dayNumberRow += '|' + dayNumberLabel + (' ' * 8)
            currentDate += datetime.timedelta(days=1)  # Go to next day.
        dayNumberRow += '|\n'  # Add the vertical line after Saturday.

        calTex += dayNumberRow
        for i in range(3):
            calTex += blankRow

        if currentDate.month != month:
            break

    calTex += weekSeparator
    return calTex

calTex = getCalendarFor(year, month)
print(calTex)

calendarFilename = 'calendar_{}_{}.txt'.format(year, month)
with open(calendarFilename, 'w') as fileObj:
    print('Saved to ' + calendarFilename)