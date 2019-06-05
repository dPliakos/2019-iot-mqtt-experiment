import time
import schedule
import paho.mqtt.client as paho


"""
In this exaple we just change the a flag, in a real scenario we would set
two crons, one for lights on at X time and one for closing the lights at y time.
"""



BROKER = "192.168.1.2"
PORT=1883
TOPIC="house/common/livingroom/lights"

LIGHTS_STATUS = False

def turn_all_on():
    payload = "on"
    ret= client1.publish("{}".format(TOPIC),"{}".format(payload))  # publish

def turn_all_off():
    payload = "off"
    ret= client1.publish("{}".format(TOPIC),"{}".format(payload))  # publish


def fake_decide_from_time():
    print("Fake decision make")

    global LIGHTS_STATUS
    if LIGHTS_STATUS:
        turn_all_off()
        LIGHTS_STATUS = False;
    else:
        turn_all_on()
        LIGHTS_STATUS = True;

def on_publish(client,userdata,result):             #create function for callback
    print("data published \n")
    pass





client1= paho.Client("control1")                           #create client object
client1.on_publish = on_publish                          #assign function to callback
client1.connect(BROKER, PORT)                                 #establish connection

# define the cron
schedule.every(2).seconds.do(fake_decide_from_time)

while 1:
    schedule.run_pending()
    time.sleep(1)
