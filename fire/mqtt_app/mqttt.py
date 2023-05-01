from map.mqtt import *
from map.models import *

import paho.mqtt.client as mqtt
from django.conf import settings

print('succeeeeeeeeeeeeeeessfully')

# Create a new MQTT client instance
client = mqtt.Client()

# Set the client's connection and message handling functions
client.on_connect = on_connect
client.on_message = lambda client, userdata, msg: on_message(client, userdata, msg)

# Set the client's username and password
client.username_pw_set(settings.MQTT_USER, settings.MQTT_PASSWORD)

# Connect to the MQTT broker
client.connect(
    host=settings.MQTT_SERVER,
    port=settings.MQTT_PORT,
    keepalive=settings.MQTT_KEEPALIVE
)

    # Start the MQTT loop (this function blocks and waits for incoming messages)
client.loop_forever()