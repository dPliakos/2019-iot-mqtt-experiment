import paho.mqtt.client as mqtt
from Crypto.Cipher import AES

BROKER = "192.168.1.2"
TOPIC = "house/security"
key = 'B%RY55clWv^epbJ%00Kz#M9p'


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(TOPIC)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    # TODO: Add the decryption here 
    decipher = AES.new(key, AES.MODE_ECB)
    decrypted = decipher.decrypt(msg.payload.decode())
    print(msg.topic+" "+str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
