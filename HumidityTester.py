from sense_hat import SenseHat
from time import sleep
from datetime import datetime
import time

sense = SenseHat()


for i in range(48):
    humidity = sense.get_humidity()
    temp = sense.get_temperature()
    sense.show_message("Testing!")
    print(time.ctime())
    print("Humidity: %s %%rH" % humidity)
    print("Temperature: %s C" % temp)
    sleep(300)
else:
    sense.show_message("Done!")
    

