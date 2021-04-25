from pylgbst.hub import *
from pylgbst import *
import rover


print("connecting")
connection = get_connection_bluepy(hub_mac="00:16:53:A2:DB:9A")

hub = MoveHub(connection=connection)


bot = rover.rover(hub, COLORS)

def sense(clr, distance):
    global bot
    bot.sense(clr, distance)


hub.led.set_color(9)
hub.vision_sensor.subscribe(sense, mode=VisionSensor.COLOR_DISTANCE_FLOAT)
time.sleep(200) # play with sensor while it waits   
hub.vision_sensor.unsubshub,cribe(sense)
