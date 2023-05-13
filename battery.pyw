# python script showing battery details
import psutil
import webbrowser
# function returning time in hh:mm:ss
# def convertTime(seconds):
# 	minutes, seconds = divmod(seconds, 60)
# 	hours, minutes = divmod(minutes, 60)
# 	return "%d:%02d:%02d" % (hours, minutes, seconds)

# returns a tuple

filename = 'D:\Documents\py\open.html'

while(True):
    if(psutil.sensors_battery().percent<7):
        webbrowser.open_new_tab(filename)
        break
    else:
        continue



# print("Battery percentage : ", battery.percent)
# print("Power plugged in : ", battery.power_plugged)

# converting seconds to hh:mm:ss
# print("Battery left : ", convertTime(battery.secsleft))
