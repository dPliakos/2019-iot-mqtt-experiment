import sys
import paho.mqtt.client as paho
from Crypto.Cipher import AES

BROKER = "192.168.1.2"
PORT = 1883
TOPIC = "house/security"
key = 'B%RY55clWv^epbJ%00Kz#M9p'


if len(sys.argv) < 2:
    print("no message")
    exit(1)

user_input = bytes(sys.argv[1], 'utf-8')

length = 16 - (len(user_input) % 16)
user_input += bytes([length])*length

cipher = AES.new(key, AES.MODE_ECB)
msg =cipher.encrypt(user_input)

payload = msg.hex()

def on_publish(client,userdata,result):             #create function for callback
    print("data published \n")
    pass

client1= paho.Client("control1")                           #create client object
client1.on_publish = on_publish                          #assign function to callback
client1.connect(BROKER, PORT)                                 #establish connection
ret= client1.publish("{}".format(TOPIC),"{}".format(payload))                   #publish
