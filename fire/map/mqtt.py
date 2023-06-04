
import json

import paho.mqtt.client as mqtt
from django.conf import settings

from .models import *
import pyowm
import csv 
from .FWI import *
from datetime import datetime

topics = ['v3/my-lora1-application@ttn/devices/eui-70b3d57edd05a535/up','v3/my-lora1-application@ttn/devices/eui-70b3d57ed005ca2c/up', 'v3/loraatest02@ttn/devices/eui-70b3d57ed005a5c4/up', 'v3/loraatest02@ttn/devices/eui-70b3d57ed005c92e/up']
def on_connect(mqtt_client, userdata, flags, rc):

    if rc == 0:
        print('Connected successfully')
        
        #yass card
        mqtt_client.subscribe(topics[0])

        #other card
        mqtt_client.subscribe(topics[1])
        mqtt_client.subscribe(topics[2])

    else:
        print('Bad connection. Code:', rc)

def on_message(mqtt_client, userdata, msg):
        # Decode the incoming message
        payload_dict =json.loads(msg.payload)
        print('----------------------------------------')
        print(f'Received message on topic: {msg.topic} with payload: {msg.payload}', '\n')
        
        referencep = msg.topic.split('/')[-2]
        print('---topic-reference',referencep)

        nodes = node.objects.filter(reference=referencep).order_by('-Idnode')
        
        if nodes:
            n = nodes[0]
            print('-----n',n.nom,' ------- ref-node',n.reference)
        
            temperature = payload_dict['uplink_message']['decoded_payload']['temperature']
            humidity = payload_dict['uplink_message']['decoded_payload']['humidity']
            Battery_level = payload_dict['uplink_message']['decoded_payload']['Battery_level']
            
            rssi = payload_dict['uplink_message']['rx_metadata'][0]['rssi']
            snr = payload_dict['uplink_message']['rx_metadata'][0]['snr']

            n.RSSI = rssi
            n.save()
            n.Battery_value =Battery_level
            n.save()


            print('payload-----temperature :', temperature, 'humidity :', humidity, 'rssi :', rssi, 'snr :', snr ,'Battery_level:',Battery_level, '\n')

            # Replace "YOUR_API_KEY" with your actual API key from OpenWeatherMap
            owm = pyowm.OWM("0f21fa98b6e075b77fd85b3af087e294")
                
            # Replace "City name" with the name of the city you want weather data for
            location = owm.weather_manager().weather_at_place('Bizerte, TN')
                
            weather = location.weather

            # Get the temperature, humidity, and wind speed
            temperature_owm = weather.temperature('celsius')['temp']
            humidity_owm = weather.humidity
            wind_speed = weather.wind()['speed']
            rain_volume = weather.rain.get('1h', 0)  # get rain volume in last 1 hour

                    
            datas = Data.objects.filter(node=n).order_by('-IdData')
            
            new_data = Data.objects.create(temperature=temperature, humidity=humidity, wind=wind_speed,rain=rain_volume, node=n)
            new_data.save()
            print('new_data ---------',new_data)
            
            
            with open('testBatch.csv', mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([datetime.today().strftime('%m/%d/%Y'), temperature, humidity, wind_speed, rain_volume, '0'])

            batchFWI('testBatch.csv')

            with open('testBatch.csv', mode='r') as file:
                        reader = csv.reader(file)
                        rows = list(reader)
                        last_row = rows[-1]
                        FWI = last_row[-1]

            fwi = float(FWI)
            n.FWI=fwi
            n.save()
            print('------mqt--FWI',n.FWI)



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
    