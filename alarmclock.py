import datetime


def alarmclock():
    "Show Time"
    time = datetime.datetime.now()
    print ("Current Time:")
    new_time = time.strftime("%H:%M:%S")
    print (new_time)

    "Set Alarm"
    print ('Please put your alarm time in single quotes')
    alarm_time = eval(input("Set an alarm 'H:M:S' :"))
    print("This alarm would set off at",alarm_time)
           
alarmclock()
