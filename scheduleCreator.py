import datetime

currentTime = datetime.datetime.now()
hour = currentTime.hour
minute = currentTime.minute


def createSchedule():
    schedule = [['Python video', 20], ['Python Project', 30], ['kleine pauze', 10],
                ['zang oefenen', 20], ['piano oefenen', 30],
                ['grote pauze', 30], ['project Munnik', 120], ['einde', 20]]

    print('Je planning voor vandaag:')

    for x in schedule:
        global minute, hour
        print(str(hour)+' '+str(minute)+' '+x[0])
        minute += x[1]
        keepTime()


def keepTime():
    global minute, hour
    while minute > 59:
        hour += 1
        minute -= 60

    if hour > 23:
        hour = 0


x = input('Nu beginnen? type y ')

if x == 'y':
    createSchedule()
else:
    y = input('welk uur(24H) ')
    hour = int(y)
    y = input('welke minuut ')
    minute = int(y)
    createSchedule()
