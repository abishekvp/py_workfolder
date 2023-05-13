import pywhatkit as pw
import datetime


def send():
    message = 'I will catch u later,\n now I am litle busu right now'
    time = datetime.datetime.now()
    hour = time.hour
    min = time.minute
    sec = time.second
    min += 1
    pw.sendwhatmsg(contact_name, message, hour, min, 10)
