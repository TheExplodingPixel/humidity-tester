#Get everything imported.
from sense_hat import SenseHat
from time import sleep
from datetime import datetime
import time
#Standard definitions
sense = SenseHat()
# Define some colours
g = (0, 255, 0) # Green
b = (0, 0, 0) # Black
#Define Finished Image
exclaimation_mark = [
    g, g, g, b, b, g, g, g,
    g, g, g, b, b, g, g, g,
    g, g, g, b, b, g, g, g,
    g, g, g, b, b, g, b, g,
    g, g, g, b, b, g, g, g,
    g, g, g, b, b, g, g, g,
    g, g, g, g, b, g, g, g,
    g, g, g, b, b, g, g, g
]
#Start the loop 48 times, as the process waits 5 minutes, times 48 equals four hours.
for i in range(48):
    humidity = sense.get_humidity()
    temp = sense.get_temperature()
    sense.show_message("Testing!")
    print(time.ctime())
    print("Humidity: %s %%rH" % humidity)
    print("Temperature: %s C" % temp)
    sleep(300)
#Show message when done!
else:
    sense.set_pixels(exclaimation_mark)
